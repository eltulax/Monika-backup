import os
import shutil
import datetime
import getpass
from platform import system
import json
#from win10toast import ToastNotifier

def location():
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    return __location__


def read_settings(self):
    try:
        with open(os.path.join(location(), "settings.json"), "r") as json_file:
            data = json.load(json_file)
            self.backupdir_entry.insert(0, data["backupdir"])
            self.targetdir_entry.insert(0, data["targetdir"])
            if data["autostart"] != None:
                self.autostart_checkbutton.state(["selected"])
                self.check_auto()
                self.autostart_option.delete(0)
                self.autostart_option.insert(0, data["autostart"])
            if data["autodelete"] != None:
                self.autodelete_checkbutton.state(["selected"])
                self.check_auto()
                self.autodelete_option.delete(0)
                self.autodelete_option.insert(0, data["autodelete"])
            if data["notification"] == True:
                self.notification_checkbutton.state(["selected"])
    except:
        return




def save_settings(self):
    settings = {}
    settings["backupdir"] = self.backupdir_entry.get()
    settings["targetdir"] = self.targetdir_entry.get()
    if str(self.autostart_option["state"]) == "disabled":
        settings["autostart"] = None
    else:
        settings["autostart"] = self.autostart_option.get()
        autostart()

    
    if str(self.autodelete_option["state"]) == "disabled":
        settings["autodelete"] = None
    else:
        settings["autodelete"] = self.autodelete_option.get()
        autostart()
        

    if self.notification_checkbutton.instate(["selected"]):
        settings["notification"] = True
    else:
        settings["notification"] = False

    if str(self.autostart_option["state"]) == "disabled" and str(self.autodelete_option["state"]) == "disabled":
        delete_auto()

    with open(os.path.join(location(), "settings.json"), "w") as json_file:
        json.dump(settings, json_file)



def monika_just_backup(self):
    if self.targetdir_entry.get().endswith("/") == False:
        targetdir = self.targetdir_entry.get() + "/" 




    shutil.make_archive(targetdir + f"Backup_{datetime.date.today()}", "zip", self.backupdir_entry.get())
    if self.notification_checkbutton.instate(["selected"]):
        if system() == "Linux":
            os.system("notify-send Monika-backup-maschine Backup' 'created")
        
       # if system() == "Windows":
         #   toaster = ToastNotifier()
          #  toaster.show_toast("Monika's-backup-maschine", "Backup created", icon_path="monika_bild.ico", threaded=True)



def autostart():
    if system() == "Linux":
        #creating .desktop file
        with open(os.path.join(os.path.expanduser("~"), ".config", "autostart", "Monika's-backup-maschine.desktop"), "w") as f:
            f.write("[Desktop Entry]" + "\n" + "Encoding=UTF-8" + "\n" + "Name=Monika's-backup-maschine" + "\n" + "Comment=Automatic Monika backup" + "\n" + "Icon=gnome-info" 
                    + "\n" + f"Exec=sleep 30; python3 {os.path.join(os.path.dirname(os.path.realpath(__file__)))}" + "/" + "autostart.py" + "\n" + "Terminal=false" + "\n" + "Type=Application")

    elif system() == "Windows":
        USER_NAME = getpass.getuser()
        file_path = os.path.dirname(os.path.realpath(__file__)) + "\\" #+ os.path.basename(os.path.realpath("autostart.exe"))
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(bat_path + '\\' + "monika_backup.bat", "w+") as bat_file:
            #bat_file.write(r'start "" %s' % file_path)
            bat_file.write('cd' + " " + file_path + "\n" + 'start autostart.exe')



def delete_auto():
    if system() == "Linux":
        #if os.path.exists(os.path.join("/home/benny/.config/autostart/Textdatei.txt")) == True:
           # print("test")
        os.remove(os.path.join("/home/benny/.config/autostart/Textdatei.txt"))
    
    elif system() == "Windows":
        USER_NAME = getpass.getuser()
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        if os.path.exists(bat_path + '\\' + "monika_backup.bat"):
            os.remove(bat_path + '\\' + "monika_backup.bat")
