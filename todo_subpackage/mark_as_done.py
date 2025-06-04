def mark_as_done(listo: list) -> None:
    usr_input = input("Enter task number to mark as done: ")
    if 0 <=  int(usr_input) - 1 < len(listo):
        listo.pop(int(usr_input) - 1)
        print("Task marked as done.")
    else:
        print("Invalid task number.")