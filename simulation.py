from image import*
from rayon import*
from mur import*
from point import*
from math import*
from cmath import exp as cexp
from constantes import*
from interactions import*
from interface import*

def compute_power(width,height,emetteur,MURS):
    pmin,pmax = -93,-73 #le debit est max au dela de cette valeur
    dmin,dmax = 6, 54
    increment = (dmax-dmin)/(pmax-pmin)
    #Cette fonction permet de donner la puissance recue (en dBm) pour chaque metre carré
    powers = []
    bitrates =[]
    recepteur = (0,0)
    for i in range(0,int(width)): #Boucle principale sur tous les metres carres
        powers.append([])
        bitrates.append([])
        for j in range(0,int(height)):
            recepteur=(i+0.5,j+0.5)
            if(emetteur[0]!= recepteur[0] or emetteur[1] != recepteur[1]): #Détermination de tous les rayons
                RAYS_REFLEXION = rayons_reflechi(Point(emetteur[0],emetteur[1]),Point(recepteur[0],recepteur[1]), MURS)
                RAYS_DIRECT =  rayon_direct(Point(emetteur[0],emetteur[1]),Point(recepteur[0],recepteur[1]), MURS)               
                #Calcule tous les coefficients et le stocke dans chaque point du rayon associe 
                for ray in RAYS_DIRECT + RAYS_REFLEXION:
                    transmission_coefficient(ray) #Coefficient de transmission
                for ray in RAYS_REFLEXION:
                    reflexion_coefficient(ray) #Coefficient de reflexion
                all_rays = RAYS_DIRECT + RAYS_REFLEXION
                power = 0
                for ray in all_rays: #Calcul de la puissance
                       En = sqrt(60*POWER*GAIN)
                       d = 0
                       points_principaux = ray.get_points_principaux()
                       points_transmission = ray.get_points_transmission()
                       for k in range(len(points_principaux)):
                           point = points_principaux[k]
                           En = En*point.coefficient_value
                           if k>0:
                               point_previous = points_principaux[k-1]
                               d = d + sqrt((point_previous.x-point.x)**2 + (point_previous.y-point.y)**2) #calcul de la distance parcourrue par le rayon
                       for n in range(len(points_transmission)):
                           En = En * points_transmission[n].coefficient_value
                       power = power+ (HAUTEUR_EQ*En/d)**2
                       power = power/(8*Ra)
            print (10*log10(power/0.001))
            powers[i].append(10*log10(power/0.001)) #definition de dBm
            if 10*log10(power/0.001) <pmin:
                bitrates[i].append(dmin)
            elif 10*log10(power/0.001)>pmax:
                bitrates[i].append(dmax)
            else:
                bitrates[i].append((dmin + (10*log10(power/0.001)-pmin)*increment))                   
    draw_bitrate_map(MURS,width,height,emetteur,bitrates,recepteur)
    draw_power_map(MURS,width,height,emetteur,powers,recepteur)





