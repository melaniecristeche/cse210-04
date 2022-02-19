from game.casting.actor import Actor


class Rock(Actor):
    """
    ...its just a rock, please dont hit it
    
    The responsibility of a rock is to be a rock. it hurts when you hit it

    Attributes:
        
    """
    def __init__(self):
        super().__init__()
        self._message = ""
        
    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message