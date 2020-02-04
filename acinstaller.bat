@echo off
echo This Program Requires Python3 and Git Scm
echo Make Sure This Is Installed On Your System
echo And Added To Path
pause
@echo on
copy acinstaller.bat %userprofile%\acinstaller.bat
cd %userprofile%
git clone https://github.com/Andon1379/PythonAutoclicker
cd "%userprofile%\PythonAutoclicker\Andrew's Autoclicker (version 1.3.5)"
erase *.sh
erase autoclicker
cd %userprofile%
move "%userprofile%\PythonAutoclicker\Andrew's Autoclicker (version 1.3.5)" "%userprofile%\Desktop\Andrew's Autoclicker"
rmdir %userprofile%\PythonAutoclicker\
cls
cd "%userprofile%\Desktop\Andrew's Autoclicker"
call AutoClicker.bat "%windir%\system32\cmd.exe" startmenu
@echo off
echo done
timeout /t 10
