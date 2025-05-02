import os
from datetime import datetime
from getpass import getpass


path = "/Users/chaahatamesar/Desktop/savenotesapp.txt"

def clear_screen():
    #os.system('cls' if os.name == 'nt' else 'clear')
    # ======================
    # if os.name == 'nt':
    #     os.system('cls')  # For Windows
    # else:
    #     os.environ['TERM'] = 'xterm'  # Set TERM to 'xterm' for other platforms like macOS and Linux
    #     os.system('clear')
    #======================
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            if "TERM" in os.environ:
                os.system('clear')
    except:
        pass  # If it fails, just skip clearing

def save_note(path):
    now = datetime.now()
    timestamp_now = now.strftime("%y-%m-%d %H:%M:%S")
    with open(path, "w") as createnote:
            createnote.write(f"Notes Saved on: {timestamp_now}")
    print("Note is saved!")

def append_note(path):
    now = datetime.now()
    timestamp_now = now.strftime("%y-%m-%d %H:%M:%S")
    data = input("Enter data to append: ")
    with open(path, "a") as appendnote:
        appendnote.write("\n"+ f"[{timestamp_now}] : {data} ")
        appendnote.write("\n" + "-" * 30 + "\n")
    print(f"Note is Appended")

def view_note(path):
    with open (path, "r") as readnote:
        print(readnote.read())
        # for i in readnote:
        #     print(i.strip())
    print("Viewed Note")

def search_note(path):
    word_search = input("Enter word to search: ")
    search_list = []
    word_found = []
    with open (path, "r") as searchnote :
        for i in searchnote.readlines():
            search_list.append(i.strip())
        for i, line in enumerate(search_list, start=1):
            if word_search.lower() in line.lower():
                word_found.append(f"Line {i}: {line.strip()}")
        if word_found:
            print("Found Lines: ")
            for line in word_found:
                print(f"{line}")
        else:
            print("Word not found!")

true_password = "chaahat"
start_okay = False
for i in range(3):
    # to hide the password written
    #user_password = getpass("Enter the password for the Notes App: ")
    user_password = input("Enter the password for the Notes App: ")

    if user_password == true_password:
        start_okay =  True
        break



if start_okay == True:
    while True:
        clear_screen()
        print("Select the operation: \n"
               "1. Save new note \n"
               "2. Append note \n"
               "3. View note \n"
               "4. Search notes \n"
               "5. Exit \n")
        choice = input("Please enter number between 1-5::")
        if not choice.isdigit():
            print("Please enter a number (1-4).")
            continue

        choice = int(choice)

        if choice == 1:
            save_note(path)
        elif choice == 2:
            append_note(path)
        elif choice == 3:
            view_note(path)
        elif choice == 4:
            search_note(path)
        elif choice == 5:
            break
        else:
            print("Invalid Choice!")
else:
    print("Access Denied")

