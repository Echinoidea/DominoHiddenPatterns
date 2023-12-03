from tile import Tile
from deck import Deck

from typing import List

class Player:
    
    def __init__(self, deck: Deck):
        self.deck = deck
        self.hand = self.initialDrawFromDeck(7)  # Change this to be 7 if two players, 5 if more than 2 players
    
    
    def initialDrawFromDeck(self, count: int) -> List[Tile]:
        hand = []
        for i in range(count):
            hand.append(self.deck.drawRandomPair())
        
        return hand
    
    
    def drawFromDeck(self):
        if self.deck.isDeckEmpty:
            print("Attempted to draw from deck. Deck is empty.")
            return
        
        self.hand.append(self.deck.drawRandomPair())
    
    
    def removeTileFromHand(self, tile: Tile):
        try:
            self.hand.remove(tile)
        except ValueError as e:
            print("That Tile is not in this hand.")
    
    
    def countPipsInHand(self):
        if len(self.hand <= 0):
            return 0
        
        total = 0
        
        t: Tile
        for t in self.hand:
            total += t.pip1 + t.pip2
        
        return total
    
    
    
    
d = Deck()
p = Player(d)
p.hand.append(Tile(1, 7))
print([i.__str__() for i in p.hand])
p.removeTileFromHand(Tile(1, 3))
print([i.__str__() for i in p.hand])
