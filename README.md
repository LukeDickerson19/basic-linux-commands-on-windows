# basic-linux-commands-on-windows
Windows command prompt aliases of basic linux terminal commands



### DESCRIPTION:

Windows command prompt aliases (aka doskeys in Windows) of basic linux terminal commands:
```
ls, mv, cp, cat, pwd, touch, rm
```

If you can, another option is the [Windows Subsystem for Linux](https://www.laptopmag.com/articles/use-bash-shell-windows-10)

### SETUP:
```
run: "regedit" in the windows command prompt
in the popup, go to path: HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor
right click "Command Processor" > New > String Value
set the name to "AutoRun"
right click the string value > Modify ...
set the "Value data" to the path of the bashrc.cmd file
	aka this repos path, placed where ever you want, plus "\bashrc.cmd"
```
[source: Ctrl + F for "Humdinger", this is his answer](https://superuser.com/questions/144347/is-there-windows-equivalent-to-the-bashrc-file-in-linux)

### REQUIREMENTS:
```
Windows OS
python 3.6+
```
