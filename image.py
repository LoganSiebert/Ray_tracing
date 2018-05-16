from image import*
from rayon import*
from mur import*
from point import*
from math import*
from cmath import exp as cexp
from constantes import*
from interactions import*
from intersection import*

#Méthode des images

def image(point_initial, murs):
    #renvoie une liste de liste avec les points images et les murs correspodant
    liste=[]
    for mur in murs:
        if(mur.is_horizontal()):
            image= Point(point_initial.x, 2*mur.bord1[0] - point_initial.y)
            liste.append([image, mur])
        else:
            if((mur.bord1[0] !=mur.bord2[0]) & (mur.bord1[1] !=mur.bord2[1])):
                angle_mur= (mur.bord1[1] - mur.bord2[1])/(mur.bord1[0] - mur.bord2[0])
                image = Point(point_initial.x*cos(angle_mur),(2*mur.bord1[1] - point_initial[1])*cos(angle_mur))
                liste.append([image, mur])
    return liste

def rayon_direct(start_point,end_point, murs):
    #renvoie le rayon direct (dans une liste)
    list_rayon = []
    nouveau_rayon = Rayon(start_point)                        
    nouveau_rayon.add_point_principal(end_point)
    nouveau_rayon.find_all_intersections(murs)
    list_rayon.append(nouveau_rayon)
    return list_rayon


def rayons_reflechi(start_point,end_point, murs):
     #Renvoie la liste des rayons ayant effectue 1, 2 ou 3 reflexions entre start_point et end_point
     #par méthode des images
     list_rayons = []
     image_elems = image(start_point, murs)
     
     #1 réflexion
     for elem in image_elems:        
         mur_intersec =  [elem[1]] #Mur a tester avec la fonction intersection
         intersect_point =intersection(elem[0],end_point,mur_intersec)  #intersect_point est une liste de 1 element
         if(len(intersect_point)):
            new_ray = Rayon(start_point)
            intersect_point[0].set_interaction_type("r")
            #donne la direction incidente  par méthode des images
            new_ray.add_point_reflexion(intersect_point[0])
            new_ray.add_point_principal(end_point)
            new_ray.find_all_intersections(murs) #Intersection du rayon avec les murs pour la transmission
            list_rayons.append(new_ray)  
     
    #2 réflexions
     for elem in image_elems:
        #creation d'une liste de murs ne contenant par le mur du point image elem                       
         mur_intermediaire_ls = []
         for wall in murs:
             if (Mur.is_different(wall,elem[1])):
                 mur_intermediaire_ls.append(wall)       

         #on cherche les points images des points images par les AUTRES murs
         image_elems2 = image(start_point, mur_intermediaire_ls)       
         for elem2 in image_elems2:
             mur_intersec2 =  [elem2[1]] #une list de 1 elem avec le mur pour la deuxieme reflexion
             intersect_point2_2 = intersection(elem2[0],end_point,mur_intersec2) #point de deuxieme reflexion
             if(len(intersect_point2_2)):
                new_ray = Rayon(start_point)         
                intersect_point2_1 = intersection(elem[0],intersect_point2_2[0],[elem[1]]) #premier point de reflexion
                if(len(intersect_point2_1)):                   
                    intersect_point2_1[0].set_interaction_type("r")
                    intersect_point2_2[0].set_interaction_type("r") 
                    new_ray.add_point_reflexion(intersect_point2_1[0]) #1 ere reflexion
                    new_ray.add_point_reflexion(intersect_point2_2[0]) #2 eme reflexion
                    new_ray.add_point_principal(end_point)
                    new_ray.find_all_intersections(murs) #Points de transmission
                    list_rayons.append(new_ray)
                    
     #3 réflexions
     for elem in image_elems:
        #creation d'une liste de murs ne contenant par le mur du point image elem                       
         mur_intermediaire_ls = []
         mur_intermediaire2_ls = []
         for wall in murs:
             if (Mur.is_different(wall,elem[1])):
                 mur_intermediaire_ls.append(wall)       

         #on cherche les points images des points images par les AUTRES murs
         image_elems2 = image(start_point, mur_intermediaire_ls)       
         for elem2 in image_elems2:
             mur_intersec2 =  [elem2[1]] #une list de 1 elem avec le mur pour la deuxieme reflexion
             intersect_point2_2 = intersection(elem2[0],end_point,mur_intersec2) #point de deuxieme reflexion
             if(len(intersect_point2_2)):
                new_ray = Rayon(start_point)         
                intersect_point2_1 = intersection(elem[0],intersect_point2_2[0],[elem[1]]) #premier point de reflexion
                if(len(intersect_point2_1)):                   
                    intersect_point2_1[0].set_interaction_type("r")
                    intersect_point2_2[0].set_interaction_type("r") 
                    new_ray.add_point_reflexion(intersect_point2_1[0]) #1 ere reflexion
                    new_ray.add_point_reflexion(intersect_point2_2[0]) #2 eme reflexion
                    new_ray.add_point_principal(end_point)
                    new_ray.find_all_intersections(murs) #Points de transmission
                    list_rayons.append(new_ray)

             for wall in murs:
                 if (Mur.is_different(wall,elem2[1])):
                     mur_intermediaire2_ls.append(wall)       

             image_elems3 = image(start_point, mur_intermediaire2_ls)
             for elem3 in image_elems3:
                 mur_intersec3 =  [elem3[1]] #une list de 1 elem avec le mur pour la deuxieme reflexion
                 intersect_point3_3 = intersection(elem3[0],end_point,mur_intersec3)
                 if(len(intersect_point3_3)):
                        new_ray = Rayon(start_point)         
                        intersect_point3_2 = intersection(elem2[0],intersect_point3_3[0],[elem2[1]]) 
                        if(len(intersect_point3_2)):
                            intersect_point3_1 = intersection(elem[0],intersect_point3_2[0],[elem[1]])
                            if(len(intersect_point3_1)):
                                intersect_point3_3[0].set_interaction_type("r")
                                intersect_point3_2[0].set_interaction_type("r")
                                intersect_point3_1[0].set_interaction_type("r") 
                                new_ray.add_point_reflexion(intersect_point3_1[0]) #1 ere reflexion
                                new_ray.add_point_reflexion(intersect_point3_2[0]) #2 eme reflexion
                                new_ray.add_point_reflexion(intersect_point3_3[0]) #2 eme reflexion
                                new_ray.add_point_principal(end_point)
                                new_ray.find_all_intersections(murs) #Points de transmission
                                list_rayons.append(new_ray)

 


     return list_rayons

            
