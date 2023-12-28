from typing import Dict

from tile import Tile
from deck import Deck
from enums.orientations import Orientation
from exceptions.gameExceptions import NoCompatibleTilesException

class Snake:
    
    def __init__(self):
        self.snake = {}  # A dictionary of where the pair with key 0 is the 'center', < 0 is left, > 0 is right

    
    def setStartPiece(self, deck: Deck):
        """Draw a random Tile from the Deck to play at index 0 at the start of a game.

        Args:
            deck (Deck): The Deck to draw from.
        """
        
        self.snake[0] = deck.drawRandomTile()
    
    
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
            minKey = min(iter(self.snake.keys()), default=0)
            return self.snake[minKey]
        elif side is Orientation.RIGHT:
            maxKey = max(iter(self.snake.keys()), default=0)
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
    
    
    def printSnakeItems(self):
        """Neatly print the items of the snake dict.
        """
        
        items = []
        
        for _, v in self.snake.items():
            items.append('{}'.format(v))
        
        print(' '.join(items))
    
    
    def canAddTileLeft(self, tile: Tile) -> bool:
        """Check if either pip of the given Tile matches the left endpoint of this Snake. 

        Args:
            tile (Tile): The Tile to check if it can be added to the left endpoint.

        Returns:
            bool: True if tile.pip1 or tile.pip2 == left endpoint pip1
        """
        
        lhsPip = self.getEndTile(Orientation.LEFT).pip1
        
        return tile.pip1 == lhsPip or tile.pip2 == lhsPip
    
    
    def canAddTileRight(self, tile: Tile) -> bool:
        """Check if either pip of the given Tile matches the right endpoint of this Snake. 

        Args:
            tile (Tile): The Tile to check if it can be added to the right endpoint.

        Returns:
            bool: True if tile.pip1 or tile.pip2 == right endpoint pip2
        """
        
        rhsPip = self.getEndTile(Orientation.RIGHT).pip2
        
        return tile.pip1 == rhsPip or tile.pip2 == rhsPip
    
    
    def canAddTile(self, tile: Tile) -> bool:
        """Check if the given Tile matches either endpoint of this Snake.

        Args:
            tile (Tile): The Tile to check if it can be added to this Snake.

        Returns:
            bool: True if one of the pips of tile matches either endpoint of this Snake.
        """
        
        return self.canAddTileLeft(tile) or self.canAddTileRight(tile)
    
    
    def addTile(self, tile: Tile, side: Orientation):
        """Add a tile to the left or right side of the snake.

        Args:
            tile (Tile): The Tile instance to add to the snake.
            side (Orientation): The side of the snake to add to. Left or right.
        """
        
        assert side in [Orientation.LEFT, Orientation.RIGHT], 'Side to add Tile to must be LEFT or RIGHT'
        
        lhsPip = self.getEndTile(Orientation.LEFT).pip1
        rhsPip = self.getEndTile(Orientation.RIGHT).pip2
        
        
        try:
            if not self.canAddTile(tile):
                raise NoCompatibleTilesException
        except NoCompatibleTilesException as e:
            print(e.args)
            return
        
        if side is Orientation.LEFT:
            # Check which pip of new tile matches the pip1 of the leftmost tile and change new tile orientation accordingly
            if tile.pip1 == lhsPip:
                tile.rotate(Orientation.RIGHT)
            elif tile.pip2 == lhsPip:
                tile.rotate(Orientation.LEFT)
            else:
                print("Tile {} cannot match the leftmost tile's pips.".format(tile))
                return
            
            self.snake[self.getEndKey(Orientation.LEFT) - 1] = tile
        else:
            if tile.pip1 == rhsPip:
                tile.rotate(Orientation.LEFT)
            elif tile.pip2 == rhsPip:
                tile.rotate(Orientation.RIGHT)
            else:
                print("Tile {} cannot match the rightmost tile's pips.".format(tile))
                return
                
            self.snake[self.getEndKey(Orientation.RIGHT) + 1] = tile

        self.snake = dict(sorted(self.snake.items()))

