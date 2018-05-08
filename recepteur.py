from math import *
from const import *

class Recepteur(object):

#antenne receptrice, definie par sa position, sa hauteur equivalente, sa resistance
#et son orientation dans le cas d'une antenne a rayonnement non-omnidirectionnel (par defaut 0 rad)

    def __init__(self,x,y,ra=50,orientation=0):
        self._x = x
        self._y = y
        self._ra = ra
        self._orientation = orientation

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def resistance(self):
        return self._ra
    
    def get_hauteur_equivalente(self,theta=pi/2):
        #En 2D theta est toujours egal a 90 degres
        return -WAVELENGTH/pi*cos(pi/2*cos(theta))/(sin(theta)**2)

    def set_x(self,x):
        self._x = x

    def set_y(self,y):
        self._y = y
