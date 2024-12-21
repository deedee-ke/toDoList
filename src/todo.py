import json
import os
import time
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init()

def add_task(task_list, task):
    """Add a task to the task list."""
    task_list.append(task)
    return f"{Fore.GREEN}Task '{task}' added.{Style.RESET_ALL}"

def remove_task(task_list, task):
    """Remove a task from the task list."""
    try:
        task_list.remove(task)
        return f"{Fore.GREEN}Task '{task}' removed.{Style.RESET_ALL}"
    except ValueError:
        return f"{Fore.RED}Task '{task}' not found in the list.{Style.RESET_ALL}"

def view_tasks(task_list):
    """View all tasks in the task list and return a formatted string."""
    if not task_list:
        return f"{Fore.YELLOW}No tasks available.{Style.RESET_ALL}"
    
    result = f"{Fore.CYAN}Your Tasks:{Style.RESET_ALL}\n"
    result += "─" * 40 + "\n"
    for index, task in enumerate(task_list, start=1):
        result += f"{Fore.BLUE}{index}.{Style.RESET_ALL} {task}\n"
    result += "─" * 40
    
    return result.strip()

def save_tasks(task_list, filename='tasks.json'):
    """Save tasks to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(task_list, file)
    print(f"{Fore.GREEN}Tasks saved to '{filename}'.{Style.RESET_ALL}")

def load_tasks(filename='tasks.json'):
    """Load tasks from a JSON file."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def show_help():
    """Display help menu with instructions."""
    help_text = f"""
{Fore.CYAN}Available Commands:{Style.RESET_ALL}
{Fore.YELLOW}─────────────────{Style.RESET_ALL}
{Fore.GREEN}add [task]   {Style.RESET_ALL} - Add a new task to the list
              Example: add Buy groceries
                
{Fore.RED}remove [task]{Style.RESET_ALL} - Remove a task from the list
              Example: remove Buy groceries
                
{Fore.BLUE}view         {Style.RESET_ALL} - Display all current tasks
                
{Fore.MAGENTA}save         {Style.RESET_ALL} - Save tasks to file
                
{Fore.RED}quit         {Style.RESET_ALL} - Save and exit program

{Fore.YELLOW}help         {Style.RESET_ALL} - Show this help menu
"""
    print(help_text)

def display_loading_animation(duration=1):
    """Display a simple loading animation."""
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    for _ in range(int(duration) * 10):  # Convert float to int
        for char in chars:
            print(f"\r{Fore.CYAN}Loading {char}{Style.RESET_ALL}", end='', flush=True)
            time.sleep(0.1)
    print("\r" + " " * 20 + "\r", end='')

def main():
    display_loading_animation()
    tasks = load_tasks()
    print(f"\n{Fore.CYAN}Welcome to the Todo List Manager!{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Type 'help' for instructions{Style.RESET_ALL}")
    
    while True:
        print(f"\n{Fore.CYAN}Options:{Style.RESET_ALL} add [task], remove [task], view, save, help, quit")
        command = input(f"{Fore.GREEN}Enter command:{Style.RESET_ALL} ").strip()

        if command.startswith("add "):
            task = command[4:].strip()
            if task:
                print(add_task(tasks, task))
                display_loading_animation(0.5)
            else:
                print(f"{Fore.RED}Please specify a task to add.{Style.RESET_ALL}")
        elif command.startswith("remove "):
            task = command[7:].strip()
            if task:
                print(remove_task(tasks, task))
                display_loading_animation(0.5)
            else:
                print(f"{Fore.RED}Please specify a task to remove.{Style.RESET_ALL}")
        elif command == "view":
            print(view_tasks(tasks))
        elif command == "save":
            display_loading_animation(0.5)
            save_tasks(tasks)
        elif command == "help":
            show_help()
        elif command == "quit":
            display_loading_animation(0.5)
            save_tasks(tasks)
            print(f"{Fore.YELLOW}Exiting program.{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Unknown command. Type 'help' for instructions.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
