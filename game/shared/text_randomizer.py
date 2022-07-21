import random
from game.casting.power_ups import PowerUp
from game.casting.curses import Curses
from game.casting.randomizer import Randomizer

class Text_randomizer(Randomizer):
    
    def __init__(self):
        self._value = 0
        self._power = PowerUp()
        self._curse = Curses()
        self._mystery = Randomizer()
        
        

    def renamer(self):
        
        
        name_picker = random.randint(1,5)
        
        #print('the name picker number is.', name_picker) # debugging line
        
        if name_picker == 1:
            name = '*'
            self._value = 2
            return name 
        
        elif name_picker == 2:
            name = 'O'
            self._value = -1
            return name 
            
        elif name_picker == 3:
            name = 'm'
            self._value = self._power.multiplier()
            return name 
        
        elif name_picker == 4:
            name = 'c'
            self._value = self._curse.bad_mult()
            return name 
        
        elif name_picker == 5:
            name = 'r'
            self._value = self._mystery.mystery_box()
            return name 
        
        
    def value_setter(self):
        value = self._value
        
        return value
        