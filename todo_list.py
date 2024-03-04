
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for items in file:
                task.append(items)
    except FileNotFoundError:
        pass

task = []

def save_tasks():
    with open("tasks.txt", "w") as file:
        for element in task:
            file.write("%s\n" %element)
            print("Task saved")

load_tasks()

def add_task():
    item = input("Enter task: ")
    task.append(item)
    save_tasks()
    print("Task added")

def remove_task():
    delete = input("Enter task to be removed: ")
    if delete in task:
        task.remove(delete)
        save_tasks()
        print("Task removed")
    else:
        print("Task is not here")

def view_task():
    if task:
        print("Tasks:")
        for to_do in task:
            print(to_do)
    else:
        print("None")


while True:
    option = input("To-Do List Application \n1.Add Task \n2.Delete Task \n3.View Task\n4.Exit\n Enter your choice: ")

    if option == '1':
        add_task()
    elif option == '2':
        remove_task()
    elif option == '3':
        view_tasks()
    elif option == '4':
        break
    else:
        print("Please put a choice")

#Note: To view tasks in terminal theres a need to exit the programme and stop the loop