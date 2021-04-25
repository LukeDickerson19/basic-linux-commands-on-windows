@echo off



doskey ls=dir $*
doskey cp=copy $*
doskey cat=type $*
doskey pwd=cd
doskey touch=python C:\Users\ld085a\linux_terminal_commands.py touch $*
doskey rm=python C:\Users\ld085a\linux_terminal_commands.py rm $*
doskey mv=python C:\Users\ld085a\linux_terminal_commands.py mv $*

rem tree doesn't show files by default, /f shows the files
rem aliasing it in this way makes tree show the current
rem directly regardless of if you pass the directly you
rem want to see as an argument
doskey tree=tree /f

