def todo(listo: list):

    def add_task():
        tsk = input("Enter task: ")
        listo.append(tsk)
        print("-"*50)

    def view_task():
        print("Tasks:")
        for i, t in enumerate(listo):
            print(f"{i+1}. {t}")
            print("-"*50)

    def mark_as_done():
        usr_input = input("Enter task number to mark as done: ")
        if 0 <=  int(usr_input) - 1 < len(listo): 
            listo.pop(int(usr_input) - 1)
            print("Task marked as done.")
        else:
            print("Invalid task number.")

    def exit():
        print("Exiting.")
        print("-"*50)

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        print("="*50)
        x = input("Enter your choice: ")
        if x == '1':
            add_task()
        elif x == '2':
            view_task()
        elif x == '3':
            mark_as_done()
        elif x == '4':
            exit()
            break
        else:
            print("Invalid choice.")
            print("-"*50)

    return listo