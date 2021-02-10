import random


class Player:
    def __init__(self, x, name):
        if(x == True):
            self.mark = 'X'
        else:
            self.mark = 'O'
        
        self.winner = None
        self.moves_made = 0
        self.name = name

    def make_move(self, move):
        self.new_move = move
        if(self.moves_made < 5):
            self.moves_made += 1


class HumanPlayer(Player):
    def __init__(self, x, name= 'Player1'):
        super().__init__(x, name)

    def make_move(self):
        move = int(input('Make move : '))
        super().make_move(move)
        

class ComputerPlayer(Player):
    def __init__(self, x, name= 'Player2'):
        super().__init__(x, name)

    def make_move(self):
        move = random.randint(0,8)
        super().make_move(move)
        
