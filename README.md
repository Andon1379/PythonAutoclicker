# PythonAutoclicker
An autoclicker in python

**Windows** Needs to install [Git Scm](https://git-scm.com/downloads) and [Python3](https://www.python.org/downloads/windows/)

**Unix** Needs to install [Python3](https://www.python.org/downloads/source/) [intro to install using tar.*](https://stackoverflow.com/questions/36014334/how-to-install-python-packages-from-the-tar-gz-file-without-using-pip-install)

Resources 

https://nitratine.net/blog/post/python-auto-clicker/

https://stackoverflow.com/questions/54293000/pynput-same-controller-keyboard-and-mouse 

https://docs.python.org/3.6/library/random.html#random.sample

https://pypi.org/project/pynput/


librarys and stuff used (dependencies)

python 3.6.9 (rip python 2)

pynput (https://pypi.org/project/pynput/)

----------------------------------------

Andon1379's Autoclicker (ver 1.3.5)

------------Autoclicking------------

autoclicks (by default) every 0.01 second -- this can be changed in 2 ways;

directly/manually changing the integer related to the variable delay

or

pressing 'r' to generate random times between (a default) 0.1 and 0.01 seconds each click

(this can also be changed manually/directly by changing the integer values for the rand_delay_max and rand_delay_min).


-------------Toggle Mouse Button------------

you can toggle the mouse button pressed with 'k' (by default -- this can be changed by changing the letter in the toggle_key variable).


------------Starting, Stopping, and Exiting the code------------

You can make it start clicking by pressing '.' after executing the program Autoclicker.pyw-- this can also be used to pause the code

To stop the code completely, press ','

(The controls for these, of course, can all be changed, by changing the key(s) for the start_stop_key, and exit_key respectively)


-------------Stuff Remembered Between runs------------

The only things that the program remembers inbetween runs is the amount of times it's clicked (which is saved in stats.txt),

the last mouse button pressed, and if it was clicking with a random delay (both of which are saved in mouseButton.txt)


------------Other Misc. Stuff to Know------------

Join the Discord! https://discord.gg/8AE3MZb

my website --- https://andrews-site.glitch.me/


------------Credits--------------

Me (Andon1379) -- writing most of the modifications

Mark (idk your last name) -- the idea to make this in the first place

All the resources above -- base code / debugging help 
