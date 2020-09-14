import tkinter
from tkinter import filedialog, ttk
import Monika_backup_maschine



class MainApplication:
    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.grid()


        self.backupdir_label = tkinter.Label(frame, text="Select your persistent folder", font = "Helvetica 10 bold")
        self.backupdir_label.grid(column=0, row=0, pady=15)

        self.backupdir_entry = tkinter.Entry(frame, width=40, font = "Helvetica 10")
        self.backupdir_entry.grid(column=0, row=1, pady=0)

        self.backupdir_button = tkinter.Button(frame, command=lambda: self.directory_click(self.backupdir_entry) , text="Select", font = "Helvetica 10")
        self.backupdir_button.grid(column=1, row=1)


        #targetdir path
        self.targetdir_label = tkinter.Label(frame, text= "Select the folder where you want your backups", font = "Helvetica 10 bold")
        self.targetdir_label.grid(column=0, row=2, pady=15)

        self.targetdir_entry = tkinter.Entry(frame, width=40, font = "Helvetica 10")
        self.targetdir_entry.grid(column=0, row=3)

        self.targetdir_button = tkinter.Button(frame, command=lambda: self.directory_click(self.targetdir_entry), text="Select", font = "Helvetica 10")
        self.targetdir_button.grid(column=1, row=3)


        #autostart

        self.autostart_label = tkinter.Label(frame, text="Enable automatic backup (backups automatically in the given number of days):", font = "Helvetica 10 bold")
        self.autostart_label.grid(column=0, row=4, pady=15)

        self.autostart_checkbutton = ttk.Checkbutton(frame, command=self.check_auto)
        self.autostart_checkbutton.state(["!alternate"])
        self.autostart_checkbutton.grid(column=1, row=4)

        self.autostart_option = tkinter.ttk.Combobox(frame, value=[ i for i in range(1, 31)], state="disabled", font = "Helvetica 10")
        self.autostart_option.current(6)
        self.autostart_option.grid(column=0, row=5)


        #delete backups



        self.autodelete_label = tkinter.Label(frame, text="Enable automatic delete (deletes every older backup up to the given number): ", font = "Helvetica 10 bold")
        self.autodelete_label.grid(column=0, row=6, pady=15)

        self.autodelete_checkbutton = ttk.Checkbutton(frame, command=self.check_auto)
        self.autodelete_checkbutton.state(["!alternate"])
        self.autodelete_checkbutton.grid(column=1, row=6)

        self.autodelete_option = tkinter.ttk.Combobox(frame, value=[i for i in range(1, 16)], state="disabled", font = "Helvetica 10")
        self.autodelete_option.current(4)
        self.autodelete_option.grid(column=0, row=7)


        # notfication

        self.notification_label = tkinter.Label(frame, text="Enable notification:", font = "Helvetica 10 bold")
        self.notification_label.grid(column=0, row=8, padx=0, pady=15)

        self.notification_checkbutton = ttk.Checkbutton(frame)
        self.notification_checkbutton.state(["!alternate"])
        self.notification_checkbutton.grid(column=1, row=8)




        #submit buttons


        self.savechanges_button = tkinter.Button(frame, text="save config", command=lambda: Monika_backup_maschine.save_settings(self), font = "Helvetica 10 bold")
        self.savechanges_button.grid(column=0, row=9)

        self.createbackup_button = tkinter.Button(frame, text="create backup", command=lambda: Monika_backup_maschine.monika_just_backup(self), font = "Helvetica 10 bold")
        self.createbackup_button.grid(column=1, row=9)

    
    def directory_click(self, directory):
        root.dir_ask = tkinter.filedialog.askdirectory(title="Select your folder!")
        directory.delete(0, len(directory.get()))
        directory.insert(0, root.dir_ask)

    def check_auto(self):
        if self.autostart_checkbutton.instate(["selected"]):
            self.autostart_option["state"] = "normal"
        else:
            self.autostart_option["state"] = "disabled"

        if self.autodelete_checkbutton.instate(["selected"]):
            self.autodelete_option["state"] = "normal"
        else:
            self.autodelete_option["state"] = "disabled"
        



if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Monika's backup maschine")
    root.geometry("700x500")
    root.tk.call("wm", "iconphoto", root._w, tkinter.PhotoImage(file=f"{Monika_backup_maschine.location()}/monika_bild.png"))
    c = MainApplication(root)

    Monika_backup_maschine.read_settings(c)
    root.mainloop()


