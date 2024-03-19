import tkinter as tk
from tkinter import messagebox, ttk

dataset = [
    {
        "question":"What is the capital of France",
        "choices": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    }, 
    
    {
        "question":"Who is the CEO of Tesla",
        "choices": ["Jeff Bezos", "Elon Musk", "Bill Gates", "Tony Stark"],
        "answer": "Elon Musk"
    },

    {
        "question":"The iPhone was created by which company?",
        "choices": ["Apple", "Intel", "Amazon", "Microsoft"],
        "answer": "Apple"
    },

    {
        "question":"How many Harry Potter books are there?",
        "choices": ["1", "4", "6", "7"],
        "answer": "7"
    }
    
]

current_question = 0

def show_question():
    question = dataset[current_question]
    qs_label.config(text=question["question"])

    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")

    feedback_label.config(text="")
    next_btn.config(state="disabled")

def check_answer(choice):
    question = dataset[current_question]
    selected_choice = choice_btns[choice].cget("text")
    if selected_choice == question["answer"]:
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(dataset)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")

    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

def next_question():
    global current_question
    current_question += 1
    if current_question < len(dataset):
        show_question()
    else:
        messagebox.showinfo("Quiz Completed", "Quiz Completed! Final Score: {}/{}".format(score, len(dataset)))
        root.destroy()

root = tk.Tk()
root.title("Quiz App")
root.geometry("600x500")
root.configure(bg="lightblue")  # Set the background color of the window

qs_label = ttk.Label(
    root,
    text="Question",
    font=("Arial", 16),
    wraplength=500,
    padding=10,
    background="lightblue"  # Set the background color of the label
)
qs_label.pack(pady=10)

choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        text="Choice {}".format(i+1),
        command=lambda i=i: check_answer(i),
        width=20,
        style="C.TButton"  # Set a custom style for the button
    )
    button.pack(pady=5)
    choice_btns.append(button)

feedback_label = ttk.Label(
    root,
    text="Feedback",
    font=("Arial", 12),
    padding=10,
    background="lightblue"
)
feedback_label.pack(pady=10)

score = 0

score_label = ttk.Label(
    root,
    text="Score: 0/{}".format(len(dataset)),
    font=("Arial", 12),
    padding=10,
    background="lightblue"
)
score_label.pack(pady=10)

next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled",
    style="C.TButton"
)
next_btn.pack(pady=10)

show_question()

root.mainloop()
