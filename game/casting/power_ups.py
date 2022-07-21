import random
class PowerUp:
    """
    Gives some extra incrrease to the points.
    """
    
    def __init__(self):
        self._factors = []
    
    def multiplier(self):

        self._factors = [.1, .3, .4, 2]

        factor_access = random.randint(1,100)
        
        #print(self._factors [factor_access])
        
        if factor_access == 37:
            print(factor_access)
            print('nice you get a double multiplier')
            return self._factors[3]
        
        elif factor_access <=10:
            print(factor_access)
            print('A 40 percent increase in score is good')
            return self._factors[2]
        
        elif factor_access >=80:
            print(factor_access)
            print('30 percent score increase is sweet')
            return self._factors[1]
        
        else:
            print(factor_access)
            print('10 percent increase is going to help.')
            return self._factors[0]
        
        
  