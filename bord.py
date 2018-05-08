class Bord():

    def __init__(self,x,y):
        self._x =x
        self._y = y
        self._murs = []

    @property
    def murs_associes(self):
        return self._murs

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def add_mur(self,mur):
        self._murs.append(mur)
