class DeckEmptyException(Exception):
    """The Deck is empty and cannot be drawn from."""
    
    def __init__(self, message='The Deck is empty and cannot be drawn from.'):
        super(DeckEmptyException, self).__init__(message)