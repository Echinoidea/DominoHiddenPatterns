class DeckEmptyException(Exception):
    """The Deck is empty and cannot be drawn from."""
    
    def __init__(self, message='The Deck is empty and cannot be drawn from.'):
        super(DeckEmptyException, self).__init__(message)


class HandEmptyException(Exception):
    """This Player's hand is empty."""
    
    def __init__(self, message="This Player's hand is empty."):
        super(HandEmptyException, self).__init__(message)


class NoCompatibleTilesException(Exception):
    """There are no pips on the Snake endpoints that match those of the new Tile."""
    
    def __init__(self, message='There are no pips on the Snake endpoints that match those of the new Tile.'):
        super(NoCompatibleTilesException, self).__init__(message)
