my_task = []
while True:
    print("\n  Task Manager   ")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")
    option = input("Choose an option: ")
    if option == '1':
        task = input("Enter the task: ")
        my_task.append(task)
        print("Task saved successfully! ")
    elif option == "2":
        if len(my_task) == 0:
            print("No tasks added yet.")
        else:
            print("\nYour Tasks: ")
            number = 1
            for task in my_task:
                print(str(number) + "." + task)
                number += 1

    elif option == "3":
            print("Program closed.")
            break
    else:
        print("Please enter a valid option.")

            






