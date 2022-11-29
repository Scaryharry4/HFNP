# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os
from shutil import copyfile;

#HFNP root file
rootDirectory = "E:\.HFNP"
input_file = "NULL"
subject_folder = "NULL"
subsection_folder = "NULL"
final_directory = "NULL"
new_name = "NULL"
subjectArray = os.listdir(rootDirectory)
subsectionArray = "NULL"
subsectionDrop = "NULL"

#HFNP Functions
def checkPath(fileName):
    if os.path.exists(fileName):
        print("File successfully found.")
    else:
        print("Path of the file is Invalid. Please input a valid file path.")
        checkPath(fileName)

def makeFinalDirectory():
    global final_directory
    if input_file == "NULL":
        print("The input file went missing please try again")
    elif subject_folder != "NULL":
        final_directory = str(rootDirectory) + "\\" + str(subject_folder) + "\\"
    else:
        print("LOG: Subject folder could not be found")

def compileNewDirectory():
    makeFinalDirectory()
    new_directory = str(final_directory) + "\\" + new_nameEntry.get()
    print("LOG:" + input_file)
    os.rename(str(input_file), str(new_directory))  
    new_directory = input_file  

def makeSubjectFolder(selection):
    global subject_folder, subsectionArray
    subject_folder = selection
    subsectionArray = os.listdir(rootDirectory + "\\" + subject_folder)
    return subject_folder, subsectionArray

def makeSubsectionFolder(selection):
    global subsection_folder
    subsection_folder = selection
    return subsection_folder


# Function for opening the
# file explorer root
def takeInputFile():
    global input_file
    input_file = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+ input_file)
    return input_file

root = Tk()
root.title('HFNP')
root.geometry("1920x1080")



# Create a File Explorer label
label_file_explorer = Label(root,
							text = "File Explorer using Tkinter",
							width = 100, height = 4,
							fg = "blue")

#take input file from explorer
input_file_explorer = ttk.Button(root,text = "select file for input",command = takeInputFile)
                        
#Create drop down from root directory files
subject_folder = StringVar()
subjectDrop = ttk.OptionMenu(root, subject_folder, *subjectArray, command=makeSubjectFolder)

subsection_folder = StringVar()
subsectionDrop = ttk.OptionMenu(root, subsection_folder, *subsectionArray, command=makeSubsectionFolder)

#get new name for file
new_nameEntry = ttk.Entry(root, textvariable = new_name)
new_nameEntry.insert(END,"Rename the file")

#compile with this button
move_file = ttk.Button(root, text = "Move the file", command=compileNewDirectory)
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)

input_file_explorer.grid(column = 1, row = 2)

subjectDrop.grid(column = 1,row = 3)

subsectionDrop.grid(column = 1,row = 4)

new_nameEntry.grid(column = 1,row = 5)

move_file.grid(column = 1,row = 6)

# Let the root wait for any events
root.mainloop()
