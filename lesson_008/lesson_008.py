from tkinter import messagebox
from lesson_006 import game
import tkinter

# Lesson 008
##############################################################################################
# User Interface with TKinter

engine = game.GameEngine()
secret = 22


def check_guess():
    message = engine.play(int(guess.get()))

    if isinstance(message, list):
        message = message[0]

    messagebox.showinfo("Game Info", "Best Play: {}".format(message))

    # Closes main window if the secret number is correct
    if secret == int(guess.get()):
        window.destroy()
        return

    # Clean the guess text field after attempt was made
    guess.delete(0, "end")


window = tkinter.Tk()
window.geometry("350x250")

# greeting text
greeting = tkinter.Label(window, text="Guess the secret number!", font=("Helvetica", 18), pady=35)
greeting.pack()

instructions = tkinter.Label(window, text="Enter a number between 1 and 30", font=("Helvetica", 14), pady=10)
instructions.pack()

# guess entry field
guess = tkinter.Entry(window)
guess.pack()

spacer = tkinter.Label(window, pady=5)
spacer.pack()

# submit button
submit = tkinter.Button(window, text="Submit", command=check_guess)  # check_guess, not check_guess()
submit.pack()

window.mainloop()

##############################################################################################
