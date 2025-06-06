"""
An application that allows users to manage a simple todo list.
"""

import argparse
from typing import Optional
from todo_subpackage.add_task import add_task
from todo_subpackage.view_task import view_task
from todo_subpackage.mark_as_done import mark_as_done

parser = argparse.ArgumentParser(description="Actions to take regarding a to-do list.")

parser.add_argument(
    "--action",
    "-a",
    choices=["add", "view", "done", "exit"],
    nargs="?",
    default="view",
    help="Specify the action to take: add a task, "
    "view tasks, mark a task as done, or exit the application (default: view).",
)

args = parser.parse_args()

# Extract the action argument and convert it to lowercase
action = args.action.lower()


def todo(initial_action: str, listo: Optional[list] = None) -> list:
    """
    A simple todo list application that allows users to add tasks,
    view tasks, mark tasks as done, and exit the application.

    Args:
        listo (list, optional): A list of tasks. Defaults to an empty list.

    Returns:
        None: The function modifies the list in place and does not return anything.
    """

    action = initial_action
    while True:
        print("=" * 50)
        if action == "add":
            add_task(listo)
        elif action == "view":
            view_task(listo)
        elif action == "done":
            mark_as_done(listo)
        elif action == "exit":
            print("Exiting.")
            print("-" * 50)
            break
        else:
            print("Invalid choice.")
            print("-" * 50)

        action = input("Enter your choice (add/view/done/exit) task: ").strip().lower()

    return listo


todo(action, [])
