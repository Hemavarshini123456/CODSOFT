#To-Do list program
tasks=[];
def show_menu():
    print("\n---To-Do List Menu---")
    print("1.View tasks")
    print("2.Add task")
    print("3.Remove task")
    print("4.Exit")
while True:
    show_menu()
    choice=input("Enter your choice(1-4):")
    if choice=="1":
        if len(tasks)==0:
            print("No tasks found")
        else:
            print("\nYour tasks:")
            for i,task in enumerate(tasks,start=1):
                print(f"{i}.{task}")
    elif choice=="2":
        task=input("Enter a new task:")
        tasks.append(task)
        print(f"Task ' {task}' added successfully!")
    elif choice=="3":
        if len(tasks)==0:
            print("No tasks to remove")
        else:
            for i,task in enumerate(tasks,start=1):
                print(f"{i}.{task}")
            try:
                task_num=int(input("Enter task number to remove:"))
                removed=tasks.pop(task_num-1)
                print(f"Task '{removed}' removed successfully!")
            except (ValueError,IndexError):
                print("Invalid task number")
    elif choice=="4":
        print("Exiting...Goodbye!")
        break
    else:
        print("Invalid choice.Please try again")
             
