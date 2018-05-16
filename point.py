class Point(object):

#Point par lequel passe un rayon.

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.mur = None
        self._interaction_type = "" # t ou r pour transmission ou reflexion, rien par defaut
        self._coefficient_value = 1
        self._rayon_direction = 0 #Si c'est un point de transmission, on y stocke l'angle du rayon qui le traverse
    
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def interaction_type(self):
        return self._interaction_type

    @property
    def coefficient_value(self):
        return self._coefficient_value

    @property
    def direction(self):
        return self._rayon_direction

    def set_direction(self,val):
        self._rayon_direction = val

    def set_coefficient_value(self,val):
        self._coefficient_value = val

    def set_interaction_type(self, interaction_type):
        self._interaction_type = interaction_type
        
    def set_mur(self, mur):
        self.mur = mur

