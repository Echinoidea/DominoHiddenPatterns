from game import Game
from player import Player
from deck import Deck
from snake import Snake

class UserGame:
    """This class is sloppy but this class is only intended for development use.
    """
    
    def __init__(self):
        self.game = Game()
        
    
    def userPrintTurn(self, player: Player):
        print("--------\nPlayer {}'s turn\nHand: ".format(self.game.turn), end='')
        player.printHand()
        print("\nSnake:\n--------")
        print(self.game.snake.snakeContentDebug())
        print("--------\n")
    
    
    def userInputTurn(self, player: Player):
        userMove = input("Select tile in hand to place and which side of the snake to place it on e.g. [1,3];left\n> ")
        userMove = userMove.split(';')
        userMove = (int(userMove[0][1]), int(userMove[0][3]), userMove[1])
        
        # Check if this tile can be added, if not ask again.
        # If can be added, add to snake on side
        # Check if win
        # If win, do score calculation
        



ug = UserGame()
ug.userPrintTurn(ug.game.player1)
ug.userInputTurn(ug.game.player1)