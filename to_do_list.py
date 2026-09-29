from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

window = Tk()
window.title("To-Do List")
window.geometry("800x650")
window.config(bg="#d9f7be")

count = 0
def add_item():
    global count

    item = new_item.get().strip()

    if not item:
        messagebox.showerror("Empty Task", "Please enter a task.")
        return

    count += 1

    scrolled_text.insert(
        END,
        f"{count}. {item}\n"
    )

    new_item.set("")
    new_task.focus()


def delete_item():
    global count

    if count == 0:
        messagebox.showerror("Error", "There are no tasks to delete.")
        return

    try:
        task_number = int(delete_task.get())
    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid task number."
        )
        return

    if task_number < 1 or task_number > count:
        messagebox.showerror(
            "Invalid Task",
            f"Enter a number between 1 and {count}."
        )
        return

    tasks = scrolled_text.get("1.0", END).strip().split("\n")
    deleted_task = tasks.pop(task_number - 1)
    completed = messagebox.askyesno(
        "Task Status",
        "Did you complete this task?"
    )
    scrolled_text.delete("1.0", END)

    for index, task in enumerate(tasks, start=1):
        task_name = task[3:]   # Remove old "1. " / "2. " etc.
        scrolled_text.insert(
            END,
            f"{index}. {task_name}\n"
        )

    count -= 1
    delete_task.set("")

    # Display result
    task_name = deleted_task[3:]

    if completed:
        messagebox.showinfo(
            "Task Completed",
            f"Great! You completed:\n{task_name}"
        )
    else:
        messagebox.showinfo(
            "Task Deleted",
            f"Task aborted:\n{task_name}"
        )


def clear_tasks():
    global count

    if count == 0:
        return

    answer = messagebox.askyesno(
        "Clear Tasks",
        "Are you sure you want to remove all tasks?"
    )

    if answer:
        scrolled_text.delete("1.0", END)
        count = 0
        delete_task.set("")
title = Label(
    window,
    text="To-Do List",
    font=("Arial", 28, "bold"),
    bg="#d9f7be"
)
title.pack(pady=20)


# Add task section

task_label = Label(
    window,
    text="Enter your task",
    font=("Arial", 16),
    bg="#d9f7be"
)
task_label.pack()


new_item = StringVar()

new_task = Entry(
    window,
    width=50,
    font=("Arial", 15),
    textvariable=new_item
)
new_task.pack(
    ipady=8,
    padx=20,
    pady=10
)


add_button = Button(
    window,
    text="Add Task",
    width=15,
    bg="white",
    borderwidth=0,
    font=("Arial", 12, "bold"),
    cursor="hand2",
    command=add_item
)
add_button.pack(pady=5)


# Task display

scrolled_text = ScrolledText(
    window,
    width=60,
    height=12,
    wrap="word",
    font=("Arial", 14)
)
scrolled_text.pack(
    padx=20,
    pady=20
)


# Delete section

delete_label = Label(
    window,
    text="Enter task number to delete",
    font=("Arial", 14),
    bg="#d9f7be"
)
delete_label.pack(pady=5)


delete_task = IntVar(value=0)

delete_entry = Entry(
    window,
    width=10,
    font=("Arial", 14),
    textvariable=delete_task,
    justify="center"
)
delete_entry.pack(pady=5)


button_frame = Frame(
    window,
    bg="#d9f7be"
)
button_frame.pack(pady=15)


delete_button = Button(
    button_frame,
    text="Delete",
    width=12,
    bg="#ff6b6b",
    fg="white",
    borderwidth=0,
    font=("Arial", 11, "bold"),
    cursor="hand2",
    command=delete_item
)
delete_button.grid(row=0, column=0, padx=5)


clear_button = Button(
    button_frame,
    text="Clear All",
    width=12,
    bg="#555555",
    fg="white",
    borderwidth=0,
    font=("Arial", 11, "bold"),
    cursor="hand2",
    command=clear_tasks
)
clear_button.grid(row=0, column=1, padx=5)
new_task.bind("<Return>", lambda event: add_item())
new_task.focus()

window.mainloop()
