class Emetteur(object):
    
#antenne de la station de base, definie par sa position, sa puissance d'emission (par defaut 15dBm = 0.0056W)
#et son orientation dans le cas d'une antenne a rayonnement non-omnidirectionnel (par defaut 0 rad)

    def __init__(self,x,y,power=0.0056,orientation=0):
        self._x = x
        self._y = y
        self._power = power
        self._orientation = orientation

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def power(self):
        return self._power

    def get_gain(self,theta=0):
        #3.7dB par defaut
        return 2.34
        
    def set_x(self,x):
        self._x = x

    def set_y(self,y):
        self._y = y
    
