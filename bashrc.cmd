@echo off

doskey ls=dir $*
doskey cp=copy $*
doskey cat=type $*
doskey pwd=cd

rem Get this files path
rem %~dp0 will return path to batch location
rem source: https://stackoverflow.com/questions/17063947/get-current-batchfile-directory
doskey touch=python %~dp0\linux_terminal_commands.py touch $*
doskey rm=python %~dp0\linux_terminal_commands.py rm $*
doskey mv=python %~dp0\linux_terminal_commands.py mv $*
doskey tree=python %~dp0\linux_terminal_commands.py _tree $*


rem tree doesn't show files by default, /f shows the files
rem aliasing it in this way makes tree show the current
rem directly regardless of if you pass the directly you
rem want to see as an argument
rem doskey tree=tree /f

