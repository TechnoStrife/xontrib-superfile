# Overview
[superfile](https://github.com/yorukot/superfile) support function for xonsh shell


## Installation

To install use pip:

``` bash
xpip install xontrib-superfile
# or: xpip install -U git+https://github.com/TechnoStrife/xontrib-superfile
```

## Usage
It adds `sf` alias function. So commands like `cd` will work from superfile.
``` bash
$ xontrib load superfile
$ sf
```

`superfile` can also be launched with shortcut `Ctrl+N`. 
This can be changed by `$XONSH_SUPERFILE_KEY="c-n"` or disabled with `$XONSH_SUPERFILE_KEY=""`. 
(PS [PTK's keybinding guide](https://python-prompt-toolkit.readthedocs.io/en/master/pages/advanced_topics/key_bindings.html#list-of-special-keys) 
for full list of key names.)

## Credits

This package was created from [xontrib broot example](https://github.com/jnoortheen/xontrib-broot).
