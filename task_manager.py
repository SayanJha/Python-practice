def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def task():
    tasks = []
    print("-----Welcome to the task management system-----")
    total_tasks = int(input("How many tasks do you want to add? "))

    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter your task {i}: ").title()
        tasks.append(task_name)

    print("Today's tasks are:")
    display_tasks(tasks)

    while True: # No need for an inner while loop (like in basic_calculator.py) 
        try:    # here because we are not using any print function for displaying operations
            operation = int(input("\nEnter:\n1- Add\n2- Update\n3- Delete\n4- View\n5- Exit\n> "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if operation == 1:
            add = input("Enter the task you want to add: ").title()
            tasks.append(add)
            print(f"Task \"{add}\" has been added successfully...")
            display_tasks(tasks)

        elif operation == 2:
            display_tasks(tasks)
            updated_task = input("Enter the task you want to update: ").title()
            if updated_task in tasks:
                new_task = input("Enter new task: ").title()
                index = tasks.index(updated_task)
                tasks[index] = new_task
                print(f"\"{updated_task}\" has been changed to \"{new_task}\" successfully...")
                display_tasks(tasks)
            else:
                print("Task not found.")

        elif operation == 3:
            display_tasks(tasks)
            deleted_task = input("Which task do you want to delete? ").title()
            if deleted_task in tasks:
                tasks.remove(deleted_task)
                print(f"Task \"{deleted_task}\" has been deleted successfully...")
                display_tasks(tasks)
            else:
                print("Task not found.")

        elif operation == 4:
            print(f"There are {len(tasks)} tasks.")
            display_tasks(tasks)

        elif operation == 5:
            print("Goodbye...")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":  # Only run the main function if this file is
    task()                  # executed directly
