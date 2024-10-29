import json
import os

def add_task(task_list, task):
    """Add a task to the task list."""
    task_list.append(task)
    return f"Task '{task}' added."

def remove_task(task_list, task):
    """Remove a task from the task list."""
    try:
        task_list.remove(task)
        return f"Task '{task}' removed."
    except ValueError:
        return f"Task '{task}' not found in the list."

def view_tasks(task_list):
    """View all tasks in the task list and return a formatted string."""
    if not task_list:
        return "No tasks available."
    
    result = ""
    for index, task in enumerate(task_list, start=1):
        result += f"{index}. {task}\n"
    
    return result.strip()  # Return the formatted string

def save_tasks(task_list, filename='tasks.json'):
    """Save tasks to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(task_list, file)
    print(f"Tasks saved to '{filename}'.")

def load_tasks(filename='tasks.json'):
    """Load tasks from a JSON file."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []  # Return an empty list if the file does not exist

def main():
    tasks = load_tasks()  # Load tasks when the program starts
    while True:
        print("\nOptions: add [task], remove [task], view, save, quit")
        command = input("Enter command: ").strip()

        if command.startswith("add "):  # Space after 'add' ensures task is specified
            task = command[4:].strip()
            if task:  # Checking if a task was actually provided
                print(add_task(tasks, task))
            else:
                print("Please specify a task to add.")
        elif command.startswith("remove "):
            task = command[7:].strip()
            if task:  # Checking if a task was actually provided
                print(remove_task(tasks, task))
            else:
                print("Please specify a task to remove.")
        elif command == "view":
            print(view_tasks(tasks))
        elif command == "save":
            save_tasks(tasks)
        elif command == "quit":
            save_tasks(tasks)  # Save tasks on exit
            print("Exiting program.")
            break
        else:
            print("Unknown command. Please use 'add [task]', 'remove [task]', 'view', 'save', or 'quit'.")

if __name__ == "__main__":
    main()
