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
        print(f"Task Number {counter + 1} : {i}")
        counter += 1

def mark_complete():
    counter = 0
    for i in to_do_list:
        print(f"Task Number {counter + 1} : {i}")
        counter += 1
    complete_task = int(input("Enter the number of the task completed: "))
    to_do_list[complete_task - 1]["status"] = "completed"
    print("Marked Completed!")

def delete_task():
    counter = 0
    for i in to_do_list:
        print(f"Task Number {counter + 1} : {i}")
        counter += 1
    complete_task = int(input("Enter the number of the task to be deleted: "))
    del to_do_list[complete_task - 1]
    print("Task deleted.")

def save_list():
    # with open("/Users/chaahatamesar/Desktop/to-do-list.txt", "w") as list_todo:
    #     for i in to_do_list:
    #         list_todo.write(f"{datetime_now} : {i} \n")
    with open("/Users/chaahatamesar/Desktop/to-do-list.json", "w") as file:
        json.dump(to_do_list, file)
    print("List saved")

def load_file():
    global to_do_list
    if os.path.exists("/Users/chaahatamesar/Desktop/to-do-list.json"):
        with open("/Users/chaahatamesar/Desktop/to-do-list.json", "r") as file:
            to_do_list = json.load(file)
            print(to_do_list)

def main():
    global start_process
    while start_process is True:
        clear_screen()
        choice = int(input("To-Do List App!!\n1.New Task\n2.View List\n3.Mark Complete\n4.Delete Task\n5.Save to file\n6.Load File\n7.End\nEnter the choice: "))
        if choice == 1:
            start_process = True
            new_task()
            print("Create a new task")
        elif choice == 2:
            view_tasks()
            print("View the list")
        elif choice == 3:
            mark_complete()
            print("Mark the task complete")
        elif choice == 4:
            delete_task()
            print("Delete a task")
        elif choice == 5:
            save_list()
            print("Save to and load from file")
        elif choice == 6:
            load_file()
        elif choice == 7:
            break
        else:
            print("Enter a number 1-5")

if __name__ == '__main__':
    main()
