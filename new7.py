import json

def add_todos(todos):
    task = input("What you Want To Do: ")
    
    new_task = { 
        "task": task,
        "completed": False
    }
    todos.append(new_task)
    save_todos(todos)
    print(f"✅ New task: {task} added")

def view_todos(todos):
    if not todos:
        print("📝 No Todos Currently!")
        return
    
    print("\n=== YOUR TASKS ===")
    for i, todo in enumerate(todos, 1):
        status = "✓" if todo['completed'] else "○"
        print(f"{status} {i}. {todo['task']}")
    print("=" * 20)

def save_todos(todos):
    with open("todos.json", "w") as file:
        json.dump(todos, file, indent=4)

def load_todos():
    try:
        with open("todos.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def del_todos(todos):
    if not todos:
        print("📝 No tasks to delete!")
        return
    
    try:
        view_todos(todos)
        choice = input("Enter task number to delete: ")
        index = int(choice) - 1  # Convert to int and adjust for 0-indexing
        
        if 0 <= index < len(todos):  # Check if valid index
            deleted_task = todos.pop(index)
            save_todos(todos)
            print(f"🗑️ Deleted: {deleted_task['task']}")
        else:
            print("❌ Invalid task number!")
            
    except ValueError:
        print("❌ Please enter a valid number!")
def mark_complete(todos):
    view_todos(todos)
    choice = input("Enter the task number You want to Mark as compete: ")
    index = int(choice) - 1

    todos[index]['completed'] = True
    save_todos(todos)
    print("✅ Task marked complete!")

def main():
    todos = load_todos()
    
    while True:
        print("\n=== TODO LIST ===")
        print("1. Add A task")
        print("2. View All Tasks")
        print("3. Delete A task")
        print("4. Mark The task As completed")
        print("5. Exit")
        choice = input("\nEnter Your Choice: ")
        
        if choice == "1":
            add_todos(todos)
        elif choice == "2":
            view_todos(todos)
        elif choice == "3":
            del_todos(todos)
        elif choice == "4":
            mark_complete(todos)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()