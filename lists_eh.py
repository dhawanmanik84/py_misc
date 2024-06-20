#to list the content of a folder
#if we provide folder name as xyz which is unavailble - handle exception
import os

folders = input("Please provide list of folders: ").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name, looks like this folder does not exist: " + folder)
        break #to ignore the wrong folder and proceed use continue
    except PermissionError:
        break
        print("No access to this folder: " + folder)

    print("Listing files for the folder - " + folder)
    #print(files)

    for file in files:
        print(file)




