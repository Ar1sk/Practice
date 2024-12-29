import tkinter as tk

def greet():
    name = entry.get()
    if name:
        label.config(text=f"Hello, {name}!")
    else:
        label.config(text="Please enter your name!")

root = tk.Tk()
root.title("AnalisaApp")
root.geometry("300x150")

label = tk.Label(root, text="Enter your name:", font=("Arial", 12))
label.pack(pady=5)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

button = tk.Button(root, text="Greet", command=greet, font=("Arial", 12))
button.pack(pady=10)

root.mainloop()
