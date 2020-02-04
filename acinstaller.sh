#!/bin/bash

echo Make Sure Python3 Is Installed
echo Check by Running python3 --version
function pause(){
	read -p "$*"
}
cd ~
git clone https://github.com/Andon1379/PythonAutoclicker >> /dev/null
cd ~/PythonAutoclicker/Andrew\'s\ Autoclicker\ \(version\ 1.3.5\)
rm *.bat >> /dev/null
cd ../..
if test -d ~/Desktop
then
	mkdir ~/Desktop/Andrew\'s\ AutoClicker
else
	mkdir ~/Desktop/
	mkdir ~/Desktop/Andrew\'s\ AutoClicker
fi
cp -r ~/PythonAutoclicker/Andrew\'s\ Autoclicker\ \(version\ 1.3.5\) ~/Desktop/Andrew\'s\ AutoClicker >> /dev/null
mkdir ~/Andrew\'s\ AutoClicker
mv ~/PythonAutoclicker/Andrew\'s\ Autoclicker\ \(version\ 1.3.5\)/* ~/Andrew\'s\ AutoClicker >> /dev/null
rm -rf ~/PythonAutoclicker/
cd ~/Andrew\'s\ AutoClicker
chmod -w autoclicker
sudo chmod +rx autoclicker 
sudo cp autoclicker /bin/
echo Run autoclicker in terminal to activate Autoclicker
pause 'Press Enter to Exit'
