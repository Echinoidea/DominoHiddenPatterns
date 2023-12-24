from enum import Enum, auto

class Orientation(Enum):
    """Represents the orientation of a tile based on pip1. E.g. pip1 is on the left side of a 
    horizontal tile, the orientation is LEFT.
    """
    
    UP = auto()
    RIGHT = auto()
    DOWN = auto()
    LEFT = auto()
    
    def __str__(self) -> str:
        return self.name
    