from math import *
from constantes import U0, OMEGA

class Mur(object):
    
    def __init__(self, e, bord1, bord2, eps, sig):
        #(matériau, epaisseur, bord1, bord2, permitivité, conductivité)
        self._bord1 = bord1
        self._bord2 = bord2
        self._epsilon = eps 
        self._sigma = sig
        self._epaisseur = e
        self._alpha = OMEGA * sqrt((U0*eps)/2) * sqrt(sqrt(1+pow(sig/(OMEGA*eps),2))-1)
        self._beta = OMEGA * sqrt((U0*eps)/2) * sqrt(sqrt(1+pow(sig/(OMEGA*eps),2))+1)

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
        return min(self.bord1[0], self.bord2[0])

    def get_xmax(self):
        return max(self.bord1[0], self.bord2[0])

    def get_ymin(self):
        return min(self.bord1[1], self.bord2[1])

    def get_ymax(self):
        return max(self.bord1[1], self.bord2[1])

    def is_horizontal(self):
        res = False
        if(self.bord1[1]== self.bord2[1]):
            res = True
        return res
    
    def is_different(self, other):
        res = True
        if((self.bord1[0] ==other.bord1[0] ) and (self.bord2[0] ==other.bord2[0] ) and (self.bord1[1] ==other.bord1[1] ) and (self.bord2[1] ==other.bord2[1])):
            res = False
        return res
