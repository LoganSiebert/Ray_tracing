from point import Point

class Rayon(object):

    def __init__(self, start_point):
        self.points_principaux = [] #debut, fin. ATTENTION, les points principaux contiennent aussi les points de reflexion
        self.points_reflexions = [] #Les points de reflexion est seulement une "sous-liste"
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



    def find_all_intersections(self,murs,exception=[]):
        #Fonction etablissant la liste de tous les points d'intersection (de transmission) d'un rayon, avec une liste de murs exceptions
        new_points = []
        
        for i in range(0,len(self.points_principaux)-1):
            p1 = self.points_principaux[i]
            p2 = self.points_principaux[i+1]

            if p1.x == p2.x: #pente infinie
                direction = None
            else:
                direction = (p2.y-p1.y)/(p2.x-p1.x) #angle

            intersections = intersect(p1,p2,murs)
            for inter in intersections:
                if inter.mur not in exception:
                    inter.set_interaction_type("t")
                    inter.set_direction(direction)
                    new_points.append(inter)

        
        self.add_points_transmission(new_points)


    def intersect(p1,p2,murs):
    #Renvoie une liste de points d'intersections du segment defini par les points p1 et p2 et une liste de murs
    ptintersects = []
    if((p2.x-p1.x !=0) and (p2.y-p1.y !=0)):
        direction = (p2.y-p1.y)/(p2.x-p1.x) #angle
        for mur in murs :
            if (mur.is_horizontal()): 
                if((mur.bord1.y>p2.y and mur.bord1.y<p1.y) or(mur.bord1.y<p2.y and mur.bord1.y>p1.y) ):
                    ptx= (mur.bord1.y-p1.y)/direction + p1.x
                    if (mur.get_xmin() <= ptx <= mur.get_xmax()):
                        p = Point(ptx ,mur.bord1.y)
                        Point.set_mur(p, mur)
                        p.set_direction(direction)
                        ptintersects.append(p)
            else:
                if (mur.bord1.x>p2.x and mur.bord1.x<p1.x) or (mur.bord1.x<p2.x and mur.bord1.x>p1.x):
                    pty =(mur.bord1.x-p1.x)*direction + p1.y
                    if (mur.get_ymin() <= pty <= mur.get_ymax()):
                        p = Point(mur.bord1.x, pty)
                        p.set_mur(mur)
                        ptintersects.append(p)  

    elif(p2.x== p1.x):
        for mur in murs :
            if (mur.is_horizontal()): 
                if((mur.bord1.y>p2.y and mur.bord1.y<p1.y) or(mur.bord1.y<p2.y and mur.bord1.y>p1.y) ):
                    p = Point(p1.x ,mur.bord1.y)
                    Point.set_mur(p,mur)
                    ptintersects.append(p)
    elif(p2.y==p1.y):
        for mur in murs :
            if (mur.is_horizontal()==False):
                if((mur.bord1.x>p2.x and mur.bord1.x<p1.x) or(mur.bord1.x<p2.x and mur.bord1.x>p1.x) ): 
                    p = Point(mur.bord1.x,p1.y)
                    Point.set_mur(p,mur)
                    ptintersects.append(p)
    
    return(ptintersects)
