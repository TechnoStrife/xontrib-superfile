import os
import shlex
import shutil
import platform
import functools
import subprocess
from pathlib import Path
from xonsh.built_ins import XSH
from xonsh.tools import uncapturable


@functools.cache
def get_superfile_path():
    if platform.system() == 'Windows':
        return XSH.env.get('LOCALAPPDATA') + r'\Programs\superfile\spf.exe'
    if shutil.which('superfile') is not None:
        return 'superfile'  # for nixos
    return 'spf'


@functools.cache
def get_spf_last_dir():
    os_name = platform.system()
    if os_name == 'Windows':
        # superfile escapes quotes like for posix on windows
        return Path(XSH.env.get('LOCALAPPDATA') + r'\superfile\lastdir')
    elif os_name == 'Darwin':
        return Path(XSH.env.get('HOME') + '/Library/Application Support/superfile/lastdir')
    elif 'XDG_STATE_HOME' in XSH.env:
        return Path(XSH.env.get('XDG_STATE_HOME') + '/superfile/lastdir')
    else:
        return Path(XSH.env.get('HOME') + '/.local/state/superfile/lastdir')


@uncapturable
def _spf(args, stdin=None, stdout=None, stderr=None):
    spf_last_dir = get_spf_last_dir()

    status_code: int = subprocess.call(
        (get_superfile_path(),) + tuple(args),
        stdin=stdin,
        stderr=stderr,
        stdout=stdout,
    )

    if status_code == 0 and spf_last_dir.is_file():
        with spf_last_dir.open() as f:
            content = f.read()
            if content:
                _, path = shlex.split(content)
                os.chdir(path)
        spf_last_dir.unlink()

    return status_code


XSH.aliases['spf'] = _spf


@XSH.builtins.events.on_ptk_create
def custom_keybindings(bindings, **kw):
    def handler(key_name: str, default: str):
        def do_nothing(_):
            pass

        if key_name not in XSH.env:
            key = default
        else:
            key = XSH.env.get(key_name)
        if key:
            return bindings.add(key)
        return do_nothing

    @handler('XONSH_SUPERFILE_KEY', 'c-n')
    def start_superfile(event):
        _spf([])


if __name__ == '__main__':
    from xonsh.built_ins import XSH

    XSH.load()
    data = XSH.execer.eval('')
