# BASIC FILE HANDLING PROJECT CRUD OPERATION

from pathlib import Path
import os


def readFileandFolder():
    path = Path('.')
    items = list(path.rglob('*'))

    if not items:
        print("No files or folders found.")
        return

    for i, item in enumerate(items):
        print(f"{i + 1} : {item}")


def readFile():
    try:
        readFileandFolder()

        name = input("Which file do you want to read :- ")
        p = Path(name)

        if p.exists() and p.is_file():

            with p.open('r') as fs:
                data = fs.read()
                print("\nFile Content:\n")
                print(data)

            print("\nREAD Successfully")

        else:
            print("File does not exist")

    except Exception as err:
        print(f"An error occurred: {err}")


def createFile():
    try:
        readFileandFolder()

        name = input("Please tell your file name :- ")
        p = Path(name)

        if not p.exists():

            with p.open("w") as fs:
                data = input("What do you want to write in this file :- ")
                fs.write(data)

            print("File created successfully")

        else:
            print("This file already exists")

    except Exception as err:
        print(f"An error occurred: {err}")


def updateFile():
    try:
        readFileandFolder()

        name = input("Tell which file you want to update :- ")
        p = Path(name)

        if p.exists() and p.is_file():

            print("\nPress 1 for Changing the Name")
            print("Press 2 for OverWriting the Data")
            print("Press 3 for Appending some content\n")

            res = int(input("Tell your response :- "))

            if res == 1:

                name2 = input("Tell your new file name :- ")
                p2 = Path(name2)

                p.rename(p2)

                print("File renamed successfully")

            elif res == 2:

                with p.open('w') as fs:
                    data = input("Tell what you want to write (This will overwrite old data) :- ")
                    fs.write(data)

                print("File overwritten successfully")

            elif res == 3:

                with p.open('a') as fs:
                    data = input("Tell what you want to append :- ")
                    fs.write(data)

                print("Data appended successfully")

            else:
                print("Invalid Choice")

        else:
            print("File does not exist")

    except Exception as err:
        print(f"An error occurred: {err}")


def deleteFile():
    try:
        readFileandFolder()

        name = input("Which file do you want to delete :- ")
        p = Path(name)

        if p.exists() and p.is_file():

            os.remove(p)

            print("File removed successfully")

        else:
            print("No such file exists")

    except Exception as err:
        print(f"An error occurred: {err}")


# MAIN MENU

print("\n===== FILE HANDLING CRUD PROJECT =====\n")

print("Press 1 for Creating a file")
print("Press 2 for Reading a file")
print("Press 3 for Updating a file")
print("Press 4 for Deleting a file\n")

check = int(input("Please tell your response :- "))

if check == 1:
    createFile()

elif check == 2:
    readFile()

elif check == 3:
    updateFile()

elif check == 4:
    deleteFile()

else:
    print("Invalid Input")