from game.casting.actor import Actor


class FallingArtifact(Actor):
    """
    
    The responsibility of an FallingArtifact is to provide a dealer of the points of a GameObject
    Attributes:
        _points (int): current points of the artifact
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        
    def get_points(self):
        """
        Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._points
    
    def set_points(self, points):
        """
        Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._points = points