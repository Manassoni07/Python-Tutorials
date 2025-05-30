import tkinter as tk
from time import strftime

# Create window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.configure(bg="black")

# Create clock label
label = tk.Label(root, font=('Arial', 48), background='black', foreground='cyan')
label.pack(anchor='center', expand=True)

# Update time every second
def update_time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, update_time)

update_time()
root.mainloop()
