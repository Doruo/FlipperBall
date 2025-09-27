import numpy as np
import matplotlib.pyplot as plt
import math
import random

"""
- PARTIE 3 -

1) On sait qu'au moment de l'impact, la boule va effectuer 
un mouvement symétrique par rapport à la droite horizontale,
donc sur l'axe h. Une transformation de symétrie équivaut à
déterminer le complément d'une même coordonné.

Donc avec Ve(Vx,Vy), on aura Vs(-Vx, Vy). 
Cela permettra d'effectuer un déplacement opposé sur l'axe horizontale.

2)
Pour x=h, sur le bord droite de la boule, la condition est Xc + r >= h.

3) Pour le bord gauche, comme cela s'applique dans le sens inverse sur X, 
la condition sera donc: Xc - r < 0 avec x=0.

4) Sur l'axe vertical avec Y=h, les conditions sont similaires car 
elle s'applique juste maintenant à la coordonée y du vecteur:

Avec Ve(Vx,Vy), on aura Vs(Vx, -Vy)

"""

#delta
dt=0.01

# Coordonnées des points A et B
Xa,Ya=1,1
Xm,Ym=10,random.randint(1,10)

# nombre d'images
nImage=100 # Valeur qui ne va jamais changé

# Centre et rayon du cercle
Xc,Yc=1,random.randint(1,3)
r=0.1

# Définition de téta, défini sur [0,2pi[
teta=np.linspace(0,2*np.pi,100)

#définition du cercle:
# les abscisses
x=Xc+r*np.cos(teta)
# les ordonnées:
y=Yc+r*np.sin(teta)

# Définition du plan sur x et y sur [0,10]
limit=10
plt.xlim(0, limit)
plt.ylim(0, limit)
# Creation de la boule
line, = plt.plot(x,y)

# Si un des 4 bords touchés
# On modifie Xm ou Xy pour modifier le trajet de la balle
def verifyBorderAxisX(Xm,Ym) :
    global nImage
    # Bord droite gauche touché
    if x[0]>=limit:
        return -1*(Xm),Ym
    elif x[0]<=0:
        return -1*(Xm),Ym
    # Bord haut bas touché
    elif y[0]<=0:
        return Xm,-1*(Ym)
    elif y[0]>=limit:
        return Xm,-1*(Ym)
    # Valeur inchangé sinon
    return Xm,Ym

# boucle pour l'animation (avant impact)
while True:
    Xm,Ym = verifyBorderAxisX(Xm,Ym)
    print(x[0])
    print(y[0])
    # Déplacement
    x=x+((Xm-Xa)/nImage)
    y=y+((Ym-Ya)/nImage)
    line.set_data(x,y)
    plt.pause(dt)   

