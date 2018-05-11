from math import*
from cmath import*
from mur import*
from point import*
from rayon import*
from constantes import*

####################
#      Getters     #
####################

def get_theta_i (direction,p2):
    #angle d'incidence au point p2 (appartenant à un mur) ayant pour attribut la
    #direction du rayon passant par ce point
    mur = p2.mur 
    if mur.is_horizontal():
        if direction == None:
            return PI/2
        else:
            return PI/2 - atan(direction)
    else:
        if direction == None:
            return 0
        else:
            return atan(direction)


def get_theta_t (theta_i,eps):
    # Loi de Snell
    return asin((sqrt(EPS_0)/sqrt(eps))*sin(theta_i))


def s(theta_t,l):
    # Distance parcourue dans le mur
    if theta_t != PI/2:
        return l/cos(theta_t)
    else:
        return 0

def coeff_reflexion_perpendiculaire(eps,theta_i):
    # Coefficent de reflexion pour onde plane polarisée perpendiculairement
    #Z1 impédance du vide, Z2 impédance du mur
    theta_t= get_theta_t(theta_i,eps)
    Z1=sqrt(U0/EPS0)
    Z2=sqrt(U0/eps)
    return (Z2*cos(theta_i)-Z1*cos(theta_t))/(Z2*cos(theta_i)+Z1*cos(theta_t))

####################
#   Transmisssion  #
####################

def transmission_coefficient(rayon):
    #change le coefficient de transmission des points de transmissions du rayon
    points_transmissions = rayon.get_points_transmission() #Récupération des pts de transmission

    for pt in points_transmissions:
        mur = pt.mur
        alpha = mur.alpha
        beta = mur.beta
        gamma = complex(alpha,beta)
        if(pt.direction != None):
            direction = abs(pt.direction)
        else:
            direction = None
        theta_i = get_theta_i(direction,pt)
        theta_t = get_theta_t(theta_i,mur.epsilon)
        s = s(theta_t,mur.epaisseur)
        Z1 = sqrt(U0/EPS_0)
        Z2 = sqrt(U0/mur.epsilon)
        r = coeff_reflexion_perpendiculaire(mur.epsilon,theta_i)
        coeff_mur = ((1-pow(r,2))*cexp(-gamma*s))/(1-(pow(r,2)*cexp((-2*gamma*s)+(gamma*2*s*sin(theta_t)*sin(theta_i))))
        pt.set_coefficient_value(coeff_mur)
                          

####################
#    Réflexion    #
####################

def reflexion_coefficient(rayon):

    #change le coefficient de réflexion des points de réflexion du rayon

    points_reflexion = rayon.get_points_reflexions()
    
    for pt in points_reflexion:
        mur = pt.mur
        alpha = mur.alpha
        beta = mur.beta
        gamma = complex(alpha,beta)
        if(pt.direction != None):
            direction = abs(pt.direction)
        else: 
            direction = None
        theta_i = get_theta_i(direction,pt)
        theta_t = get_theta_t(theta_i,mur.epsilon)
        s = s(theta_t,mur.epaisseur)
        Z1 = sqrt(U0/EPS_0)
        Z2 = sqrt(U0/mur.epsilon)
        r = coeff_reflexion_perpendiculaire(mur.epsilon,theta_i)
        coeff_mur = r + ((1-pow(r,2))* r *cexp(-2*gamma*s)*cexp(2*gamma*s*sin(theta_t)*sin(theta_i)))/(1-(pow(r,2)*cexp((-2*gamma*s)+(gamma*2*s*sin(theta_t)*sin(theta_i)))))
        pt.set_coefficient_value(coeff_mur)





  

