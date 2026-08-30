import shutil
import subprocess
from pathlib import Path
from xonsh.built_ins import XSH
from xonsh.tools import uncapturable


superfile = "superfile"  # for nixos
if shutil.which("superfile") is None:
    superfile = "spf"


@uncapturable
def _sf(args, stdin=None, stdout=None, stderr=None):
    spf_last_dir = Path(XSH.env.get("HOME") + "/.local/state/superfile/lastdir")
    status_code: int = subprocess.call(
        (superfile,) + tuple(args),
        stdin=stdin,
        stderr=stderr,
        stdout=stdout,
    )
    if status_code == 0 and spf_last_dir.is_file():
        with spf_last_dir.open() as f:
            content = f.read()
            if content:
                XSH.builtins.evalx(content)
        spf_last_dir.unlink()

    return status_code


XSH.aliases["sf"] = _sf


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

    @handler("XONSH_SUPERFILE_KEY", "c-n")
    def start_superfile(event):
        _sf([])


if __name__ == "__main__":
    from xonsh.built_ins import XSH

    XSH.load()
    data = XSH.execer.eval("")
