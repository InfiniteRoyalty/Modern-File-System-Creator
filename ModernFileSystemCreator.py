import tkinter as tk
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import os

# System Settings
ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

# window
window = ctk.CTk()
window.title('File System Creator')
window.geometry('500x500')

# UI Elements/Widgets
title = ctk.CTkLabel(
    window, 
    text='File System Creator', 
    text_color='white', 
    font=('Arial', 24))
title.pack(padx = 20, pady = 20)

subTitle = ctk.CTkLabel(
    window,
    text='Master Folder',
    text_color='white',
    font=('Arial', 20))
subTitle.pack(padx = 10, pady = 10)

masterFolder = ctk.CTkEntry(
    window,
    width=300,
    text_color='white',
    font=('Arial', 20))
masterFolder.pack()

subTitle2 = ctk.CTkLabel(
    window,
    text='Subfolder',
    text_color='white',
    font=('Arial', 20))
subTitle2.pack(padx = 10, pady = 10)

subFolder = ctk.CTkEntry(
    window,
    width=300,
    text_color='white',
    font=('Arial', 20))
subFolder.pack()

def update():
    # create list to store Entry widgets
    entry_list = []

    # create loop to create Entry widgets
    for i in range(int(subfolderAmount.get()) - 1):
        subFolder = ctk.CTkEntry(
            window,
            width=300,
            text_color='white',
            font=('Arial', 20))
        subFolder.pack(padx = 5, pady = 5)
        entry_list.append(entry_list)

subTitle3 = ctk.CTkLabel(
    window,
    text='How many Subfolders?',
    text_color='white',
    font=('Arial', 18))
subTitle3.pack(padx = 10, pady = 10)

subfolderAmount = ctk.CTkEntry(
    window,
    width=120,
    text_color='white',
    font=('Arial', 18))
subfolderAmount.pack()

checkboxState = tk.IntVar()

checkBox = ctk.CTkCheckBox(
     window, 
     text="Different names?", 
     variable=checkboxState, 
     command = update,
     font=('Arial', 16))
checkBox.pack(padx = 5, pady = 5)

# Output #1
def createSNFolder():
    master_folder_name = masterFolder.get()
    sub_folder_name = subFolder.get()
    os.mkdir(master_folder_name)
    
    for i in range(int(subfolderAmount.get())):
        os.mkdir(os.path.join(master_folder_name, sub_folder_name + " " +str(i+1)))

    masterFolder.delete(0, 'end')
    subFolder.delete(0, 'end')
    subfolderAmount.delete(0, 'end')

    CTkMessagebox(
        title="File System Creator", 
        icon='check', 
        message='Done!')

# Output 2
def createDFolder():
    master_folder_name = masterFolder.get()
    sub_folder_name = subFolder.get()
    os.mkdir(master_folder_name)
    
    for i in range(int(subfolderAmount.get())):
        os.mkdir(os.path.join(master_folder_name, sub_folder_name + " " +str(i+1)))

    masterFolder.delete(0, 'end')
    subFolder.delete(0, 'end')
    subfolderAmount.delete(0, 'end')

    CTkMessagebox(
        title="File System Creator", 
        icon='check', 
        message='Folders created successfully!')

# Decide Output

def runProgram():
    if checkboxState.get() == 1:
        createDFolder()
        print(checkboxState.get())
    else:
        createSNFolder()
        print(checkboxState.get())

submitButton = ctk.CTkButton(
    window,
    command = runProgram,
    text='Submit',
    text_color='white',
    font=('Arial', 20),)
submitButton.pack(padx = 10, pady = 10)

# run
window.mainloop()