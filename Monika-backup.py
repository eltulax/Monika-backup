
# imports
import os
import shutil
import datetime
import getpass
from platform import system


# variables and paths
dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
test = True
today = datetime.date.today()
name = f"Backup_{today}"

# open the settings.txt
with open(os.path.join(dir_path, "settings.txt"), "r") as f:
    settings = f.read()

settings = settings.split("\n")
try:
    backup_dir = settings[0]
    target_dir = settings[1]
    period = int(settings[2])
    autostart = int(settings[3])
except:
    print("settings.txt is wrong configured")
    quit()


# making the target directory, if it doesnt exist
if os.path.exists(target_dir) == False:
    os.mkdir(target_dir)


# checking if a new backup will created 
for filename in os.listdir(target_dir):
    if filename.startswith("Backup_"):
        filename = filename.split("_")
        filename = filename[1].split(".")
        filename = filename[0].split("-")
        year = int(filename[0])
        month = int(filename[1])
        day = int(filename[2])
        backup_date = datetime.date(year, month, day)
        time = today - backup_date
        if time.days >= period:
            continue
        else:
            test = False
            break



#probably unnecessary path checking

if target_dir.endswith("/") == False and system() != "Windows" :
    target_dir += "/" 

elif target_dir.endswith("\\") == False and system() == "Windows":
    target_dir += "\\"



# creating the backup

if os.path.isfile(target_dir + name) == False and test != False:
    shutil.make_archive(target_dir + "/" + name, "zip", backup_dir)
    print("Backup was created")


#autostart for linux ubuntu-based distros

if autostart == 1 and system() == "Linux" and os.path.isfile(os.path.join(os.path.expanduser("~"), ".config", "autostart", "Monika-backup.desktop")) == False:
    with open(os.path.join(os.path.expanduser("~"), ".config", "autostart", "Monika-backup.desktop"), "w") as f:
        f.write("[Desktop Entry]" + "\n" + "Encoding=UTF-8" + "\n" + "Name=Monika backup" + "\n" + "Comment=Automatic Monika backup" + "\n" + "Icon=gnome-info" + "\n" + f"Exec=python3 {dir_path}" + "/" + __file__ + "\n" + "Terminal=false" + "\n" + "Type=Application" + "\n" + "Categories=" + "\n" + "X-GNOME-Autostart-enabled=true")



# autostart for windows

elif autostart == 1 and system() == "Windows":
    USER_NAME = getpass.getuser()
    file_path = os.path.dirname(os.path.realpath(__file__)) + "\\" + os.path.basename(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "monika_backup.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)


quit()
