import numpy as np
from os import system

def cls():
    system('cls')


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.winner = None
        self.moves_made = 0
        

    def display_board(self):
        for row in (self.board[i*3 : (i+1)*3] for i in range(3)):
            print('| ' + ' | '.join(row) + ' |')
        print('\n')
            

    def player_turn(self, player):
        print(f"{player.name}'s Turn : ")
        
        while True:
            player.make_move()
            move = player.new_move 

            if(self.board[move - 1] != ' '):
                print(player)
                print('Place Taken.')
            else:
                self.board[move - 1] = player.mark
                self.moves_made += 1
                break
       
    
    def row_check(self):
        for row in (self.board[i*3 : (i+1)*3] for i in range(3)):
            if( row[0] == row[1] == row[2] != ' '): 
                return [True, row[0]]

        return [False]

    
    def col_check(self):
        transposed = np.transpose(np.array(self.board).reshape(3,3)).reshape(1,9)[0]

        for col in (transposed[i*3 : (i+1)*3] for i in range(3)):
            if( col[0] == col[1] == col[2] != ' '): 
                return (True, col[0])

        return [False]

    
    def diag_check(self):
        array = np.array(self.board).reshape(3,3)
        primary_diagonal = []
        secondary_diagonal = []
        
        for i in range(3):
            primary_diagonal.append(array[i][i])
            secondary_diagonal.append(array[i][len(array) - 1 - i])
        
        if(primary_diagonal[0] == primary_diagonal[1] == primary_diagonal[2] != ' '):
            return [True, primary_diagonal[1]]
        elif(secondary_diagonal[0] == secondary_diagonal[1] == secondary_diagonal[2] != ' '):
            return [True, secondary_diagonal[1]]
        else:
            return [False]            


    def is_win(self):
        if(self.row_check()[0] == True):
            return self.row_check() 
        elif(self.col_check()[0] == True):
            return self.col_check() 
        elif(self.diag_check()[0] == True):
            return self.diag_check() 
        else:
            return [False]


    def play(self):
        while True:
            self.player_turn(self.player1)
            cls()
            self.display_board()
            
            if(self.is_win()[0] == True):
                print(f'{self.is_win()[1]} won.')
                break
            
            if(self.moves_made >= 9):
                break

            self.player_turn(self.player2)
            cls()
            self.display_board()
            
            if(self.is_win()[0] == True):
                print(f'{self.is_win()[1]} won.')
                break
            
            
            

            
