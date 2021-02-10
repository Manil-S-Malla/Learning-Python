import Game
import Players

player1 = Players.HumanPlayer(True)
player2 = Players.ComputerPlayer(False, 'Player2')
game = Game.Game(player1, player2)
game.play()
