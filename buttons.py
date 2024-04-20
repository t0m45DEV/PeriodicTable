from io import *
from tkinter import messagebox
import tkinter

class Button():

    def __init__(self, where, name, row, column):

        self.name = name

        name = tkinter.Button(where, text=name, command=self.showinfo)
        name.grid(row=row, column=column, sticky="nsew", pady=2, padx=2)

        if column == 0 and row == 0:
            name.config(bg="#affc41")

        elif column < 2:
            name.config(bg="#90e0ef")

        elif (column >= 3 and row == 7) or (column >= 3 and row == 8):
            name.config(bg="#a3ddd0")

        elif column >= 2 and column <= 11:
            name.config(bg="light green")

        elif column == 17:
            name.config(bg="#ffe774")

        elif (column >= 12 and column <=16) and row == 1:
            name.config(bg="pink")

        elif (column >= 13 and column <=16) and row == 2:
            name.config(bg="pink")

        elif (column >= 14 and column <=16) and row == 3:
            name.config(bg="pink")

        elif (column >= 15 and column <=16) and row == 4:
            name.config(bg="pink")

        elif column == 16 and row == 5:
            name.config(bg="pink")

        else:
            name.config(bg="light yellow")

    def readinfo(self):
        info = open(("Elements/"+(self.name + ".txt")), "r")
        return info.read()

    def showinfo(self):
        info = self.readinfo()
        messagebox.showinfo(self.name, info)
