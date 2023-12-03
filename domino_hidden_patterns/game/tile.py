from enums.orientations import Orientation

class Tile:
    
    def __init__(self, pip1: int, pip2: int):
        self.pip1 = pip1    
        self.pip2 = pip2
    
    
    def __str__(self):
        return 'Tile[{}, {}]'.format(self.pip1, self.pip2)
    
    
    def __eq__(self, __value: object) -> bool:
        """Equality operator overload for Tile comparison. Checks the values of pip1 and pip2.

        Args:
            __value (object): The other Tile to compare.

        Returns:
            bool: Returns True if pip1 == pother.pip1 and pip2 == other.pip2 or pip1 == other.pip2 and pip2 == other.pip1
        """
        return self.pip1 == __value.pip1 and self.pip2 == __value.pip2 or self.pip1 == __value.pip2 and self.pip2 == __value.pip1
    

# t1 = Tile(5, 1, Orientation.LEFT)
# t2 = Tile(1, 5, Orientation.LEFT)
# t3 = Tile(1, 5, Orientation.LEFT)
# t4 = Tile(1, 2, Orientation.LEFT)

# print(t1 == t4)