import customtkinter as ctk

def add_todo():
    task = entry.get()
    label = ctk.CTkLabel(scrollable_frame, text=task)
    label.pack()
    entry.delete(0, ctk.END)

root = ctk.CTk()
root.geometry("750x450")
root.title("Mr Toodo")

title_label = ctk.CTkLabel(root, text="Task List", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(40, 20))

scrollable_frame = ctk.CTkScrollableFrame(root, width=500, height=200)
scrollable_frame.pack()

entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add task")
entry.pack(fill="x")

add_button = ctk.CTkButton(root, text="Add", width=500, command=add_todo)
add_button.pack(pady=20)

root.mainloop()
