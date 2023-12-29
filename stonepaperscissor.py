import tkinter as tk
from tkinter import messagebox
import random

def play_game(player_choice):
    choices = ["Stone", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result = determine_winner(player_choice, computer_choice)

    message = f"You chose {player_choice}\nComputer chose {computer_choice}\n\n"
    if result == 'win':
        message += "You Win!"
    elif result == 'lose':
        message += "You Lose!"
    else:
        message += "It's a Tie!"

    messagebox.showinfo("Result", message)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'tie'
    elif (
        (player_choice == 'Stone' and computer_choice == 'Scissors') or
        (player_choice == 'Paper' and computer_choice == 'Stone') or
        (player_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        return 'win'
    else:
        return 'lose'


root = tk.Tk()
root.title("Stone-Paper-Scissors Game")


label = tk.Label(root, text="Choose your move:")
label.pack(pady=10)

choices = ["Stone", "Paper", "Scissors"]

for choice in choices:
    tk.Button(root, text=choice, command=lambda c=choice: play_game(c)).pack()


root.mainloop()
