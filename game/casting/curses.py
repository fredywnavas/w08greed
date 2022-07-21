import random
from game.casting.power_ups import PowerUp


class Curses(PowerUp):
    """
    Decrease the points in some factor
    """
    def __init__(self):
        super().__init__()
    
    def bad_mult(self): 
        mult = super().multiplier()
        bad = (mult * - 1)
        print('this is curses class bad_mult method being activated.  The bad mult is', bad)
        
        return bad