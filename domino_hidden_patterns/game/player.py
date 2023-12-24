from tile import Tile
from deck import Deck
from exceptions.gameExceptions import DeckEmptyException

from typing import List

class Player:
    
    def __init__(self, deck: Deck, id: int):
        self.id = id
        self.deck = deck
        self.hand = self.initialDrawFromDeck(7)  # Change this to be 7 if two players, 5 if more than 2 players
        self.points = 0
    
    
    def printHand(self):
        print([i.__str__() for i in self.hand])
    
    
    def initialDrawFromDeck(self, count: int) -> List[Tile]:
        """Draw 'count' Tiles from the deck. This function is called at the start of a game for each player.

        Args:
            count (int): The number of Tiles to draw from the Deck.

        Returns:
            List[Tile]: List containing 'count' drawn Tiles from the Deck. 
        """
        
        hand = []
        for i in range(count):
            hand.append(self.deck.drawRandomTile())
        
        return hand
    
    
    def drawFromDeck(self):
        """Draw a Tile from the Deck and append it to this Player's hand.
        """

        try:
            if self.deck.isDeckEmpty():
                raise DeckEmptyException
        except DeckEmptyException as e:
            print(e.args)
            return
        
        drawnTile = self.deck.drawRandomTile()
        
        self.hand.append(drawnTile)
        
    
    def removeTileFromHand(self, tile: Tile):
        """Remove a Tile from this Player's hand.

        Args:
            tile (Tile): The Tile to remove.
        """
        
        try:
            self.hand.remove(tile)
        except ValueError as e:
            print("That Tile is not in this hand.")
    
    
    def isHandEmpty(self) -> bool:
        """Is this Player's hand empty

        Returns:
            bool: True if the number of Tiles in Player.hand <= 0
        """
        
        return len(self.hand) <= 0
    
    
    def countTilesInHand(self) -> int:
        """Return the number of Tiles in this Player's hand.

        Returns:
            int: Length of Player.hand
        """
        
        return len(self.hand)
    
    
    def countPipsInHand(self) -> int:
        """Count and return the total number of pips among the Tiles in this Player's hand.
        Used for score calculation at the end of a round.

        Returns:
            int: The total number of pips in this Player's hand.
        """
        
        if len(self.hand) <= 0:
            return 0
        
        total = 0
        
        t: Tile
        for t in self.hand:
            total += t.pip1 + t.pip2
        
        return total
    
    
    def __eq__(self, __value: object) -> bool:
        return self.id == __value.id
    
