# Simple to-do list (Level 1)

tasks = []

def show_menu():
    print("""
To-Do List Menu:
1. Add a task
2. View tasks
3. Quit
""")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def show_task(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print(f"You have {len(tasks)} task to do.")
        for i, task in enumerate(tasks, 1):
            print("{}. {}".format(i, task.title()))

def main():
    while True:
        show_menu()
        choice = str(input("Choose an option (1 - 3): "))

        if choice == "1":
            add_task(tasks = tasks) # Keyword Argument
        elif choice == "2":
            show_task(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

