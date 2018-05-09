from mur import *
from point import *
from math import *

#Méthode des images

def image(point_initial, murs):
    #renvoie une liste de liste avec les points images et les murs correspodant
    liste=[]
    for mur in murs:
        if(mur.is_horizontal()):
            image= Point(point_initial.x, 2*mur.bord1.y - point_initial.y)
            liste.append(image, mur])
        else:
            angle_mur= (mur.bord1.y - mur.bord2.y)/(mur.bord1.x - mur.bord2.x)
            image = Point(point_initial.x*cos(angle_mur),(2*mur.bord1.y - point_initial.y)*cos(angle_mur))
            liste.append([image, mur])
    return liste
            
