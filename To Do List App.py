# 📝 Task: Build a CLI To-Do List App
# Features to implement:
# Add a task
# Input: task name, priority (high, medium, low), due date (YYYY-MM-DD)
# Store in a list of dictionaries
# View all tasks
# Show sorted by priority, then due date
# Mark task as complete
# Delete a task
# Save to and load from file
import os
import datetime
import json
import colorama
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True) #means colors reset after each print, so you don’t have to manually reset them.

to_do_list = [{"task": "Learn German", "priority": "high", "due_date": "2025-05-20", "status": "pending"}
            , {"task": "udemy", "priority": "low", "due_date": "2025-05-26", "status": "pending"}
            , {"task": "Python", "priority": "medium", "due_date": "2025-05-29", "status": "pending"}
            , {"task": "data science", "priority": "high", "due_date": "2025-05-18", "status": "pending"}
              ]

start_process = True
datetime_now = datetime.date.today()

def clear_screen():
    try:
        if os.name == 'nt':
            os.system('clear')
        else:
            if 'TERM' in os.environ:
                os.system('clear')
    except:
        pass

def new_task():
    task_name = input("Enter task name: ")
    priority = input("Enter Priority (high/ medium / low)")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    to_do_list.append({"task": task_name, "priority": priority, "due_date": due_date, "status": "pending"})

def view_tasks():
    priority_order = {"high" : 1, "medium" : 2, "low" : 3}
    sorted_list = sorted(to_do_list, key=lambda x: (priority_order.get(x["priority"], 4), x["due_date"]))
    counter = 0
    for i in sorted_list:
        print(f"Task Number {counter + 1} : {Style.BRIGHT + str(i)}")
        counter += 1

def mark_complete():
    counter = 0
    for i in to_do_list:
        print(f"Task Number {counter + 1} : {i}")
        counter += 1
    complete_task = int(input("Enter the number of the task completed: "))
    to_do_list[complete_task - 1]["status"] = "completed"
    print(Fore.GREEN + "Marked Completed!")

def delete_task():
    counter = 0
    for i in to_do_list:
        print(f"Task Number {counter + 1} : {i}")
        counter += 1
    complete_task = int(input("Enter the number of the task to be deleted: "))
    del to_do_list[complete_task - 1]
    print(Fore.GREEN +"Task deleted.")

def save_list():
    # with open("/Users/chaahatamesar/Desktop/to-do-list.txt", "w") as list_todo:
    #     for i in to_do_list:
    #         list_todo.write(f"{datetime_now} : {i} \n")
    with open("/Users/chaahatamesar/Desktop/to-do-list.json", "w") as file:
        json.dump(to_do_list, file)
    print(Fore.GREEN +"List saved")

def load_file():
    if os.path.exists("/Users/chaahatamesar/Desktop/to-do-list.json"):
        with open("/Users/chaahatamesar/Desktop/to-do-list.json", "r") as file:
            to_do_list = json.load(file)
            print(to_do_list)
def edit_task():
    for i, line in enumerate(to_do_list, start= 1):
        print(f"{i} : Task - {line.get('task')}, priority - {line.get('priority')}, due_date - {line.get('due_date')}, status - {line.get('status')}")
    edit_whichtask = int(input("Enter the number of the task you want to edit: "))
    try:
        if edit_whichtask <= len(to_do_list) + 1:
            edit_main = to_do_list[edit_whichtask - 1]
            task_edit = input("Enter the change of the task: ")
            priority_edit = input("Enter the priority of the task high/medium/low :")
            duedate_edit = input("Enter the Due Date of the task(YYYY-MM-DD): ")
            if task_edit != edit_main.get("task"):
                edit_main["task"] = task_edit
            if priority_edit != edit_main.get("priority"):
                edit_main["priority"] = priority_edit
            if duedate_edit != edit_main.get("due_date"):
                edit_main["due_date"] = duedate_edit
            print(Fore.GREEN +"Task updated successfully!")
        else:
            print(Fore.RED + "Invalid Task number")
    except ValueError:
        print(Fore.RED + "Please enter a valid number.")


def main():
    global start_process
    while start_process is True:
        clear_screen()
        choice = int(input("To-Do List App!!\n1.New Task\n2.View List\n3.Mark Complete"
                           "\n4.Delete Task\n5.Save to file\n6.Load File\n7.Edit Task\n8.End\nEnter the choice: "))
        if choice == 1:
            new_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            mark_complete()
        elif choice == 4:
            delete_task()
        elif choice == 5:
            save_list()
        elif choice == 6:
            load_file()
        elif choice == 7:
            edit_task()
        elif choice == 8:
            break
        else:
            print(Fore.RED + "Enter a number 1-5")

if __name__ == '__main__':
    main()
