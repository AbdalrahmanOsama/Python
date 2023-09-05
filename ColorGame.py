import random
import tkinter


colors = ["Red", "White", "Yellow", "Pink", "Blue", "Black", "Brown", "Purple", "Green", "Cyan"]

score = 0
time_left = 60


def game(play):
    if time_left == 60:
        countdown()
    change_color()


def change_color():
    global score
    global time_left

    if time_left > 0:
        e.focus_set()
        if e.get().lower() == colors[1].lower():
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(colors)
        label.config(fg=str(colors[1]), text=str(colors[0]))
        score_label.config(text=f"Score: {str(score)}")


def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        time_label.config(text=f"Time remaining: {str(time_left)}")
        time_label.after(1000, countdown)

    if time_left == 0:
        game_over_label.config(text=f"Game Over!!\nYour Score is {str(score)}\n\U0001f600")
        game_over_label.pack()



root = tkinter.Tk()
root.title("ColorGame")
root.geometry("600x400")

instruct = tkinter.Label(root, text="What is The Color?", font=("san=serif", 30))
instruct.pack()

score_label = tkinter.Label(root, text="Press Enter to start", font=("san-serif", 24))
score_label.pack()

time_label = tkinter.Label(root, text=f"Time remaining: {str(time_left)}", font=("san-serif", 18))
time_label.pack()

label = tkinter.Label(root, font=("san-serif", 60))
label.pack()

e = tkinter.Entry(root)
root.bind("<Return>", game)
e.pack()
e.focus_set()

game_over_label = tkinter.Label(root, text="", font=("san-serif", 20))

root.mainloop()
