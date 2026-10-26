# DSA Microproject: Undo-Redo Text Editor Using Stack
# GUI using Python Tkinter

import tkinter as tk
from tkinter import messagebox, filedialog

undo_stack = []
redo_stack = []
text = ""


def update_display():
    editor.configure(state="normal")
    editor.delete("1.0", tk.END)
    editor.insert("1.0", text)
    editor.configure(state="disabled")
    status_var.set(f"Characters: {len(text)}")


def add_text():
    global text

    new_text = input_box.get().strip()

    if not new_text:
        messagebox.showinfo("No Text", "Please enter some text.")
        return

    undo_stack.append(text)
    text = text + (" " if text else "") + new_text

    # Clear redo history after a new edit
    redo_stack.clear()

    input_box.delete(0, tk.END)
    update_display()


def undo():
    global text

    if not undo_stack:
        messagebox.showinfo("Undo", "Nothing to undo!")
        return

    redo_stack.append(text)
    text = undo_stack.pop()
    update_display()


def redo():
    global text

    if not redo_stack:
        messagebox.showinfo("Redo", "Nothing to redo!")
        return

    undo_stack.append(text)
    text = redo_stack.pop()
    update_display()


def clear_text():
    global text

    if not text:
        return

    undo_stack.append(text)
    text = ""
    redo_stack.clear()
    update_display()


def save_file():
    file_path = filedialog.asksaveasfilename(
        title="Save Text",
        defaultextension=".txt",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text)

            messagebox.showinfo(
                "Saved",
                "Text file saved successfully!"
            )

        except OSError as error:
            messagebox.showerror("Save Error", str(error))


def open_file():
    global text

    file_path = filedialog.askopenfilename(
        title="Open Text",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                loaded_text = file.read()

            undo_stack.append(text)
            text = loaded_text
            redo_stack.clear()
            update_display()

        except OSError as error:
            messagebox.showerror("Open Error", str(error))


def show_about():
    messagebox.showinfo(
        "About Project",
        "Undo-Redo Text Editor Using Stack\n\n"
        "DSA Microproject using Python and Tkinter.\n\n"
        "Undo Stack stores previous text states.\n"
        "Redo Stack stores undone text states."
    )


# Main window
root = tk.Tk()
root.title("Undo-Redo Text Editor Using Stack")
root.geometry("850x600")
root.minsize(650, 450)
root.configure(bg="#F4F6F8")


# Header
header = tk.Frame(
    root, bg="#17365D", padx=18, pady=14
)
header.pack(fill="x")

tk.Label(
    header,
    text="Undo-Redo Text Editor",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#17365D"
).pack(anchor="w")

tk.Label(
    header,
    text="DSA Microproject | Python | Stack Data Structure",
    font=("Arial", 10),
    fg="#E5EDF7",
    bg="#17365D"
).pack(anchor="w", pady=(4, 0))


# Text input section
input_frame = tk.Frame(
    root, bg="#F4F6F8", padx=18, pady=12
)
input_frame.pack(fill="x")

tk.Label(
    input_frame,
    text="Enter text:",
    font=("Arial", 10, "bold"),
    bg="#F4F6F8",
    fg="#222222"
).pack(anchor="w")

input_row = tk.Frame(input_frame, bg="#F4F6F8")
input_row.pack(fill="x", pady=(5, 0))

input_box = tk.Entry(
    input_row,
    font=("Arial", 11),
    relief="solid",
    bd=1
)
input_box.pack(side="left", fill="x", expand=True, ipady=7)
input_box.bind("<Return>", lambda event: add_text())


def make_button(parent, label, command, color="#FFFFFF"):
    return tk.Button(
        parent,
        text=label,
        command=command,
        font=("Arial", 10, "bold"),
        padx=12,
        pady=7,
        bg=color,
        fg="#17365D",
        activebackground="#DBE7F5",
        relief="groove",
        cursor="hand2"
    )


make_button(
    input_row, "Add Text", add_text, "#DCE8F5"
).pack(side="left", padx=(8, 0))


# Toolbar buttons
toolbar = tk.Frame(root, bg="#F4F6F8", padx=18)
toolbar.pack(fill="x", pady=(0, 10))

make_button(
    toolbar, "Undo", undo, "#E7EEF8"
).pack(side="left", padx=(0, 8))

make_button(
    toolbar, "Redo", redo, "#E7EEF8"
).pack(side="left", padx=(0, 8))

make_button(
    toolbar, "Clear Text", clear_text, "#FBE9E7"
).pack(side="left", padx=(0, 8))

make_button(
    toolbar, "Open File", open_file
).pack(side="left", padx=(0, 8))

make_button(
    toolbar, "Save File", save_file
).pack(side="left", padx=(0, 8))

make_button(
    toolbar, "About", show_about
).pack(side="right")


# Current text display
editor_frame = tk.Frame(
    root, bg="#F4F6F8", padx=18, pady=4
)
editor_frame.pack(fill="both", expand=True)

tk.Label(
    editor_frame,
    text="Current Text",
    font=("Arial", 10, "bold"),
    bg="#F4F6F8",
    fg="#222222"
).pack(anchor="w", pady=(0, 5))

text_frame = tk.Frame(
    editor_frame, bg="white", bd=1, relief="solid"
)
text_frame.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side="right", fill="y")

editor = tk.Text(
    text_frame,
    wrap="word",
    font=("Consolas", 12),
    padx=10,
    pady=10,
    relief="flat",
    yscrollcommand=scrollbar.set
)
editor.pack(side="left", fill="both", expand=True)

scrollbar.config(command=editor.yview)
editor.configure(state="disabled")


# Status bar
status_var = tk.StringVar(value="Characters: 0")

tk.Label(
    root,
    textvariable=status_var,
    anchor="w",
    font=("Arial", 9),
    bg="#E6E9ED",
    fg="#333333",
    padx=18,
    pady=7
).pack(fill="x")


# Start application
update_display()
input_box.focus_set()
root.mainloop()