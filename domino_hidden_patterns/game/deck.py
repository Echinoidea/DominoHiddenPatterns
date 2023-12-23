from typing import Dict, List
from itertools import combinations_with_replacement
from random import sample, randint, choice

from tile import Tile
from enums.orientations import Orientation

class Deck:
    
    def __init__(self):
        self.deckOrigin = self.generateDeck()
        self.deck = self.deckOrigin
        
    
    def printDeckDebug(self):
        """Print the deck dict in a readable fashion.
        """
        
        if self.isDeckEmpty():
            print("Trying to print deck: Deck is Empty")
        
        for i in range(len(self.deck)):
            try:
                print('{}: {}'.format(i, self.deck[i]))
            except KeyError:
                continue
            
    
    def isTileInDeck(self, tile: Tile) -> bool:
        """Get whether a Tile is in the deck dict already or not.

        Args:
            tile (Tile): The Tile to check if there any duplicates of.

        Returns:
            bool: Returns True if a Tile with the same pip values are in the deck dict, else False.
        """
        
        for t in self.deck.values():
            if t == tile:
                return True

        return False
    
    
    def generateDeck(self) -> Dict[int, Tile]:
        """Generate the starting Dominoes deck with 28 Tiles. May add a parameter to allow for larger decks.

        Returns:
            Dict[int, Tile]: The populated deck dict of Tiles.
        """
        
        keys = [i for i in range(0, 29)]
        tiles = []
        pipPairs = list(combinations_with_replacement(range(0, 7), 2))
        
        for pair in pipPairs:
            tiles.append(Tile(pair[0], pair[1]))
        
        return dict(zip(keys, tiles))
    

    def shuffleDeck(self) -> Dict[int, Tile]:
        """Shuffle the deck dict.

        Returns:
            Dict[int, Tile]: The shuffled deck dict.
        """
        return dict(zip(self.deck, sample(list(self.deck.values()), len(self.deck))))
    
    
    def isDeckEmpty(self) -> bool:
        """Check if the deck dict is empty or not.

        Returns:
            bool: True if the deck dict is empty. Else, False.
        """
        
        return len(self.deck) <= 0
    
    
    def deleteTile(self, key: int):
        """Delete a k,v pair in the deck dict if the key exists.

        Args:
            key (int): The key of the pair to delete.
        """
        
        try:
            del self.deck[key]
        except KeyError as e:
            print("No such key: {}".format(e.args))
    
    
    def getRandomPair(self) -> Tile:
        """Return a randomly selected k, v pair from the deck dict without affecting the deck.

        Returns:
            Tile: A randomly selected k, v pair from the deck dict.
        """
        
        randIndex = randint(0, len(self.deck) - 1)
        return self.deck[randIndex]
    
    
    def drawRandomPair(self) -> Tile:
        """Draws (returns and deletes) a randomly selected k, v pair from the deck dict.

        Returns:
            Tile: The randomly selected Tile from the deck dict.
        """
        
        randomKey, _ = choice(list(self.deck.items()))
        return self.deck.pop(randomKey, None)
        
    
    
    
    
    
        
# d = Deck()
# d.printDeckDebug()
# d.deck = d.shuffleDeck()
# d.printDeckDebug()
# # print(d.isTileInDeck(Tile(1,6,Orientation.LEFT)))
# for i in range(len(d.deck)):
#     print(d.deleteTile(i))
    
# d.printDeckDebug()
