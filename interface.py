import matplotlib.pyplot as plot
from matplotlib import collections  as coll
import pylab as pl
from constantes import *
from mur import Mur
from bord import Bord
from emetteur import Emeteur
from recepteur import Recepteur
import numpy as np
from numpy.matrixlib import matrix


def decode_plan(filename):

    #Cette fonction permet de lire le plan et de renvoyer la liste de murs
    #ainsi que l'emetteur et le récepteur

    print("Decodage du plan",end='') 

    input = open(filename,'r')
    lines = input.readlines()
    input.close()

    murs = []
    tempbords = {}
    bord = []
    recepteur = []

    for line in lines:
        content = line.split(" ")

        #Les premieres lignes (dimensions, emetteur, recepteur)

        keyword = content[0]
        if keyword=="DIMENSIONS":
            width = float(content[1])
            height = float(content[2])
        elif keyword=="EMETTEUR":
            emmetteur = Emetteur(float(content[1]),float(content[2]))
        elif keyword=="RECEPTEUR":
            recepteur.append(Emmetteur(float(content[1]),float(content[2])))

        #Les murs et les bords
        elif keyword == "M":
            x1,y1,x2,y2 = float(content[3]),float(content[4]),float(content[5]),float(content[6])
            bord1 = tempbords.get((x1,y1),None) #Ces etapes permettent de ne pas generer de coins doubles
            bord2 = tempbords.get((x2,y2),None)
            if(bord1==None):
                bord1 = Bord(x1,y1)
                tempbords[(x1,y1)] = bord1
                bord.append(bord1)
            if(bord2==None):
                bord2 = Bord(x2,y2)
                tempbords[(x2,y2)] = bord2
                bord.append(bord2)

            eps = EPS_1
            sig = SIG_1
            materiau = content[1]
            if materiau=="2":
                eps = EPS_2
                sig = SIG_2
            elif materiau=="3":
                eps = EPS_3
                sig = SIG_3

            m = Mur(float(content[2]),bord1,bord2,eps,sig)
            bord1.add_mur(m)
            bord2.add_mur(m)
            murs.append(m)
    

    return [width,height,base,receivers,murs,coins]



def draw_main_stage(murs,width,height,TXx,TXy,fig,ax,recepteur=None):

    #Genere l'affichage de l'etage

    lines = []

    #Dessin des murs
    for mur in murs:
        p1=(mur.bord1.x,mur.bord1.y)
        p2=(mur.bord2.x,mur.bord2.y)
        seg = [p1,p2]
        lines.append(seg)

    wallLines = coll.LineCollection(lines)
    wallLines.set_color("white")
    wallLines.set_linewidth(2)    
    ax.add_collection(wallLines)

    ax.plot(TXx,TXy,"r1",markersize = 12)

    if recepteur != None:
        for rec in recepteur:
            ax.plot(rec.x, rec.y, "g1",markersize=12)

    fig.canvas.set_window_title("Ray Tracing Visualizer")
    ax.set_xlim(-1, width+1)
    ax.set_ylim(-1, height+1)
    ax.set_facecolor('black')


def draw_rays(murs, rays_reflexion, width, height, TXx, TXy, RXx, RXy):

    #Genere l'affichage des rayons

    print("\nAffichage des rayons...")

    fig, ax = plot.subplots()
    draw_main_stage(murs,width,height,TXx,TXy,fig,ax)  
    ray_lines = []
    ax.plot(RXx,RXy,"b1",markersize=12) #Emetteur

    #Dessin des rayons
    for ray in rays_reflexion:
        points_principaux = ray.get_points_principaux()
        points_transmission = ray.get_points_transmission()
        
        if(len(points_principaux)>=2):
            for i in range(0,len(points_principaux)-1):
                p1 = (points_principaux[i].x, points_principaux[i].y)
                p2 = (points_principaux[i+1].x, points_principaux[i+1].y)
                seg = [p1,p2]
                ray_lines.append(seg)
                if(i != 0):
                    ax.plot(p1[0], p1[1],"y+",markersize=10)

        if len(points_transmission)>0:
            for pt in points_transmission:
                ax.plot(pt.x, pt.y,"bo",markersize=4)

    ray_lines_collection = coll.LineCollection(ray_lines)
    ray_lines_collection.set_color("green")
    ray_lines_collection.set_linewidth(1)    
    ax.add_collection(ray_lines_collection)


def draw_power_map(MURS,width,height,base,powers_dbm,recepteur=None):

    #Genere l'affichage de la carte de puissances

    print("\nAffichage graphique de la puissance...")

    fig, ax = plot.subplots()
    draw_main_stage(MURS,width,height,base.x,base.y,fig,ax,recepteur)
    pwrs = full_transpose(powers_dbm)
    image = ax.imshow(pwrs, cmap='hot', interpolation='bicubic',extent=[0,width,height,0])
    fig.colorbar(image)
    
    ax.set_xlabel("Power map [dBm]")

def draw_bitrate_map(MURS,width,height,base,bitrate,recepteur=None):

    #Genere l'affichage du bitrate

    print("\nAffichage graphique du debit...")

    fig, ax = plot.subplots()
    draw_main_stage(MURS,width,height,base.x,base.y,fig,ax,recepteur)
    bitrates = full_transpose(bitrate)
    image = ax.imshow(bitrates, cmap='bone', interpolation='bicubic',extent=[0,width,height,0])
    fig.colorbar(image)

    ax.set_xlabel("Bitrate map [Mbps]")

def show_maps():
    #Affiche les fenetres
    plot.show()


def full_transpose(m):
    #Transposition de matrice
    res = []
    for i in range(0,len(m[0])):
        res.append([])
        for j in range(0,len(m)):
            res[i].append(m[j][i])

    return res
