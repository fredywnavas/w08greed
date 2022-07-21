import pyray


class VideoService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    def __init__(self, caption, width, height, cell_size, frame_rate, debug = False):
        """Constructs a new VideoService using the specified debug mode.
        
        Args:
            debug (bool): whether or not to draw in debug mode.
        """
        self._caption = caption
        self._width = width
        self._height = height
        self._cell_size = cell_size
        self._frame_rate = frame_rate
        self._debug = debug

    def close_window(self):
        """Closes the window and releases all computing resources."""
        pyray.close_window()

    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()
    
    def draw_game_object(self, game_object):
        """Draws the given game_object's text on the screen.
        Args:
            game_object (game_object): The game_object to draw.
        """ 
        text = game_object.get_text()
        x = game_object.get_position().get_x()
        y = game_object.get_position().get_y()
        font_size = game_object.get_font_size()
        color = game_object.get_color().to_tuple()
        pyray.draw_text(text, x, y, font_size, color)
        
    def draw_game_objects(self, game_objects):
        """Draws the text for the given list of game_objects on the screen.
        Args:
            game_objects (list): A list of game_objects to draw.
        """ 
        for game_object in game_objects:
            self.draw_game_object(game_object)
    
    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """ 
        pyray.end_drawing()

    def get_cell_size(self):
        """Gets the video screen's cell size.
        
        Returns:
            Grid: The video screen's cell size.
        """
        return self._cell_size

    def get_height(self):
        """Gets the video screen's height.
        
        Returns:
            Grid: The video screen's height.
        """
        return self._height

    def get_width(self):
        """Gets the video screen's width.
        
        Returns:
            Grid: The video screen's width.
        """
        return self._width

    def is_window_open(self):
        """Whether or not the window was closed by the user.
        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        return not pyray.window_should_close()

    def open_window(self):
        """Opens a new window with the provided title.
        Args:
            title (string): The title of the window.
        """
        pyray.init_window(self._width, self._height, self._caption)
        pyray.set_target_fps(self._frame_rate)

    def _draw_grid(self):
        """Draws a grid on the screen."""
        for y in range(0, self._height, self._cell_size):
            pyray.draw_line(0, y, self._width, y, pyray.GRAY)
        for x in range(0, self._width, self._cell_size):
            pyray.draw_line(x, 0, x, self._height, pyray.GRAY)