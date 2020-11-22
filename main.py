import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

#If this is not the first time using the GUI then this code block will
#add previously opened apps to the screen on start up.
if os.path.isfile("save.txt"):
    with open("save.txt", "r") as f:
        tempApps = f.read()
        tempApps = tempApps.split(",")
        apps = [x for x in tempApps if x.strip()]

#Function that handles the event of a user adding an app to the app list
def addApp():
    #remove current selections when adding a new app. Prevents duplications
    for widget in frame.winfo_children():
        widget.destroy()

    #Opens a windows file explorer dialog to allow users to select files to be opened
    #Contains a filter feature to filter by executables only or all file types.
    fileName = filedialog.askopenfilename(initialdir="/", title="Select File", 
                                      filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(fileName)
    print(fileName)
    #Post current selected files to be opened on screen for user
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()
#Function that handles button click to run all selected apps.
def runApps():
    for app in apps:
        os.startfile(app)

#Set Up the window where the GUI will be contained
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

#Set up a frame inside the larger window
frame = tk.Frame(root, bg="white")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

#The open file button
openFile = tk.Button(root, text="Open File", padx=10, pady=5, foreground="white", 
                           bg="#263D42", command=addApp)                         
openFile.pack()

#The run apps button
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, foreground="white", bg="#263D42", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

#Write currently selected apps to be opened into a file for reusability.
#The apps path will be written to this file and can thus be opened immediately
#the next time the user uses the app
with open("save.txt", "w") as f:
    for app in apps:
        f.write(app + ",")