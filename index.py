from tkinter import *
import datetime
root = Tk()
root.geometry("400x400")
root.config(bg="black")
root.title("Digital Clock")

design = Frame(root, bg="black",highlightbackground="red",highlightthickness=2)
design.place(relx=0.5, rely=0.5, anchor="center", height=350, width=350)

