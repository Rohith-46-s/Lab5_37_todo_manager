"""Todo manager application.

Provides utilities to add, remove, load, and save tasks with safe
parsing and explicit error handling.
"""

import ast
import hashlib
import os
import sys


API_KEY = os.getenv("TODO_API_KEY", "")


def hash_password(password):
    """Hash a password using SHA-256.

    Args:
        password: The plain-text password to hash.

    Returns:
        The SHA-256 hex digest of the password.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def add_task(task_list=None, task=None):
    """Append a task to a list.

    Args:
        task_list: Optional list to append to. A new list is created when
            omitted so the default is not shared across calls.
        task: The task to add.

    Returns:
        The updated task list.
    """
    if task_list is None:
        task_list = []
    if task is None:
        return task_list
    task_list.append(task)
    return task_list


def remove_task(task_list=None, task=None):
    """Remove the first occurrence of a task from a list.

    Args:
        task_list: Optional list to remove from. Defaults to a new list.
        task: The task to remove.

    Returns:
        The updated task list.
    """
    if task_list is None:
        task_list = []
    try:
        task_list.remove(task)
    except ValueError:
        pass
    return task_list


def load_tasks(path):
    """Load tasks from a file using safe literal evaluation.

    Args:
        path: Path to the file containing a Python literal of tasks.

    Returns:
        The list of tasks, or an empty list if the file cannot be read.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
        tasks = ast.literal_eval(data)
        return tasks
    except (OSError, ValueError, SyntaxError):
        return []


def save_tasks(path, tasks):
    """Persist tasks to a file.

    Args:
        path: Destination file path.
        tasks: Tasks to write.

    Returns:
        True if the file was written successfully, False otherwise.
    """
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(str(tasks))
        return True
    except OSError:
        print("Failed to save tasks")
        return False


def parse_user_input(raw):
    """Parse user input safely when possible.

    Args:
        raw: Raw input string from the user.

    Returns:
        The parsed Python literal, or the original string when parsing
        fails.
    """
    try:
        value = ast.literal_eval(raw)
        return value
    except (ValueError, SyntaxError):
        return raw


def print_tasks(tasks):
    """Print all tasks with an index.

    Args:
        tasks: Iterable of tasks to print.
    """
    for index, task in enumerate(tasks, start=1):
        print(f"Task {index}: {task}")


def main():
    """Run the todo manager demonstration.

    Returns:
        Exit status code.
    """
    tasks = add_task(task_list=None, task="Buy milk")
    tasks = add_task(task_list=tasks, task="Call mom")
    tasks = add_task(task_list=tasks, task="Review lab")
    print_tasks(tasks)
    if API_KEY:
        print("API key configured from environment")
    return 0


if __name__ == "__main__":
    sys.exit(main())
