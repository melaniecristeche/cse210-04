from game.casting.actor import Actor


class Rock(Actor):
    """
    ...its just a rock, please dont hit it
    
    The responsibility of a rock is to be a rock. it hurts when you hit it

    Attributes:
        
    """
    def __init__(self):
        super().__init__()
        self._point=-10
        
    def get_point(self):
        """Gets the rocks current penalty score.
        
        Returns:
            string: current penalty
        """
        return self._points
    
    def set_point(self, penalty):
        """Updates the penalty value to the given one
        
        Args:
            penalty (int) the point value
        """
        self._point = penalty