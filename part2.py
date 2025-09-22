import numpy as np
import matplotlib.pyplot as plt
import math

#delta
dt=0.01
# Coordonnées des points A et B
xa,ya=1,1
xb,yb=10,5
# nombre d'images
nImage=100

# Centre et rayon du cercle
xc,yc=1,1
r=0.1

# Définition de téta, défini sur [0,2pi[
teta=np.linspace(0,2*np.pi,100)

#définition du cercle:
# les abscisses
x=xc+r*np.cos(teta)
# les ordonnées:
y=yc+r*np.sin(teta)

# boucle pour l'animation
for i in range(nImage):

    # Initialisation
    if i == 0:
        line, = plt.plot(x,y)
        plt.axis([-1,10,-1,10])

    # Déplacement
    else:
        x=x+((xb-xa)/nImage)
        y=y+((yb-ya)/nImage)
        line.set_data(x,y)
    plt.pause(dt)
