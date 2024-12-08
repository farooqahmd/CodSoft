tasks = []
def create_task():
    task = input("Enter a new task : ")
    tasks.append(task)
    print("Task created successfully")

def update_task():
    if not tasks:
        print("There are currently no tasks to update !!")
        return

    track_tasks()
    try:
        task_number = int(input("Enter the task number to update: ")) -1
        if 0 <= task_number <len(tasks):
            new_task =input("Enter the new task description: ")
            tasks[task_number] = new_task
            print("Task updated successfully")
        else:
            print("Invalid task number: ")
    except ValueError:
        print("Please enter a valid number: ")

def track_tasks():
    if not tasks:
        print("No tasks available")
        return
    else:
        print("---To-Do List: ")
        for i, task in enumerate(tasks,start=1):
             print(f"{i}. {task} ")


def main():
    print("-----To-Do Console Application-----")
    while True:
        print("\n1.Create\n2.Update\n3.Track\n4.Exit")
        choice =int(input("Choose the operation: "))

        if choice ==  1:
            create_task()
        elif choice == 2:
            update_task()
        elif choice ==3:
            track_tasks()
        elif choice ==4:
            "Exiting the program."
            break
        else:
            print("Invalid choice. Try Again")

if __name__ =="__main__":
    main()