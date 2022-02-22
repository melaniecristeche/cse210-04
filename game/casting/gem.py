from game.casting.actor import Actor


class Gem(Actor):
    """
    a pretty shiny gem, you better collect lots of these
    
    The responsibility of the gem is to be the treasure to collect.

    Attributes:
        
    """
    def __init__(self):
        super().__init__()
        self._point=10
        
    def get_point(self):
        """Gets the gems current score.
        
        Returns:
            string: current value
        """
        return self._points
    
    def set_point(self, points):
        """Updates the point value to the given one
        
        Args:
            penalty (int) the point value
        """
        self._point = points