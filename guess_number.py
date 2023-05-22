from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.geometry("450x320")
window.title("[Challenge] - Guess the number")
window.configure(bg="gainsboro")


def randomizator():
    b = int(random.choice(range(10)))
    try:
        if b == int(guess_entry1.get()):
            guess_answer.config(text="YOU WIN!\nHECK YEAH!", bg="teal", fg="white")
            guess_i_said_label.config(text=b)
        else:
            guess_answer.config(text="YOU LOSE\nTRY AGAIN!", bg="gainsboro", fg="red")
            guess_i_said_label.config(text=b)
    except ValueError:
        if (guess_entry1.get()) == "":
            pass
        elif (guess_entry1.get()) == " ":
            messagebox.showerror("Alerta",
                                 "Debe ingresar números enteros")
            guess_entry1.delete(0, END)
        else:
            messagebox.showerror("Alerta",
                                 "Intente colocar un número entero")
            guess_entry1.delete(0, END)


guess_title = Label(window,
                    text="Guess the number",
                    font="Fixedsys 26 italic bold underline",
                    bg="gainsboro").pack()

guess_u_said = Label(window,
                    text="You said:",
                    font="Fixedsys 20 italic bold",
                    bg="gainsboro").pack()

guess_entry1 = Entry(window,
                    text="",
                    font="Fixedsys 20 bold",
                    width=13,
                    justify=CENTER,
                    bg="gainsboro",
                    fg="green")
guess_entry1.focus()
guess_entry1.pack()

guess_i_said = Label(window,
                    text="I said: ",
                    font="Fixedsys 20 italic bold",
                    bg="gainsboro").pack()

guess_i_said_label = Label(window,
                    text=" * ",
                    font="Fixedsys 20 italic bold",
                    bg="gainsboro",
                    fg="green")
guess_i_said_label.pack()

guess_answer = Label(window,
                    text="_ _ _",
                    font="Fixedsys 22 bold",
                    bg="gainsboro",
                    fg="green")
guess_answer.pack()

guess_button = Button(window,
                      text="GuEsS",
                      font="Terminal 18 bold",
                      fg="navy",
                      command=randomizator).pack()

window.mainloop()
