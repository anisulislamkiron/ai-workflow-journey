# ============================================================
# TO-DO LIST CLI
# ============================================================

tasks = []  # This list stores all your tasks

# ------------------------------------------------------------
def add_task():
    task = input("Enter task: ")
    tasks.append({"name": task, "done": False})
    print(f"✅ '{task}' added!\n")

# ------------------------------------------------------------
def view_tasks():
    print("\nYour To-Do List:")
    if len(tasks) == 0:
        print("  No tasks yet!\n")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else " "
            print(f"  {i}. [{status}] {task['name']}")
    print()

# ------------------------------------------------------------
def mark_done():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        num = int(input("Enter task number to mark done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print(f"✅ '{tasks[num - 1]['name']}' marked as done!\n")
        else:
            print("❌ Invalid number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

# ------------------------------------------------------------
def show_menu():
    print("===== To-Do List =====")
    print("1. Add item")
    print("2. View list")
    print("3. Mark done")
    print("4. Exit")

# ------------------------------------------------------------
# MAIN LOOP
while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        print("Goodbye! 👋")
        break
    else:
        print("❌ Invalid option. Try again.\n")