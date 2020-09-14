import os
import shutil
import datetime
from platform import system
import json
#from win10toast import ToastNotifier

if __name__ == "__main__":
        
    # open the settings
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, "settings.json"), "r") as json_file:
        data = json.load(json_file)
        backup_dir = data["backupdir"]
        target_dir = data["targetdir"]
        start_days = data["autostart"]
        delete_days = data["autodelete"]
        notification = data["notification"]
    
    # checking if a new backup will created or deleted
    backup_counter = 0
    age = None
    test = True
    for filename in os.listdir(target_dir):
        if filename.startswith("Backup_"):
            backup_counter += 1
            if age == None or age > os.path.getmtime(os.path.join(target_dir, filename)):
                age = os.path.getmtime(os.path.join(target_dir, filename))
                oldest = filename
            filename = filename.split("_")
            filename = filename[1].split(".")
            filename = filename[0].split("-")
            year = int(filename[0])
            month = int(filename[1])
            day = int(filename[2])
            backup_date = datetime.date(year, month, day)
            time = datetime.date.today() - backup_date
            if start_days != None and time.days >= int(start_days) :
                continue
            else:
                test = False
                continue

    #creating process
    if os.path.isfile(os.path.join(target_dir, f"Backup_{datetime.date.today()}")) == False and test != False:
        shutil.make_archive(os.path.join(target_dir, f"Backup_{datetime.date.today()}"), "zip", backup_dir)
    if notification == True:
        if system() == "Linux":
            os.system("notify-send Monika-backup-maschine Backup' 'created")

    #deleting process
    if delete_days != None and backup_counter > int(delete_days):
        os.remove(os.path.join(target_dir, oldest))
        if notification == True:
            if system() == "Linux":
                os.system("notify-send Monika-backup-maschine Backup' 'deleted")

    #notifcation

    
        #if system() == "Windows":
            #toaster = ToastNotifier()
           # toaster.show_toast("Monika's-backup-maschine", "Backup created", icon_path="monika_bild.ico", threaded=True)
