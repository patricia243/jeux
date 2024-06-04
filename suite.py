# tic_tac_toe.py
#créer l'interface graphique Tkinter avec deux module
import tkinter as tk
from tkinter import font

#définit la classe TicTacToeBoard qui hérite de la classe tk.Tk
class TicTacToeBoard(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self._cells = {} #stocker les boutons de la grille de jeu.                           
        self.current_player = "X"
        self.game_is_active = True
        self._winner = None
        self._create_board_display()
        self._create_board_grid()
#crée un cadre (Frame) pour afficher le texte "Bienvenu dans le jeux ?"
    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
         # Label Tkinter avec une police de caractères
        self.display = tk.Label(
            master=display_frame,
            text="Bienvenu dans le jeux ?",
           
            font=font.Font(size=16, weight="bold"),
        )
        self.display.pack()
#disposés dans la grille à l'aide 
    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(3):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                )
                self._cells[button] = (row, col)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )
#lance la boucle d'événements principale de Tkinter
    def run_game(self):
        self.mainloop()
#pour démarrer le jeu
if __name__ == "__main__":
    board = TicTacToeBoard()
    board.run_game()


       