from point import Point
from intersection import*

class Rayon(object):

    def __init__(self, start_point):
        self.points_principaux = [] #les points principaux contiennent aussi les points de reflexion
        self.points_reflexions = [] #Les points de reflexion est une "sous-liste"
        self.points_transmission = [] #transmission
        self.points_principaux.append(start_point) #Point de depart par defaut comme premier point principal

    @property
    def start_point(self):
        return self.points_principaux[0]

    @property
    def end_point(self):
        return self.points_principaux[-1]

    def add_point_principal(self, point):   #ajouter un point d'extremite
        self.points_principaux.append(point)

    def add_point_reflexion(self, point):       #ajouter un point de reflexion
        self.points_reflexions.append(point)
        self.add_point_principal(point)

    def add_points_principaux(self, point):     #ajouter une liste de points de reflexion
        self.points_principaux.extend(point)
    
    def get_points_principaux(self):
        return self.points_principaux

    def get_points_reflexions(self):
        return self.points_reflexions

    def add_point_transmission(self, point):   #ajouter un point de transmission
        self.points_transmission.append(point)

    def add_points_transmission(self, point): #ajouter une liste de points de transmission
        self.points_transmission.extend(point)
    
    def get_points_transmission(self):
        return self.points_transmission

    def find_all_intersections(self,murs):
        #Fonction etablissant la liste de tous les points d'intersection (de transmission) d'un rayon, avec une liste de murs exceptions
        new_points = []       
        for i in range(0,len(self.points_principaux)-1):
            p1 = self.points_principaux[i]
            p2 = self.points_principaux[i+1]
            if p1.x == p2.x: #pente infinie
                direction = None
            else:
                direction = (p2.y-p1.y)/(p2.x-p1.x) #angle
            intersections=intersection(p1,p2,murs)
            for inter in intersections:
                    inter.set_interaction_type("t")
                    inter.set_direction(direction)
                    new_points.append(inter)       
        self.add_points_transmission(new_points)

