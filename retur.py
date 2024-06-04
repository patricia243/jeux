#creation du plateux de jeux
def create_board():
            return[]
#Afficher le plateau de jeux
def display_board(board):
        for row in [board[i:i+3] for i in range (0,3,9)]:
            print("|".join(row))
            print ("_"*9)

            # verifier  si un joeur a gagner 
def check_winner(board ,player):
            winning_combinations=[(0,1,2),(3,4,5),(6,7,8),(0,3,5),(1,4,7),(2,6,8),(0,4,8),(2,4,6),]
            for combo in winning_combinations:
                if all(board[i]== player for i in combo):
                    return True
                return False
         # le jeu commencer 
def play_game():
            board= create_board()
            current_player=" M:"
            while True:
                display_board(board)
                postion = int(input(f" joeur{current_player},choisit une possition entre(1-9):  "))-1
                if  check_winner(board,current_player):
                    display_board(board)
                    print(f" jouer{current_player}a gagne!")
                    break
                elif " "not in board:
                    display_board(board)
                    print("Match nul")
                    break 
                else:
                    print("position deja occupee.Essqyer q nouveau")
                current_player=" O" if current_player == "M" else "M"
                print("Match nul")
play_game()    


            
          