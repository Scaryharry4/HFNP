# Harrys File Name Protocol                                                    -
# This is a file organization and naming protocol built for ease of use.       -
# The system is ment to be easily understandable, readable yet concise.        -
# Protocol originally developed by and for primary use by Harrison Velentzas   -
# Contact: harrison.velentzas@gmail.com                                        -
#-------------------------------------------------------------------------------

#Import required libraries
import os;
from shutil import copyfile

#define variables -------------------
#HFNP root file
rootDirectory = "E:\.HFNP"
input_file = "NULL"
subject_folder = "NULL"
subsection_folder = "NULL"

#function to confirm file existence. will ask again if no file is found
def checkPath(fileName):
    if os.path.exists(fileName):
        print("File successfully found.")
    else:
        print("Path of the file is Invalid. Please input a valid file path.")
        checkPath(fileName)

def newSubject():
    new_subject = str(input("If you would like to create a subject labeled '" + subject_folder + "', then please confirm its name "))
    if new_subject == subject_folder:
        os.mkdir(rootDirectory + "\\" + new_subject + "\\")
    else:
        print("Names do not match please attempt again and check your spelling")
        newSubject()

def newSubsection():
    new_subsection = str(input("If you would like to create a subsection labeled '" + subsection_folder + "', then please confirm its name "))
    if new_subsection == subsection_folder:
        os.mkdir(rootDirectory + "\\" + subject_folder + "\\" + new_subsection + "\\")
    else:
        print("Names do not match please attempt again and check your spelling")
        newSubsection()

input_file = str(input("what is the file path of the file you are inputing to the protocol? "))
checkPath(input_file)

subject_folder = str(input("What subject folder are you entering? "))
subjectList = os.listdir(rootDirectory)


if subject_folder in subjectList:
    print("Subject folder found")
else:
    print("Subject folder '" + subject_folder + "' not found")
    newSubject()

subsection_folder = str(input("What subsection folder are you entering? "))
subsectionList = os.listdir(rootDirectory + "\\" + subject_folder + "\\")

if subsection_folder in subsectionList:
    print("Subsection folder found")
else:
    print("Subsection folder '" + subsection_folder + "' not found")
    newSubsection()

new_name = str(input("What do you want to rename the file? Be sure to include the file extension in the name "))

if input_file == "NULL":
    print("The input file went missing please try again")
elif subject_folder != "NULL":
    final_directory = rootDirectory + "\\" + subject_folder + "\\"
else:
    print("LOG: Subject folder could not be found")

if subsection_folder != "NULL":
    final_directory = rootDirectory + "\\" + subject_folder + "\\" + subsection_folder
else:
    print("LOG: Subsection folder could not be found")

#this is the final step that compiles the new directory name moves the file and renames it
new_directory = final_directory + "\\" + new_name
os.rename(input_file, new_directory)

if os.path.exists(new_directory):
    print("File transfered successfully")
else:
    print("File transfer failed")