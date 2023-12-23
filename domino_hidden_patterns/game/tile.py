from enums.orientations import Orientation

class Tile:
    
    def __init__(self, pip1: int, pip2: int):
        self.pip1 = pip1    
        self.pip2 = pip2
        
        # self.Orientation: Orientation
        # self.Orientation = None
        
        self.Orientation = Orientation.LEFT
    
    
    def rotate(self, targetOrientation: Orientation):
        """'Rotate' this Tile by swapping the values of pip1 and pip2 and the orientation.

        Args:
            targetOrientation (Orientation): LEFT or RIGHT. Orientation is determined by the position
            of pip1. E.g. Orientation.LEFT means pip1 is on the LEFT.
        """
        
        if self.Orientation == targetOrientation:
            print("Cannot rotate Tile. Tile's orientation is already {}".format(targetOrientation.__str__()))
            return
        
        pip1 = self.pip1
        pip2 = self.pip2
        self.pip1 = pip2
        self.pip2 = pip1
        
        # self.Orientation = Orientation.LEFT if self.Orientation is not Orientation.LEFT else Orientation.RIGHT
        
        if self.Orientation == Orientation.LEFT:
            self.Orientation = Orientation.RIGHT
        elif self.Orientation == Orientation.RIGHT:
            self.Orientation = Orientation.LEFT

    
    def __str__(self):
        return '[{}, {}]'.format(self.pip1, self.pip2)
    
    
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