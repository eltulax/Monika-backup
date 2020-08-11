# Monika-backup
Python Script to automatically backup Monika

Info:
This script is just designed for the modifikation "Monika After Story" of the game "Doki Doki Literature Club!".
Game: https://ddlc.moe/
Mod: https://www.monikaafterstory.com/


Instructions:

To run the script you need to have python 3.6 or higher installed on your system!

Step 1:
Download the to files.

Step 2:
Edit the settings.txt.
The first line should be your path to your folder, where the persistent file is located.
When you do not know where this is, here is a detailed instruction: https://github.com/Monika-After-Story/MonikaModDev/wiki/FAQ#i-want-to-back-up-my-persistent

The second line should be your path to your folder, where you want your backups.

The third line is the frequency of the backup creation in days.

The fourth line activates the autostart at 1 and disables it at 0.
This works currently only on Windows and Ubuntu-based distributions.
On other operating sysetms you should be able to autostart it manually with crontab 

Please delete all comments made in the settings.txt, or the script will not function.
Also the settings.txt must be in the same folder than the python script.
