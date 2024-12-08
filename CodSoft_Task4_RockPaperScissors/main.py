import random
import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
def play_game():
    global playing
    while playing:
        player = None
        while player not in moves:
            player = simpledialog.askstring("Your Move", "Choose your move(rock,paper,scissor): ").lower()
            if player is None:
                return

        computer = random.choice(moves)

        messagebox.showinfo("Game Result", f"Player: {player}\nComputer: {computer}")

        if player == computer:
            result ="It's a tie!"
        elif player == "scissor" and computer == "paper":
            result ="You Win!"
        elif player == "paper" and computer == "rock":
            result ="You Win!"
        elif player == "rock" and computer == "scissor":
            result ="You Win!"
        else:
            result = "You Lost!!"

        messagebox.showinfo("Result", result)

        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if not play_again:
            playing = False
            messagebox.showinfo("Goodbye","Thank you for playing!")

def exit_game():
    global playing
    playing = False
    root.quit()

moves =("rock","paper","scissor")
playing = True

#root.tk.Tk()
root.title("Rock-Paper-Scissor Game")
root.geometry("600x600")

root.config(bg="grey")


title = tk.Label(root,text="Rock-Paper-Scissor Game", font=("Arial",32,"bold"))
title.pack(pady=30)

start_button = tk.Button(root,text="Start Game", width=30,height=5, command=play_game,font=("Arial",15,"bold"))
start_button.pack(pady=30)

exit_button = tk.Button(root, text="Exit",width=25,height =3, command=exit_game,font=("Arial",15,"bold"))
exit_button.pack(pady=20)

root.mainloop()
