from interface import*
from simulation import*
from image import*

#Génère la zone de couverture (cartographie de puissance et de bitrate maximal)
# ainsi que du tracé des rayons

data = decode_plan("plan_test2.txt")
width, height, emetteur, recepteur, murs = data[0],data[1],data[2], data[3],data[4]

compute_power(width,height,emetteur,murs) #Génération de la zone de couverture

rayons_reflexion = rayons_reflechi(Point(emetteur[0], emetteur[1]), Point(recepteur[0], recepteur[1]), murs)
rayons_direct =  rayon_direct(Point(emetteur[0], emetteur[1]), Point(recepteur[0], recepteur[1]),murs)
rayons_affichage =[]
rayons_affichage.extend(rayons_reflexion)
rayons_affichage.extend(rayons_direct)

draw_rays(murs,rayons_affichage,width,height,emetteur[0],emetteur[0],recepteur[0],recepteur[1]) #tracé des rayons
plot.show()
