"""
An application that allows users to manage a simple todo list.
"""

from typing import Optional
from todo_subpackage.add_task import add_task
from todo_subpackage.view_task import view_task
from todo_subpackage.mark_as_done import mark_as_done


def todo(listo: Optional[list] = None) -> list:
    """
    A simple todo list application that allows users to add tasks, 
    view tasks, mark tasks as done, and exit the application.

    Args:
        listo (list, optional): A list of tasks. Defaults to an empty list.

    Returns:
        None: The function modifies the list in place and does not return anything.
    """

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        print("="*50)
        x = input("Enter your choice: ")
        if x == '1':
            add_task(listo)
        elif x == '2':
            view_task(listo)
        elif x == '3':
            mark_as_done(listo)
        elif x == '4':
            print("Exiting.")
            print("-"*50)
            break
        else:
            print("Invalid choice.")
            print("-"*50)

    return listo

todo([])
