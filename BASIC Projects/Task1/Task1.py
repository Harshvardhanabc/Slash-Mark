# Empty list of tasks
tasks = []

# display tasks
def Dis_task():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List: ")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}.{task['task']}({status})")

# Add tasks in to-do list
def Add_task(task_details):
    task = {"task": task_details,"completed":False}
    tasks.append(task)
    print(f"Task '{task_details}' added to your to-do list.")

# Mark as completed task
def mark_complete(task_num):
    try:
        tasks[task_num - 1]["completed"] = True
        print(f"Task {task_num} is mark as completed.")
    except IndexError:
        print("Invalid task number. Please try a valid number.")

# Remove task
def Remove_task(task_num):
    try:
        Remove_task = tasks.pop(task_num - 1)
        print(f"Task '{Remove_task['task']} removed from your to-do list.")
    except IndexError:
        print("Invalid task number. Please try a valid number.")

# Main program
while True:
    print("\nOptions:")
    print("1: Display To-Do List")
    print("2: Add a task")
    print("3: Mark as completed")
    print("4: Remove task")
    print("5: Quit")
    choice = input("Enter your choice = ")
    
    if choice == "1":
        Dis_task()

    elif choice == "2":
        task_details = input("Task: ")
        Add_task(task_details)

    elif choice == "3":
        task_num = int(input("Enter task number = "))
        mark_complete(task_num)

    elif choice == "4":
        task_num = int(input("Enter task number = "))
        Remove_task(task_num)

    elif choice == "5":
        break

    else:
        print("Invalid choice. Please enter a valid choice.")

