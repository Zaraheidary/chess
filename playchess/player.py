class Player:
    """
    Represents a player by the flags he chose in the game

    Attributes:
        flags (list): A list of flagged cells 

    Methods: 
          add_flag and remove_flag  
    """

    def __init__(self):
        """
        Initialize the player with an empty list of flags (tuples)
        """
        self.flags = []

    def add_flag(self, cell):
        """
        Add a flag to the list of flagged cells

        Args:
            cell (tuple or str): The cell coordinates (column, row)            
        """
        self.flags.append(cell)

    def remove_flag(self, cell):
        """
        Remove a flag from the list of flagged cells

        Args:
            cell (tuple or str): The cell coordinates (column, row)
        """
        self.flags.remove(cell)
