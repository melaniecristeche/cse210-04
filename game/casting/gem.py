from game.casting.actor import Actor


class Gem(Actor):
    """
    a pretty shiny gem, you better collect lots of these
    
    The responsibility of the gem is to be the treasure to collect.

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