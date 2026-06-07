import os

TASK_FILE = "tasks.txt"

def load_tasks():
    ## Loads tasks from the file into a list.
    tasks = []
    try:
        if os.path.exists(TASK_FILE):
            with open(TASK_FILE, "r") as file:
                # Read each line and remove the newline character
                tasks = [line.strip() for line in file.readlines()]
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error loading tasks: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while loading: {e}")
    return tasks

def save_tasks(tasks):
    ## Saves the current list of tasks to the file.
    try:
        with open(TASK_FILE, "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except PermissionError:
        print("Error: Permission denied. Could not save tasks.")
    except Exception as e:
        print(f"An unexpected error occurred while saving: {e}")

def add_task(tasks):
    ## Adds a new task to the list and saves it. 
    new_task = input("Enter the task description: ").strip()
    if new_task:
        tasks.append(new_task)
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Task description cannot be empty.")

def view_tasks(tasks):
    ## Displays the current list of tasks.
    if not tasks:
        print("\nYour task list is empty.")
    else:
        print("\n--- YOUR CURRENT TASKS ---")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def remove_task(tasks):
    ## Removes a task by its list number.
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("\nEnter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number. Please choose a number from the list.")
    except ValueError:
        print("Error: Please enter a valid number (e.g., 1, 2, 3).")

def main():
    ## Main menu for the Task Manager.
    tasks = load_tasks()
    
    while True:
        print("\n--- Task List Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Completed Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
