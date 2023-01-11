"""
Task Manager Using Python OOP

a. Task class will have 6 fields.
     1. task: The name of task (string)
     2. created_time: The date and time when task was created (datetime)
     3. updated_time: The date and time when task was updated (datetime)
     4. completed_time: The date and time when task was completed (datetime)
     5. task_done: Define if the task is completed (boolean)
     6. id: Unique id to define the task (uuid)

b. Task class will have two methods:
     1. update_task(): It will take the task object and new task name and update the task name and add updated_time.
     2. complete_task(): It will take the task object and mark the task as completed and add completed_time.

"""

import uuid
from datetime import datetime


class Task:
    def __init__(self, task_name: str):
        self.task = task_name
        self.created_time = datetime.now()
        self.updated_time = None
        self.completed_time = None
        self.task_done = False
        self.id = uuid.uuid4()

    def update_task(self, new_task_name: str):
        self.task = new_task_name
        self.updated_time = datetime.now()

    def complete_task(self):
        self.task_done = True
        self.completed_time = datetime.now()


def add_new_task():
    task_name = input("Enter task name: ")
    new_task = Task(task_name)
    print("\n\nTask created successfully!\n")
    return new_task


def show_all_tasks(tasks):
    print("\nAll Tasks:")
    for task in tasks:
        print(f"\nID: {task.id}")
        print(f"Task: {task.task}")
        print(f"Created Time: {task.created_time}")
        print(f"Updated Time: {task.updated_time}")
        print(f"Completed: {task.task_done}")
        print(f"Completed Time: {task.completed_time}")
        print()


def show_incomplete_tasks(tasks):
    incomplete_tasks = [task for task in tasks if not task.task_done]
    if incomplete_tasks:
        print("\nIncomplete Tasks:")
        for task in incomplete_tasks:
            print(f"\nID: {task.id}")
            print(f"Task: {task.task}")
            print(f"Created Time: {task.created_time}")
            print(f"Updated Time: {task.updated_time}")
            print(f"Completed: {task.task_done}")
            print(f"Completed Time: {task.completed_time}")
            print()
    else:
        print("\nNo incomplete task\n")


def show_completed_tasks(tasks):
    completed_tasks = [task for task in tasks if task.task_done]
    if completed_tasks:
        print("\nCompleted Tasks:")
        for task in completed_tasks:
            print(f"\nID: {task.id}")
            print(f"Task: {task.task}")
            print(f"Created Time: {task.created_time}")
            print(f"Updated Time: {task.updated_time}")
            print(f"Completed: {task.task_done}")
            print(f"Completed Time: {task.completed_time}")
            print()
    else:
        print("\n\nNo task completed\n")


def update_task(tasks):
    incomplete_tasks = [task for task in tasks if not task.task_done]
    if incomplete_tasks:
        print("\nAll Tasks:\n")
        for i, task in enumerate(incomplete_tasks):
            print(f"{i + 1}. {task.task} (ID: {task.id})")
        task_number = int(input("\nEnter task number: "))
        if task_number > 0 and task_number <= len(incomplete_tasks):
            task_name = input("\nEnter new task name: ")
            incomplete_tasks[task_number - 1].update_task(task_name)
            print("\nTask updated successfully!\n")
        else:
            print("\nInvalid task number!\n")
    else:
        print("\nNo incomplete task\n")


def mark_task_as_completed(tasks):
    incomplete_tasks = [task for task in tasks if not task.task_done]
    if incomplete_tasks:
        print("\nSelect which task to complete:\n")
        for i, task in enumerate(incomplete_tasks):
            print(f"{i + 1}. {task.task} (ID: {task.id})")
            print(f"Created Time: {task.created_time}")
            print(f"Updated Time: {task.updated_time}")
            print(f"Completed: {task.task_done}")
            print(f"Completed Time: {task.completed_time}")
            print()
        task_number = int(input("Enter task number: "))
        if task_number > 0 and task_number <= len(incomplete_tasks):
            incomplete_tasks[task_number - 1].complete_task()
            print("\nTask marked as completed successfully!\n")
        else:
            print("Invalid task number!")
    else:
        print("\nNo task to complete\n")


tasks = []
while True:
    print("1. Add New Task")
    print("2. Show All Tasks")
    print("3. Show Incomplete Tasks")
    print("4. Show Completed Tasks")
    print("5. Update Task")
    print("6. Mark Task as Completed")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        tasks.append(add_new_task())
    elif choice == 2:
        show_all_tasks(tasks)
    elif choice == 3:
        show_incomplete_tasks(tasks)
    elif choice == 4:
        show_completed_tasks(tasks)
    elif choice == 5:
        update_task(tasks)
    elif choice == 6:
        mark_task_as_completed(tasks)
    elif choice == 7:
        break
    else:
        print("Invalid choice!")
