from deck import Deck
from tile import Tile
from enums.orientations import Orientation
from player import Player
from snake import Snake

from collections import namedtuple
from typing import NamedTuple

class Game:
    
    def __init__(self):
        self.deck = Deck()
        self.player1 = Player(self.deck, '1')
        self.player2 = Player(self.deck, '2')
        self.snake = Snake()
        self.snake.setStartPiece(self.deck)
        self.turn = 1
        self.scoreToWin = 40
    
    
    def getRoundWinner(self) -> NamedTuple:
        """Check if either Player has no Tiles left in their hand. If so, return a
        named tuple containing the winning Player obj and the total number of pips
        in the opponents hand for score calculation.

        Returns:
            NamedTuple: NamedTuple containing the winning Player and the total 
            number of pips in the opposing Player's hand.
        """
        
        winner = namedtuple("Winner", ['player', 'pointsToGain'])
        
        if self.player1.countTilesInHand <= 0:
            return winner(self.player1, self.player2.countPipsInHand())
        else:
            return winner(self.player2, self.player1.countPipsInHand())
        
        
    def getMatchWinner(self) -> Player:
        # if self
        pass
    
    
    def mustDraw(self, player: Player) -> bool:
        """Check if the Player's hand contains any Tiles that can match those on this
        Game's Snake.

        Args:
            player (Player): The Player who is attempting to place a Tile.

        Returns:
            bool: True if the Player has no available moves and must draw from the Deck.
        """
        
        for tile in player.hand:
            if self.snake.canAddTile(tile):
                return False
            else:
                continue
        
        return True

    
    
        
        
        
    
    


# deck = Deck()

# p1 = Player(deck, '0')
# p2 = Player(deck, '1')
# g = Game(p1, p2)

# # g.snake.getStartPiece(deck)
# g.snake.snake[0] = Tile(1, 2)
# p1.hand = [Tile(5, 3), Tile(3, 2)]
# print([i.__str__() for i in p1.hand])


# print(g.mustDraw(p1))

# g.userPrintTurn(p1)