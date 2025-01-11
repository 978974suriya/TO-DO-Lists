def display_menu():
    print("\n=== To-Do List Menu ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{i + 1}. {task['task']} [{status}]")

def add_task(tasks):
    task_name = input("\nEnter the task: ").strip()
    if task_name:
        tasks.append({"task": task_name, "completed": False})
        print(f"Task '{task_name}' added successfully!")
    else:
        print("Task name cannot be empty!")

def mark_task_complete(tasks):
    if not tasks:
        print("\nNo tasks available to mark as complete!")
        return
    try:
        task_num = int(input("Enter the task number to mark as complete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
            print(f"Task '{tasks[task_num]['task']}' marked as complete!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task(tasks):
    if not tasks:
        print("\nNo tasks available to delete!")
        return
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"Task '{removed_task['task']}' deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting... Have a productive day!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
