import tkinter as tk
import random 
user_wins=0
computer_win=0

options=["rock","paper","scissors"]

def play(user_input):
    global user_wins,computer_win
    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    result_label.config(text=f"Computer Picked: {computer_pick}")

    if user_input=="Rock" and computer_pick=="scissors":
        result_label.config(text=f"Computer Picked: {computer_pick}\nYou Won")
        user_wins+=1
    elif user_input=="Paper" and computer_pick=="rock":
        result_label.config(text=f"Computer Picked: {computer_pick}\nYou Won")
        user_wins+=1
    elif user_input=="Scissors" and computer_pick=="paper":
        result_label.config(text=f"Computer Picked: {computer_pick}\nYou Won")
        user_wins+=1
    elif user_input== computer_pick:
        result_label.config(text=f"Computer Picked: {computer_pick}\nIt's Draw")
    else:
        result_label.config(text=f"Computer Picked: {computer_pick}\n You Lost")
        computer_win+=1
    
    user_score_label.config(text=f"Your Wins: {user_wins}")
    computer_score_label.config(text=f"Computer Wins: {computer_win}")

def quit():
    root.quit()

def restart():
    result_label.config(text="Make your Choice")
    user_score_label.config(text=f"Your wins: {user_wins}")
    computer_score_label.config(text=f"Computer wins: {computer_win}")

    

#Create GUI window
root=tk.Tk()
root.title("Rock Paper Scissors")

user_score_label=tk.Label(root,text="Your Wins: 0",font=("Arial Bold",12))
user_score_label.pack()

computer_score_label=tk.Label(root,text="Computer Wins : 0",font=("Arial Bold",12))
computer_score_label.pack()

#Label to display result
result_label=tk.Label(root,text="Make Your Chice",font=("Arial Bold",14))
result_label.pack(pady=15)

#Button for user input
rock_button=tk.Button(root,text="Rock",bg="#8c92ac",font=("Arial Bold",14),width=20, command=lambda:play("Rock"))
rock_button.pack(pady=10)

paper_button=tk.Button(root,text="Paper",bg="#8c92ac",font=("Arial Bold",14),width=20,command=lambda:play("Paper"))
paper_button.pack(pady=10)

scissors_button=tk.Button(root,text="Scissors",bg="#8c92ac",font=("Arial Bold",14),width=20,command=lambda:play("Scissors"))
scissors_button.pack(pady=10)

play_again_button=tk.Button(root,text="Play Again,",bg="#8c92ac",font=("Arial Bold",14),width=20,command=restart)
play_again_button.pack(pady=10)



#quit Game
quit_button=tk.Button(root,text="Quit",bg="#8c92ac",font=("Arial Bold",14),width=20, command=quit)
quit_button.pack(pady=20)

root.mainloop()