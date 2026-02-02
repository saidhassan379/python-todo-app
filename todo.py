import json
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except:
            tasks = []
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

tasks =[]

load_tasks()
def show_menu():
    print("\n---TO DO LIST---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Compelete task")
    print("4. Delete task")
    print("5. Exit")
while True:
    show_menu()
    choice = input ("Choose an option: ")
    if choice == "1":
        task= input("Enter task: ")
        tasks.append({"title": task, "done": False})
        save_tasks()
        print ("Task added!")

    elif choice == "2":
        if not tasks:
            print ("No tasks available.")
        else:
            for i, task in enumerate(tasks):
                status= "Done" if task["done"] else "pending" 
                print (f"{i+1}. {task['title']} - {status}")    
            
    elif choice == "3":
        number= int(input("Enter task number to complete: "))
        tasks[number-1]["done"]= True
        save_tasks()    
        print("Task Completed! ")
    elif choice == "4":
        number= int(input("Enter task number to delete: "))
        tasks.pop(number-1)
        save_tasks()
        print("Task deleted!")
    elif choice == "5":
        break
    else:
        print ("Invalid choice. Please try again.")
  
    
    