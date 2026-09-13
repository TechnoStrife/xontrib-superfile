# Overview
[superfile](https://github.com/yorukot/superfile) support function for xonsh shell


## Installation

To install use pip:
``` bash
xpip install xontrib-superfile
```
``` bash
xpip install -U git+https://github.com/TechnoStrife/xontrib-superfile
```

### Nix
If you're using nix, you can use [NUR](https://github.com/drmikecrowe/nur-packages) to install like so:
```nix
    programs.xonsh =  {
        extraPackages = ps: with ps; [
            pkgs.nur.repos.xonsh-xontribs.xontrib-superfile
        ];
    };
```

Or, you can import this repo directly into your flake and use the package.

## Usage
Enable `cd_on_quit` in [superfile config](https://superfile.dev/configure/superfile-config/):
```
cd_on_quit = true
```

This xontrib adds `spf` alias function.
``` bash
$ xontrib load superfile
$ spf
```

Now you can quit superfile normally and xonsh will cd into the last directory.

You can also add your own alias like this: `aliases['s'] = 'spf'`.

`superfile` can also be launched with shortcut `Ctrl+N`. 
This can be changed by setting `$XONSH_SUPERFILE_KEY="c-n"` before loading or disabled with `$XONSH_SUPERFILE_KEY=""`. 
(PS [PTK's keybinding guide](https://python-prompt-toolkit.readthedocs.io/en/master/pages/advanced_topics/key_bindings.html#list-of-special-keys) 
for full list of key names, not all can be used as a shortcut.)

## Credits

This package was created from [xontrib broot example](https://github.com/jnoortheen/xontrib-broot).
