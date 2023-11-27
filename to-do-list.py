import pickle
import os
import tkinter as tk
from tkinter import messagebox


def display_tasks(tasks):
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")


def add_task(tasks, task_description):
    tasks.append(task_description)
    print("Task added successfully!")


def remove_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Removed task: {removed_task}")
    else:
        print("Invalid task index.")


def main():
    filename = "todo_list.pkl"

    if os.path.exists(filename):
        with open(filename, "rb") as file:
            tasks = pickle.load(file)
    else:
        tasks = []

    while True:
        print("\nMenu:")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Open GUI To-Do List")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_tasks(tasks)
        elif choice == 2:
            task_description = input("Enter task description: ")
            add_task(tasks, task_description)
        elif choice == 3:
            display_tasks(tasks)
            task_index = int(input("Enter the task number to remove: "))
            remove_task(tasks, task_index)
        elif choice == 4:

            open_gui_to_do_list(tasks)
        elif choice == 5:

            with open(filename, "wb") as file:
                pickle.dump(tasks, file)
            break
        else:
            print("Invalid choice. Please try again.")


def open_gui_to_do_list(tasks):
    def add_task():
        task = entry_task.get()
        if task:
            listbox_tasks.insert(tk.END, task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task():
        selected_task = listbox_tasks.curselection()
        if selected_task:
            listbox_tasks.delete(selected_task)
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    root = tk.Tk()
    root.title("To-Do List")

    listbox_tasks = tk.Listbox(root)
    listbox_tasks.pack()

    entry_task = tk.Entry(root)
    entry_task.pack()

    button_add_task = tk.Button(root, text="Add Task", command=add_task)
    button_add_task.pack()

    button_remove_task = tk.Button(root, text="Remove Task", command=remove_task)
    button_remove_task.pack()

    for task in tasks:
        listbox_tasks.insert(tk.END, task)

    root.mainloop()


if __name__ == "__main__":
    main()