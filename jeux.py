import tkinter as tk
from tkinter import messagebox
class jeux:
    def __init__(self) :
     self.current_player="X"
     self.board= [
           [ "" for _ in range (3)]for _ in range(3)
]
     self.root=tk.Tk()
     self.root.title("jeux")
     self.buttons= [
            [""  for _ in  range (3)]for _ in  range(3)
           ]
    for i in range(3):
            for j in range(3): 
                  self.tk.buttons =[i][j]=tk.Button(
                  self.root() ,
                    text="",
                    font=("helvetica",20),
                    width=5,
                    height=2,
                    command=lambda row=i,col=j:
                    self.make_move(row,col)
            )
                  self.tk.buttons[i][j].grid(row=i,column=j)
    def make_move(self,row,col):
                if self.board[row][col]=="":
                    self.board[row][col]=self.current_player
                    self.buttons[row][col] .conf(text=self.current_player)    
                    if self.check_winner():
                         messagebox.showinfo("Game over",f"player{self.current_player}wins!")
                    self.reset_game() 
                elif self.check_draw():
                         messagebox.showinfo("game over","it's draw!") 
                         self.reset_game() 
                else:
                        self.switch_players() 

                def check_winner(self):
                         for i in range(3):
                              if self.boar[i][0]==self.board[i][1]==self.board[i][2]!="":
                                   return True
                         for j in range(3):
                              if self.board[0][0]==self.board[1][j]==self.board[2][j]!="":
                                   return True
                              if self.board[0][0]==self.board[1][1] ==self.board[2][2]!="":
                                    return True
                              if self.board[0][2]==self.board[1][1]==self.board[2][0]!="":
                                    return True
                         return False
                def check_draw(self):
                      for row in self.board:
                            if ""in row:
                                  return False
                            return True
                      def switch_players(self):
                            self.current_player="O"
                            if self.current_player=="X":
                             #else : "X"
                               
                                def reset_game(self) :
                                    self.current_player="X" 
                            self.board=[ 
                                  ["" for _ in range (3)] for _ in range(3)
                                  ]
                            for i in range (3):
                                  for i in range(3):
                                        self.buttons[i][j].config(text="")
                            def run(self):
                                  self.root.mainloop()
                            if __name__ =="__main __":
                             game=jeux()
                             game.run()
            
                          


                                  
                    


                         
                                    
                                        
                         
                                                                               