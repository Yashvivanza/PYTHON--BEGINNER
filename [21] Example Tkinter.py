import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Tkinter GUI Example")
root.geometry("400x300")

# Label
label = tk.Label(root, text="Enter your name:", font=("Arial", 12))
label.pack(pady=10)

# Text field (Entry)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Function to display name
def display_name():
    name = entry.get()
    result_label.config(text=f"Hello, {name}!")
    # Insert into table too
    tree.insert("", "end", values=(name, "Registered"))

# Button
button = tk.Button(root, text="Submit", command=display_name)
button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

# Table (Treeview for tabular display)
tree = ttk.Treeview(root, columns=("Name", "Status"), show="headings", height=5)
tree.heading("Name", text="Name")
tree.heading("Status", text="Status")
tree.pack(pady=10)

# Run window
root.mainloop()
