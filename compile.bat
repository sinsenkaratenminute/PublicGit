for /R %%i in (*.sln) do (MSBuild.exe /p:Configuration=Release "%%i")
pause