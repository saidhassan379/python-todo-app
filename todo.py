tasks =[]
def show_menu():
    print("\n---TO DO LIST---")
    print("1. Add task")
    print("2. View taks")
    print("3. Complte task")
    print("Delte task")
    print("5. Exit")
while True:
    show_menu()
    choice = input ("Choose an option: ")
    if choice == "1":
        print ("Add task slected")
    elif choice == "2":
        print ("View tasks selected")
    elif choice == "3":
        print ("Complete task selected")
    elif choice == "4":
        print ("Delete task selected")
    elif choice == "5":
        break
    else:
        print ("Invalid choice. Please try again.")
    
    