@echo off

set FileName=%~n0

cd /d %~dp0
pyinstaller %FileName%.py --onefile --noconsole

exit