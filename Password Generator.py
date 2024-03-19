import tkinter as tk
import random
import string 

def generate_password():
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password_length = int(password_input.get("1.0", "end"))
    password = "".join(random.choice(all_characters) for _ in range(password_length))
    output.config(state="normal")
    output.delete("1.0", "end")
    output.insert("1.0", password)
    output.config(state="disabled") 

def accept_password():
    username = username_input.get("1.0", "end")
    password = output.get("1.0", "end")
    print(f"Accepted Username: {username}, Password: {password}")

def reset_all_fields():
    username_input.delete("1.0", "end")
    password_input.delete("1.0", "end")
    output.config(state="normal")
    output.delete("1.0", "end")
    output.config(state="disabled")

root = tk.Tk()
root.geometry("400x450")
root.title("Password Generator")
root.resizable(width=False, height=False)

title_label = tk.Label(root, text="Password Generator", fg="blue", font=("Arial", 18, "underline"))
title_label.place(x=90, y=10)

username_label = tk.Label(root, text = "Enter user name:", font=("Arial", 12))
username_label.place(x=20, y=70)
password_label = tk.Label(root, text = "Enter password length:", font=("Arial", 12))
password_label.place(x=20, y=120)
output_label = tk.Label(root, text = "Generated Password:", font=("Arial", 12))
output_label.place(x=20, y=170)

username_input = tk.Text(root, height=1, width=15, font=("Arial"))
username_input.place(x=190,y=70)
password_input = tk.Text(root, height=1, width=15, font=("Arial"))
password_input.place(x=190,y=120)
output = tk.Text(root, height=1, width=15, font=("Arial"), state="disabled")
output.place(x=190,y=170)

generate_password_btn = tk.Button(root, text="GENERATE PASSWORD", height=2, width=19, bg="blue", fg="white", font=("Arial", 9, "bold"), command=generate_password)
generate_password_btn.place(x=120,y=230)

accept_btn = tk.Button(root, text="ACCEPT", fg="blue", height=2, width=10, command=accept_password)
accept_btn.place(x=150, y=290)

reset_btn = tk.Button(root, text="RESET", fg="blue", height=2, width=10, command=reset_all_fields)
reset_btn.place(x=150, y=350)

root.mainloop()
