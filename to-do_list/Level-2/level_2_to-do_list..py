# To-Do List (Level 2)

tasks = []


# tasks = [
#     {"task": "Study", "done": False}, (Element = 1) index = 0 of the list tasks
#     {"task": "Practice Python", "done": True},
#     {"task": "Sleep", "done": False}
# ]



def show_updated_task(tasks):
    print("Updated Task List: ")
    view_task(tasks)

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. Update task")
    print("3. Delete task")
    print("4. View tasks")
    print("5. Mark a task as completed")
    print("6. Quit")

def add_task(tasks):
    task = input("Enter the task: ").title()
    tasks.append({"task" : task, "done" : False})
    print("Task added!")
    show_updated_task(tasks)

def update_task(tasks):
    view_task(tasks)
    try:
        num = int(input("Enter the task number you want to update: "))
        if 1 <= num <= len(tasks):
            update_task = input("Please enter the new task: ").title()
            task_item = tasks[num - 1]
            previous_task = task_item["task"]
            task_item["task"] = update_task
            print(f"\"{previous_task}\" has been changed to \"{update_task}\"")
            show_updated_task(tasks)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    
def delete_task(tasks):
    view_task(tasks)
    try:
        num = int(input("\nEnter your task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1) # User input = 2, index = 2 - 1 = 1 = num
            print(f"Deleted task: {removed["task"]}")
            show_updated_task(tasks)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def view_task(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\n----- Your tasks -----")
        for i, task in enumerate(tasks, 1):
            status = "\u2713" if task["done"] else "\u2717" # UNICODES for tick and cross
            print(f"{i}. [{status}] {task["task"]}")

def mark_completed(tasks):
    view_task(tasks)
    try:
        num = int(input("Enter the task number to mark as completed: "))
        if 1 <= num <= len(tasks):
            task_item = tasks[num - 1]
            task_item["done"] = True
            print(f"Task '{task_item['task']}' marked as completed.")
            show_updated_task(tasks)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        while True:
            try:
                choice = int(input("Enter operation (1/2/3/4/5/6): "))
                if 1<= choice <= 6: # We could use = if choice in tuple(x for x  in range(1, 7)):
                    break
                else:
                    print("Invalid operation. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            update_task(tasks)
        elif choice == 3:
            delete_task(tasks)
        elif choice == 4:
            view_task(tasks)
        elif choice == 5:
            mark_completed(tasks)
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

