import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Super Log Hunter v2.0")
root.geometry("400x450")

selected_folder = ""

def select_folder_path():
    global selected_folder
    selected_folder = filedialog.askdirectory()
    
    if selected_folder != "":
        lbl_folder_status.config(text=f"Folder: {selected_folder} ✅", fg="blue")

def scan_logs():
    if selected_folder == "":
        lbl_result.config(text="⚠️ First select a folder.!", fg="red")
        return

    secret_word = enter_word.get()
    errors_found = 0

    for file_name in os.listdir(selected_folder):
        if file_name.endswith(".txt"):
            full_path = os.path.join(selected_folder, file_name)
            
            with open(full_path, "r", encoding="utf-8", errors="ignore") as my_file:
                text_file = my_file.read()
                
            my_file.close()

            if secret_word in text_file:
                errors_found = errors_found + 1
                
    lbl_result.config(text=f"Files containing the word '{secret_word}': {errors_found}", fg="green")


lbl1 = tk.Label(root, text="1. Select a folder to scan", font=("Arial", 11, "bold"))
lbl1.pack(pady=10)

btn_folder = tk.Button(root, text="📂 Browse...", font=("Arial", 10), command=select_folder_path)
btn_folder.pack(pady=5)

lbl_folder_status = tk.Label(root, text="No folder selected", font=("Arial", 10), fg="gray")
lbl_folder_status.pack(pady=5)

lbl2 = tk.Label(root, text="2. What word should I look for? (ERROR, error, wrong...)", font=("Arial", 11, "bold"))
lbl2.pack(pady=10)

enter_word = tk.Entry(root, font=("Arial", 12), width=20)
enter_word.insert(0, "ERROR")
enter_word.pack(pady=5)

btn_start = tk.Button(root, text="🚀 Start", font=("Arial", 14, "bold"), bg="green", fg="white", command=scan_logs)
btn_start.pack(pady=25)

lbl_result = tk.Label(root, text="waiting for launch...", font=("Arial", 12))
lbl_result.pack(pady=10)

root.mainloop()
