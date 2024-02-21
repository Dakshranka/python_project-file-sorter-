import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
def organize_files():
    path = entry_path.get()
    if not os.path.exists(path):
        messagebox.showerror("Error", "Invalid directory path.")
        return
    folder_names = ['pptx', 'pdf', 'document']
    file_names = os.listdir(path)
    for folder_name in folder_names:
        folder_path = os.path.join(path, folder_name)
        try:
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create folder: {folder_name}\nError: {str(e)}")
    
    for file_name in sorted(file_names, key=lambda x: os.path.getmtime(os.path.join(path, x))):
        file_path = os.path.join(path, file_name)
        if os.path.isfile(file_path):
            try:
                if file_name.lower().endswith('.pptx'):
                    shutil.move(file_path, os.path.join(path, 'pptx', file_name))
                elif file_name.lower().endswith('.pdf'):
                    shutil.move(file_path, os.path.join(path, 'pdf', file_name))
                elif file_name.lower().endswith('.docx'):
                    shutil.move(file_path, os.path.join(path, 'document', file_name))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to move file: {file_name}\nError: {str(e)}")
    
    messagebox.showinfo("Success", "Files have been organized successfully!")

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, folder_path)

root = tk.Tk()
root.title("File Sorter")

entry_path = tk.Entry(root, width=50)
entry_path.grid(row=0, column=0, padx=10, pady=10)
browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.grid(row=0, column=1, padx=5, pady=10)
organize_button = tk.Button(root, text="Organize Files", command=organize_files)
organize_button.grid(row=1, column=0, columnspan=2, pady=10)
root.mainloop()
