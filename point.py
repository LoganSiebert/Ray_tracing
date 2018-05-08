class Point(object):

#Objet point point par lequel passe un rayon. Il peut s'agir d'un point
#d'interaction du rayon avec l'environnement

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
    
    def find_mur(self, murs):
        #permet de verifier si le point se situe sur un mur de la liste murs
        c = None
        for mur in murs:
            if (self.mur.x1 == self.x and self.mur.x2 == self.x and ((self.y<=self.mur.get_ymax() and self.y>=self.mur.get_ymin()))) \
            or (self.mur.y1 == self.y and self.mur.y2 ==self.y and ((self.x<=self.mur.get_xmax() and self.x>=self.mur.get_xmin()))):
               c = mur
        return c
