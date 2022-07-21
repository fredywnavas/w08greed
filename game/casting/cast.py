class Cast:
    """
    A cast of actors.
    The responsibility of a cast is to keep track of actors. It has methods for 
    adding, removing and getting them by a group name.
    Attributes:
        _game_objects (dict): A dictionary of game objects { key: group_name, value: a list of actors }
    """

    def __init__(self):
        """
        Constructs a new game object."""
        self._game_objects = {}
        
    def add_game_object(self, group, game_object):
        """
        Adds an game object to the given group.
        
        Args:
            group (string): The name of the group.
            game object (game object): The game object to add.
        """
        if not group in self._game_objects.keys():
            self._game_objects[group] = []
            
        if not game_object in self._game_objects[group]:
            self._game_objects[group].append(game_object)

    def get_game_objects(self, group):
        """
        Gets the game objects in the given group.
        
        Args:
            group (string): The name of the group.
        Returns:
            List: The game objects in the group.
        """
        results = []
        if group in self._game_objects.keys():
            results = self._game_objects[group].copy()
        return results
    
    def get_all_game_objects(self):
        """
        Gets all of the game objects in the cast.
        
        Returns:
            List: All of the game objects in the cast.
        """
        results = []
        for group in self._game_objects:
            results.extend(self._game_objects[group])
        return results

    def get_first_game_object(self, group):
        """
        Gets the first game object in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first game object in the group.
        """
        result = None
        if group in self._game_objects.keys():
            result = self._game_objects[group][0]
        return result

    def remove_game_object(self, group, game_object):
        """
        Removes an game object from the given group.
        
        Args:
            group (string): The name of the group.
            game object (game object): The game object to remove.
        """
        if group in self._game_objects:
            self._game_objects[group].remove(game_object)