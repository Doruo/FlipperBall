import numpy as np
import matplotlib.pyplot as plt
import math

#delta
dt=0.01

# Coordonnées des points A et B
Xa,Ya=1,1
Xb,Yb=10,5

# nombre d'images
nImage=100

# Centre et rayon du cercle
Xc,Xc=1,1
r=0.1

# Définition de téta, défini sur [0,2pi[
teta=np.linspace(0,2*np.pi,100)

#définition du cercle:
# les abscisses
x=Xc+r*np.cos(teta)
# les ordonnées:
y=Xc+r*np.sin(teta)

# boucle pour l'animation
for i in range(nImage):

    # Initialisation
    if i == 0:
        line, = plt.plot(x,y)
        plt.axis([-1,10,-1,10])

    # Déplacement
    else:
        x=x+((Xb-Xa)/nImage)
        y=y+((Yb-Ya)/nImage)
        line.set_data(x,y)
    plt.pause(dt)
