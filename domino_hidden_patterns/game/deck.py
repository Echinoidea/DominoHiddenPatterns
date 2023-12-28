from typing import Dict, List
from itertools import combinations_with_replacement
from random import shuffle, randint, choice

from tile import Tile
from enums.orientations import Orientation
from exceptions.gameExceptions import DeckEmptyException

class Deck:
    
    def __init__(self):
        self.deckOrigin = self.generateDeck()
        self.deck = self.deckOrigin
        
    
    def printDeckDebug(self):
        """Print the deck list in a readable fashion.
        """
        
        try:
            if self.isDeckEmpty():
                raise DeckEmptyException
        except DeckEmptyException as e:
            print(e.args)
        
        for tile in self.deck:
            print(tile.__str__(), end=', ')
            
    
    def isTileInDeck(self, tile: Tile) -> bool:
        """Get whether a Tile is in the deck list already or not.

        Args:
            tile (Tile): The Tile to check if there any duplicates of.

        Returns:
            bool: Returns True if a Tile with the same pip values are in the deck list, else False.
        """
        
        try:
            if self.isDeckEmpty():
                raise DeckEmptyException
        except DeckEmptyException as e:
            print(e.args)
        
        for t in self.deck:
            if t == tile:
                return True

        return False
    
    
    def generateDeck(self) -> List[Tile]:
        """Generate the starting Dominoes deck with 28 Tiles. May add a parameter to allow for larger decks.

        Returns:
            List[Tile]: The populated deck list of Tiles.
        """
        
        tiles = []
        pipPairs = list(combinations_with_replacement(range(0, 7), 2))
        
        for pair in pipPairs:
            tiles.append(Tile(pair[0], pair[1]))
        
        return tiles
    

    def shuffleDeck(self) -> List[Tile]:
        """Shuffle the deck list.

        Returns:
            List[Tile]: The shuffled deck dict.
        """
        
        try:
            if self.isDeckEmpty():
                raise DeckEmptyException
        except DeckEmptyException as e:
            print(e.args)
        
        return shuffle(self.deck)
    
    
    def isDeckEmpty(self) -> bool:
        """Check if the deck list is empty or not.

        Returns:
            bool: True if the deck list is empty. Else, False.
        """
        
        return len(self.deck) <= 0
    
    
    def deleteTileByIndex(self, index: int):
        """Delete a Tile by index in the deck list if the key exists.

        Args:
            index (int): The index of the list to delete.
        """
        
        try:
            self.deck.pop(index)
        except KeyError as e:
            print("No such key: {}".format(e.args))
    
    
    def getRandomTile(self) -> Tile:
        """Return a randomly selected Tile from the Deck list without affecting the Deck.

        Returns:
            Tile: A randomly selected Tile from the Deck list
        """
        
        try:
            if self.isDeckEmpty():
                raise DeckEmptyException
        except DeckEmptyException as e:
            print(e.args)
        
        randIndex = randint(0, len(self.deck) - 1)
        return self.deck[randIndex]
    
    
    def drawRandomTile(self) -> Tile:
        """Draws (returns and deletes) a randomly selected Tile from the deck list.

        Returns:
            Tile: The randomly selected Tile from the deck list.
        """
        
        try:
            if self.isDeckEmpty():
                raise DeckEmptyException
        except DeckEmptyException as e:
            print(e.args)
        
        return self.deck.pop(randint(0, len(self.deck) - 1))
        
