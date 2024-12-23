from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

window = Tk()
window.title("To Do List")
window.geometry("1000x600")
window.config(bg="lightgreen")

count = 0

def add_item() :
	global  count
	item = new_item.get()
	if len(item) > 0 :
		count += 1
		scrolled_text.insert(END, f"{count}. {item}\n")
		new_item.set("")
	else :
		messagebox.showerror("Empty Task", "Task Entry box is empty")


def delete_item() :
	global count
	task_to_delete = delete_task.get()
	if count >= task_to_delete > 0:
		count -= 1
		task_completion = messagebox.askquestion("Task", "Did you completed your task")
		all_tasks = scrolled_text.get("1.0", "end")
		all_tasks = all_tasks.split("\n")[ :-2]
		task_for_delete = all_tasks.pop(task_to_delete- 1)
		all_tasks = [task_list for index, task_list in enumerate(all_tasks) if (index, task_list) is not (task_to_delete-1,task_for_delete)]
		scrolled_text.delete("1.0", "end")
		for index, one_task in enumerate(all_tasks) :
			scrolled_text.insert(END, f"{index+1}. {one_task[2:]}\n")

		if task_completion == "yes" :
			messagebox.showinfo("Task Deleted", f"You Completed {task_for_delete[:2]}")
		else :
			messagebox.showinfo("Task Deleted", f"Your task is aborted")

	else :
		messagebox.showerror("Error occured", "You Enter the wrong value for deletion")



new_item = StringVar()
delete_task = IntVar()
task = Label(window, text="Enter the Task", font="lucida 20 normal", bg="lightgreen")
task.pack()
new_task = Entry(width=70, font="lucida 15 normal", textvariable=new_item)
new_task.pack(ipadx=30, ipady=10, padx=10, pady=10)
Button(window, width=10, bg="white", text="Add", borderwidth=0, font=("Arial", 8), cursor="hand2", command=add_item).pack()
scrolled_text = ScrolledText(window, width=50, height=10, wrap="word", font=("Arial", 14))
scrolled_text.pack(padx=20, pady=10, ipadx=10)
delete_label = Label(text="Enter the no. of task : ", bg="lightgreen", font=("Arial", 15))
delete_label.pack(padx=10, pady=10)
delete_entry = Entry(cursor="hand2", width=10, font=("Arial", 15), textvariable=delete_task)
delete_entry.pack(padx=10, pady=20, anchor="n")
Button(text="Delete", width=10, height=1, bg="red", borderwidth=0, command=delete_item, ).pack()



window.mainloop()






