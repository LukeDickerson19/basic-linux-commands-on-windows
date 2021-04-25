@echo off

doskey ls=dir $*
doskey cp=copy $*
doskey cat=type $*
doskey pwd=cd

rem Get this files path
rem %~f0 will return the full pathname (e.g. W:\scripts\mybatch.cmd
rem source: https://stackoverflow.com/questions/17063947/get-current-batchfile-directory
doskey touch=python %~dp1\linux_terminal_commands.py touch $*
doskey rm=python %~dp1\linux_terminal_commands.py rm $*
doskey mv=python %~dp1\linux_terminal_commands.py mv $*

rem tree doesn't show files by default, /f shows the files
rem aliasing it in this way makes tree show the current
rem directly regardless of if you pass the directly you
rem want to see as an argument
doskey tree=tree /f

