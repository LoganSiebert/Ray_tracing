import matplotlib.pyplot as plot
from matplotlib import collections  as coll
import pylab as pl
from constantes import *
from mur import Mur
import numpy as np
from numpy.matrixlib import matrix


def decode_plan(filename):
    #Cette fonction permet de lire le plan et de renvoyer la liste de murs
    #ainsi que l'emetteur et le récepteur
    input = open(filename,'r')
    lines = input.readlines()
    input.close()
    murs = []
    for line in lines:
        content = line.split(" ")
        #Les premieres lignes (dimensions, emetteur, recepteur)
        keyword = content[0]
        if keyword=="DIMENSIONS":
            width = float(content[1])
            height = float(content[2])
        elif keyword=="EMETTEUR":
            emetteur = [float(content[1]),float(content[2])]
        elif keyword=="RECEPTEUR":
            recepteur= [float(content[1]),float(content[2])]
        #Les murs et les bords
        elif keyword == "M":
            x1,y1,x2,y2 = float(content[3]),float(content[4]),float(content[5]),float(content[6])
            #Les types de mur (brique, béton, cloison)
            eps = EPS_1
            sig = SIG_1
            materiau = content[1]
            if materiau=="2":
                eps = EPS_2
                sig = SIG_2
            elif materiau=="3":
                eps = EPS_3
                sig = SIG_3
            bord1=[x1,y1]
            bord2=[x2,y2]
            m = Mur(float(content[2]),bord1,bord2,eps,sig)
            murs.append(m)
    return [width,height,emetteur,recepteur,murs]



def draw_main_stage(murs,width,height,TXx,TXy,fig,ax):
    #Genere l'affichage de l'etage
    lines = []
    #Dessin des murs
    for mur in murs:
        p1=(mur.bord1[0],mur.bord1[1])
        p2=(mur.bord2[0],mur.bord2[1])
        seg = [p1,p2]
        lines.append(seg)
    wallLines = coll.LineCollection(lines)
    wallLines.set_color("black")
    wallLines.set_linewidth(2)    
    ax.add_collection(wallLines)
    fig.canvas.set_window_title("Ray Tracing")
    ax.set_xlim(-1, width+1)
    ax.set_ylim(-1, height+1)
    ax.set_facecolor('white')


def draw_rays(murs, rays_reflexion, width, height, TXx, TXy, RXx, RXy):
    #Genere l'affichage des rayons
    fig, ax = plot.subplots()
    draw_main_stage(murs,width,height,TXx,TXy,fig,ax)  
    ray_lines = []
    ax.plot(RXx,RXy,"bo",markersize=7)
    ax.plot(TXx,TXy, "mo",markersize=7)
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
                    ax.plot(p1[0], p1[1],"y+",markersize=9)
        if len(points_transmission)>0:
            for pt in points_transmission:
                ax.plot(pt.x, pt.y,"go",markersize=2)
    ray_lines_collection = coll.LineCollection(ray_lines)
    ray_lines_collection.set_color("red")
    ray_lines_collection.set_linewidth(1)    
    ax.add_collection(ray_lines_collection)


def draw_power_map(MURS,width,height,emetteur,powers,recepteur):
    #Genere l'affichage de la carte de puissances
    fig, ax = plot.subplots()
    ax.plot(recepteur[0],recepteur[1],"bo",markersize=7)
    ax.plot(emetteur[0],emetteur[1], "mo",markersize=7)
    draw_main_stage(MURS,width,height,emetteur[0],emetteur[1],fig,ax)
    pwrs = full_transpose(powers)
    image = ax.imshow(pwrs, cmap='hot', interpolation='bicubic',extent=[0,width,height,0])
    fig.colorbar(image)   
    ax.set_xlabel("Power (dBm)")

def draw_bitrate_map(MURS,width,height,emetteur,bitrate,recepteur):
    #Genere l'affichage du bitrate
    fig, ax = plot.subplots()
    ax.plot(recepteur[0],recepteur[1],"bo",markersize=7)
    ax.plot(emetteur[0],emetteur[1], "mo",markersize=7)
    draw_main_stage(MURS,width,height,emetteur[0],emetteur[1],fig,ax)
    bitrates = full_transpose(bitrate)
    image = ax.imshow(bitrates, cmap='bone', interpolation='bicubic',extent=[0,width,height,0])
    fig.colorbar(image)
    ax.set_xlabel("Bitrate (Mb/s)")

def full_transpose(m):
    #Met la matrice de puissance à l'endroit
    res = []
    for i in range(0,len(m[0])):
        res.append([])
        for j in range(0,len(m)):
            res[i].append(m[j][i])
    return res
