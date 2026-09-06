# To-Do List Application

tasks = []


def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\n------ YOUR TASKS ------")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['name']} - {status}")


def add_task():
    task_name = input("\nEnter the task: ")

    task = {
        "name": task_name,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def update_task():
    show_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("\nEnter task number to update: "))

        if 1 <= number <= len(tasks):
            new_name = input("Enter the new task: ")
            tasks[number - 1]["name"] = new_name
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def complete_task():
    show_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("\nEnter task number to mark as completed: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    show_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):
            deleted_task = tasks.pop(number - 1)
            print(f"'{deleted_task['name']}' deleted successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


while True:

    print("\n======================")
    print("      TO-DO LIST")
    print("======================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        complete_task()

    elif choice == "5":
        delete_task()

    elif choice == "6":
        print("\nThank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")