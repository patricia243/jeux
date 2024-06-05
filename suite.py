# tic_tac_toe.py
#créer l'interface graphique Tkinter avec deux module
import tkinter as tk
from tkinter import font

#définit la classe TicTacToeBoard qui hérite de la classe tk.Tk
class TicTacToeBoard(tk.Tk):

    def __init__(self):
        super().__init__()
        self.joueur = "X"
        self.title("Tic-Tac-Toe Game")
        self._cells = {} #stocker les boutons de la grille de jeu.                           
    #
        self.current_player = "X"
       
        self.game_is_active = False
        self._winner = None

        self._create_board_display()
        self._create_board_grid()

    def click(self, id_button):
        if self.joueur == "X":
             self.joueur = "O"
        else:
             self.joueur = "X"
        if id_button == 1:
            self.button_1.config(text=self.joueur)
            
        elif id_button == 2: 
            self.button_2.config(text=self.joueur)

        elif id_button == 3:
            self.button_3.config(text=self.joueur)

        
        elif id_button == 4:
            self.button_4.config(text=self.joueur)
            
        elif id_button == 5:
            self.button_5.config(text=self.joueur)
            
        elif id_button == 6:
            self.button_6.config(text=self.joueur)
            
        elif id_button == 7:
            self.button_7.config(text=self.joueur)
            
        elif id_button == 8:
            self.button_8.config(text=self.joueur)
            
        elif id_button == 9:
            self.button_9.config(text=self.joueur)


    def ations_button_2(self):

        if self.current_player == "X":
           #self.button_2.con2fig(text="O")
           self._toggle_player()
           self._update_display()
       

  #fin de le  premiere fonction 
    def _create_board_grid(self):
        
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        # for row in range(3):
        #     self.rowconfigure(row, weight=1, minsize=50)
        #     self.columnconfigure(row, weight=1, minsize=75)
        #     for col in range(3):
        #         button = tk.Button(
        #             master=grid_frame,
        #             text="X",
        #             font=font.Font(size=36, weight="bold"),
        #             fg="black",
        #             width=3,
        #             height=2,
        #             highlightbackground="lightblue",
        #         )
        #         self._cells[button] = (row, col)
        #         button.grid(
        #             row=row,
        #             column=col,
        #             padx=5,
        #             pady=5,
        #             sticky="nsew"
        #         )  

        self.button_1 = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=30, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                    command=lambda : self.click(1)
                )   
        self.button_1.grid(
                    row=0,
                    column=0,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )  

        self.button_2 = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=30, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    command=lambda : self.click(2)
                    #highlig8htbackground="lightblue",
                )   
        self.button_2.grid(
                    row=0,
                    column=1,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                ) 
        self.button_3 = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=30, weight="bold"),
                    
                    fg="black",
                    width=3,
                    height=2,
                    command=lambda : self.click(3)
                    #highlightbackground="lightblue",
                )   
        self.button_3.grid(
                    row=0,
                    column=2,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )
        self.button_4 = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=30, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    command=lambda : self.click(4)
                    #highlightbackground="lightblue",
                )   
        self.button_4.grid(
                    row=1,
                    column=0,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )
        self.button_5 = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=30, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    command=lambda : self.click(5)
                    #highlightbackground="lightblue",
                )   
        self.button_5.grid(
                    row=1,
                    column=1,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )
        self.button_6 = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=30, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    command=lambda : self.click(6)
                    #highlightbackground="lightblue",
                )   
        self.button_6.grid(
                    row=1,
                    column=2,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )
        self.button_7 = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=30, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    command=lambda : self.click(7)
                   # highlightbackground="lightblue",
                )   
        self.button_7.grid(
                    row=2,
                    column=0,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )
        self.button_8 = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=30, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    command=lambda : self.click(8)
                    #highlightbackground="lightblue",
                )   
        self.button_8.grid(
                    row=2,
                    column=1,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )
        self.button_9 = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=30, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    command=lambda : self.click(9)
                    #highlightbackground="lightblue",
                )   
        self.button_9.grid(
                    row=2,
                    column=2,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )
        
         

# foncton2 crée un cadre (Frame) pour afficher le texte "Bienvenu dans le jeux ?"
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


            #elle vérifie si l'utilisateur a appuyé sur la touche "R" pour ou "N"
    def _handle_keypress(self, event):
            if not self.game_is_active:
                if event.char.upper() == "X":
                    self._reset_game()
            else:
                if event.char.upper() == "O":
                    self._toggle_player()
                    self._update_display()
    def _reset_game(self):
            self.game_is_active = True
            self._winner = None
            self.current_player = "X"
            for button in self._cells:
                button.config(text="", fg="black")
                self._update_display()
    def _check_winner(self):
            for player in ["X", "O"]:
                if any(all(self._cells[button] == player for button in win_condition)
                for win_condition in [
                    [self._cells[button] for button in (b1, b2, b3)],
                    [self._cells[button] for button in (b1, b4, b7)],
                    [self._cells[button] for button in (b1, b5, b9)],
                    [self._cells[button] for button in (b3, b6, b9)],
                    [self._cells[button] for button in (b3, b5, b7)],
                    [self._cells[button] for button in (b2, b5, b8)],
                    [self._cells[button] for button in (b4, b5, b6)],
                    [self._cells[button] for button in (b7, b8, b9)]
                ]):
                    self._winner = player
                break
            else:
                self._winner = None

    #disposés dans la grille à l'aide 
    
                    
    #lance la boucle d'événements principale de Tkinter
    def run_game(self):
            self.mainloop()
    #pour démarrer le jeu
if __name__ == "__main__":
        board = TicTacToeBoard()
        board.run_game()


        