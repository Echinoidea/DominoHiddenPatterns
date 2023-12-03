from typing import Dict

from tile import Tile
from deck import Deck
from enums.orientations import Orientation

class Snake:
    
    def __init__(self):
        self.snake = {}  # A dictionary of where the pair with key 0 is the 'center', < 0 is left, > 0 is right

    
    def getStartPiece(self, deck: Deck):
        self.snake[0] = deck.getRandomPair()
    
    
    def getEndKey(self, side: Orientation) -> int:
        """Return the leftmost or rightmost key in the snake dict.

        Args:
            side (Orientation): Which end of the snake to return its key.

        Returns:
            int: The key of the leftmost or rightmost item in the snake dict.
        """
        assert side in [Orientation.LEFT, Orientation.RIGHT], 'Side to get end tile must be LEFT or RIGHT'
        
        if side is Orientation.LEFT:
            return min(iter(self.snake.keys()))
        elif side is Orientation.RIGHT:
            return max(iter(self.snake.keys()))
        
    
    def getEndTile(self, side: Orientation) -> Tile:
        """Return the leftmost or rightmost value in the snake dict.

        Args:
            side (Orientation): Which end of the snake to return its value (Tile).

        Returns:
            Tile: The Tile contained within the leftmost or rightmost item in the snake dict.
        """
        assert side in [Orientation.LEFT, Orientation.RIGHT], 'Side to get end tile must be LEFT or RIGHT'
        
        if side is Orientation.LEFT:
            minKey = min(iter(self.snake.keys()))
            return self.snake[minKey]
        elif side is Orientation.RIGHT:
            maxKey = max(iter(self.snake.keys()))
            return self.snake[maxKey]

    
    def snakeContentDebug(self) -> str:
        """Print the content of the snake dict in a readable way.
        
        Returns:
            str: Readable, formatted content of the snake dict.
        """
        items = []
        for k, v in self.snake.items():
            items.append('{} : {}'.format(k, v))
        
        return items
    
    
    def addTile(self, tile: Tile, side: Orientation):
        """Add a tile to the left or right side of the snake.

        Args:
            tile (Tile): The Tile instance to add to the snake.
            side (Orientation): The side of the snake to add to. Left or right.
        """
        assert side in [Orientation.LEFT, Orientation.RIGHT], 'Side to add Tile to must be LEFT or RIGHT'
        
        if side is Orientation.LEFT:
            # Check which pip of new tile matches the pip1 of the leftmost tile and change new tile orientation accordingly
            if tile.pip1 == self.getEndTile(Orientation.LEFT).pip2:
                tile.orientation = Orientation.LEFT
            else:
                tile.orientation = Orientation.RIGHT
            
            self.snake[self.getEndKey(Orientation.LEFT) - 1] = tile
        else:
            if tile.pip1 == self.getEndTile(Orientation.RIGHT).pip2:
                tile.orientation = Orientation.LEFT
            else:
                tile.orientation = Orientation.RIGHT
            
            self.snake[self.getEndKey(Orientation.RIGHT) + 1] = tile

        self.snake = dict(sorted(self.snake.items()))


s = Snake()
d = Deck()
# s.snake[-1] = Tile(1, 2)
s.snake[0] = Tile(2, 2)
# s.snake[1] = Tile(3, 4)
print(s.getEndTile(Orientation.LEFT))

print(s.getEndTile(Orientation.RIGHT))
s.addTile(Tile(1, 3), Orientation.RIGHT )
print(s.snakeContentDebug())