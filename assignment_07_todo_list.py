# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#
# =============================================================================


def print_menu():
    print("\n============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print(f'Task added: "{task}"')


def view_tasks(tasks):
    if not tasks:
        print("Your task list is empty.")
        return

    print("Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def delete_task(tasks):
    if not tasks:
        print("Your task list is empty. Nothing to delete.")
        return

    view_tasks(tasks)
    num = int(input("Enter task number to delete: "))

    if num < 1 or num > len(tasks):
        print("Error: Invalid task number.")
        return

    removed = tasks.pop(num - 1)
    print(f'Task "{removed}" has been removed.')


def main():
    tasks = []
    running = True

    while running:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            running = False
        else:
            print("Error: Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()
