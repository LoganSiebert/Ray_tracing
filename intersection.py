from mur import*
from point import*

def intersection(p1,p2,murs):
    #Renvoie une liste de points d'intersections du segment defini par les points p1 et p2 et une liste de murs
     ptintersects=[]
     if((p2.x-p1.x !=0) and (p2.y-p1.y !=0)):
         direction = (p2.y-p1.y)/(p2.x-p1.x) #angle
         for mur in murs :
            if (mur.is_horizontal()): 
                if((mur.bord1[1]>p2.y and mur.bord1[1]<p1.y) or(mur.bord1[1]<p2.y and mur.bord1[1]>p1.y) ):
                    ptx= (mur.bord1[1]-p1.y)/direction + p1.x
                    if (mur.get_xmin() <= ptx <= mur.get_xmax()):
                         p = Point(ptx ,mur.bord1[1])
                         Point.set_mur(p, mur)
                         p.set_direction(direction)
                         ptintersects.append(p)
                else:
                    if (mur.bord1[0]>p2.x and mur.bord1[0]<p1.x) or (mur.bord1[0]<p2.x and mur.bord1[0]>p1.x):
                        pty =(mur.bord1[0]-p1.x)*direction + p1.y
                        if (mur.get_ymin() <= pty <= mur.get_ymax()):
                            p = Point(mur.bord1[0], pty)
                            p.set_mur(mur)
                            ptintersects.append(p)
     elif(p2.x== p1.x):
        for mur in murs :
            if (mur.is_horizontal()): 
                if((mur.bord1[1]>p2.y and mur.bord1[1]<p1.y) or(mur.bord1[1]<p2.y and mur.bord1[1]>p1.y) ):
                    p = Point(p1.x ,mur.bord1[1])
                    Point.set_mur(p,mur)
                    ptintersects.append(p)
     elif(p2.y==p1.y):
        for mur in murs :
            if (mur.is_horizontal()==False):
                if((mur.bord1[0]>p2.x and mur.bord1[0]<p1.x) or(mur.bord1[0]<p2.x and mur.bord1[0]>p1.x) ):
                    p = Point(mur.bord1[0],p1.y)
                    Point.set_mur(p,mur)
                    ptintersects.append(p)           
     return(ptintersects)
