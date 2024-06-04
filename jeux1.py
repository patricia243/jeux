import tkinter as tk
from tkinter import messagebox
class jeux:
        def_init_(self):
            self.window =tk.Tk()
            self.window.title("jeux")
            self.current_player="m"
            self.board["" for _ in range(9)]
            for i in range (9):
              button=tk.Button(self.window,text="",
                               font=("helvetica",24),
                               height=2,width=5,
                               command=lambda i=i :self.make_move(i) button.grid(row=i//3,column=i %3))
    
