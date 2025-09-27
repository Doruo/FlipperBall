import numpy as np
import matplotlib.pyplot as plt

"""
Questions

1)
x=xc+r*cos(teta)
y=yc+r*sin(teta)

BX=np.linspace(xc,x,10)
BY=np.linspace(yc,y,10)

2) teta=np.linspace(0,2*np.pi,100)

"""

# Centre et rayon du cercle
Xc,Yc=1,1
r=2

# Définition de téta, définie sur [0,2pi[
teta=np.linspace(0,2*np.pi,100)

# Système des points du cercle
x=Xc+r*np.cos(teta)
y=Yc+r*np.sin(teta)

#Tableaux d'abscisses et d'ordonnées
BX=np.linspace(Xc,x,10)
BY=np.linspace(Yc,y,10)

# Nuage de points
l1=plt.plot(BX,BY)

# Affichage
plt.show()
