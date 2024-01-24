from player import Player
from deck import Deck
from game import Game
from encoder import Encoder
from tile import Tile
from enums.orientations import Orientation


class Computer:
    
    def __init__(self, player: Player, game: Game):
        self.player = player
        self.game = game
    
    
    def getFirstPlayableTile(self):
        for tile in self.player.hand:
            if self.game.snake.canAddTileLeft(tile):
                print(f"Can add {tile} to snake left")
                return tile, Orientation.LEFT
            elif self.game.snake.canAddTileRight(tile):
                print(f"Can add {tile} to snake right")
                return tile, Orientation.RIGHT
            else:
                continue

        