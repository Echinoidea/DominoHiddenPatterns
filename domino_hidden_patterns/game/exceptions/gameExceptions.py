class DeckEmptyException(Exception):
    """The Deck is empty and cannot be drawn from."""
    
    def __init__(self, message='The Deck is empty and cannot be drawn from.'):
<<<<<<< HEAD
        super(DeckEmptyException, self).__init__(message)


class HandEmptyException(Exception):
    """This Player's hand is empty."""
    
    def __init__(self, message="This Player's hand is empty."):
        super(DeckEmptyException, self).__init__(message)


class NoCompatibleTilesException(Exception):
    """There are no pips on the Snake endpoints that match those of the new Tile."""
    
    def __init__(self, message='There are no pips on the Snake endpoints that match those of the new Tile.'):
        super(DeckEmptyException, self).__init__(message)
=======
        super(DeckEmptyException, self).__init__(message)
>>>>>>> b9088d2f784a13f56dde60594e2b031814bbb9ee
