import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

def move_files_and_folders(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        messagebox.showerror("Error", f"Source folder {source_folder} does not exist.")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    items = os.listdir(source_folder)

    for item_name in items:
        source_item = os.path.join(source_folder, item_name)
        mod_time = os.path.getmtime(source_item)
        date_folder = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')
        destination_date_folder = os.path.join(destination_folder, date_folder)

        if not os.path.exists(destination_date_folder):
            os.makedirs(destination_date_folder)

        destination_item = os.path.join(destination_date_folder, item_name)

        try:
            shutil.move(source_item, destination_item)
            print(f"Moved: {source_item} to {destination_item}")
        except Exception as e:
            print(f"Error moving {source_item} to {destination_item}: {e}")

    messagebox.showinfo("Success", "Files and folders moved successfully!")

def select_source_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        source_folder_var.set(folder_selected)

def select_destination_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        destination_folder_var.set(folder_selected)

def move_action():
    source_folder = source_folder_var.get()
    destination_folder = destination_folder_var.get()
    move_files_and_folders(source_folder, destination_folder)

# Create the main application window
root = tk.Tk()
root.title("File and Folder Mover")

source_folder_var = tk.StringVar()
destination_folder_var = tk.StringVar()

# Source folder selection
tk.Label(root, text="Source Folder:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=source_folder_var, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse...", command=select_source_folder).grid(row=0, column=2, padx=10, pady=10)

# Destination folder selection
tk.Label(root, text="Destination Folder:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=destination_folder_var, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse...", command=select_destination_folder).grid(row=1, column=2, padx=10, pady=10)

# Move button
tk.Button(root, text="Move Files and Folders", command=move_action).grid(row=2, column=0, columnspan=3, padx=10, pady=20)

# Start the GUI event loop
root.mainloop()
