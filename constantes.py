from math import *

EPS_0 = 1/(36*pi)*pow(10,-9) 
U0 = 4*pi*pow(10,-7)

EPS_1 = 4.6*EPS_0 #Brique
SIG_1 = 0.02
EPS_2 = 5*EPS_0 #Béton
SIG_2 = 0.014
EPS_3 = 2.25*EPS_0 #Cloison
SIG_3 = 0.04

F = 2.45*pow(10,9) #fréquence
WAVELENGTH = 3*pow(10,8)/F #longueur d'onde
BETA = 2*pi*F/(3*pow(10,8)) #nombre d'onde
OMEGA = 2*pi*F #pulsation
HAUTEUR_EQ=WAVELENGTH/pi
Ra=50
POWER=1.995 #20 dBm
GAIN=0.1 #3 dBi
