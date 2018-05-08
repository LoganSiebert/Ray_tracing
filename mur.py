from math import *
from constantes import UO, OMEGA

class Mur(object):
    
    def __init__(self, e, bord1, bord2, eps, sig):    #mur : type epaisseur bord1 bord2 epsilon sigma
        self._bord1 = bord1
        self._bord2 = bord2
        self._epsilon = eps 
        self._sigma = sig
        self._epaisseur = e
        self._alpha = OMEGA * sqrt((UO*eps)/2) * sqrt(sqrt(1+pow(sig/(OMEGA*eps),2))-1)
        self._beta = OMEGA * sqrt((UO*eps)/2) * sqrt(sqrt(1+pow(sig/(OMEGA*eps),2))+1)

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @property
    def epaisseur(self):
        return self._epaisseur
    @property
    def bord1(self):
        return self._bord1
    @property
    def bord2(self):
        return self._bord2
    @property
    def epsilon(self):
        return self._epsilon
    @property
    def sigma(self):
        return self._sigma
    @property
    def alpha(self):
        return self._alpha
    @property
    def beta(self):
        return self._beta

    def get_xmin(self):
        return min(self.bord1.x, self.bord2.x)

    def get_xmax(self):
        return max(self.bord1.x, self.bord2.x)

    def get_ymin(self):
        return min(self.bord1.y, self.bord2.y)

    def get_ymax(self):
        return max(self.bord1.y, self.bord2.y)

    def is_horizontal(self):
        res = False
        if(self.bord1.y== self.bord2.y):
            res = True
        return res
    
    def is_different(self, other):
        res = True
        if((self.bord1.x ==other.bord1.x ) and (self.bord2.x ==other.bord2.x ) and (self.bord1.y ==other.bord1.y ) and (self.bord2.y ==other.bord2.y)):
            res = False
        return res
