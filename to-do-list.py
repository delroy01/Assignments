import os

# Configuration
FILE_NAME = "tasks.txt"

def load_tasks():
    """Loads tasks from a file when the program starts."""
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 2:
                    tasks.append({
                        "name": parts[0],
                        "completed": parts[1] == "Done"
                    })
    return tasks

def save_tasks(tasks):
    """Saves the current task list to a file."""
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            status = "Done" if task["completed"] else "Pending"
            file.write(f"{task['name']} | {status}\n")

def display_tasks(tasks):
    """Displays all tasks to the user."""
    if not tasks:
        print("\n--- Your list is empty ---")
    else:
        print("\n--- Current Tasks ---")
        for i, task in enumerate(tasks, 1):
            status = "[X]" if task["completed"] else "[ ]"
            print(f"{i}. {status} {task['name']}")

def get_valid_index(tasks, prompt):
    """Safely get a valid task index from the user."""
    try:
        index = int(input(prompt)) - 1
        if 0 <= index < len(tasks):
            return index
        else:
            print("Invalid task number.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task Completed")
        print("5. Save and Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()

        if choice == '1':
            name = input("Enter the task: ").strip()
            if name:
                tasks.append({"name": name, "completed": False})
                print("Task added!")
            else:
                print("Task cannot be empty.")

        elif choice == '2':
            display_tasks(tasks)

        elif choice == '3':
            display_tasks(tasks)
            if tasks:
                index = get_valid_index(tasks, "Enter task number to delete: ")
                if index is not None:
                    removed = tasks.pop(index)
                    print(f"Deleted: {removed['name']}")

        elif choice == '4':
            display_tasks(tasks)
            if tasks:
                index = get_valid_index(tasks, "Enter task number to mark complete: ")
                if index is not None:
                    tasks[index]["completed"] = True
                    print(f"Task '{tasks[index]['name']}' marked as done!")

        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
