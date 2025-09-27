# FlipperBall
## TP: réalisation d'une animation du déplacement d'une boule de Flipper

L'objectif de ce TP est d'utiliser le langage Python pour programmer le déplacement d'une boule de Flipper.
(qui sera plus prosaïquement un cercle du plan euclidien). 

On utilisera pour modéliser ce déplacement les résultats du cours de géométrie analytique.

### Partie 1: tracé d'un cercle

On considèrera que le plan euclidien est muni d'un repère orthonormal R =(0, −→i , −→j).

- Question 1
```python
x=xc+r*cos(teta)
y=yc+r*sin(teta)

BX=np.linspace(xc,x,10)
BY=np.linspace(yc,y,10)
```
- Question 2

```python
teta=np.linspace(0,2*np.pi,100)
```

### Partie 2: déplacement du cercle

Dans cette partie on considère que la boule se déplace dans un plan infini sans obstacles. Il s'agit de comprendre
le mécanisme d'une animation sous Python.

### Partie 3: modélisation du rebond sur des parois fixes

On veut modéliser le rebond élastique (sans perte de quantité de mouvement) de la boule sur une paroi verticale
puis sur une paroi horizontale.

La boule arrive sur la paroi au point M avec un vecteur vitesse −→Ve et repart avec un vecteur vitesse −→Vs. Les
deux vecteurs vitesses sont de même norme. La représentation graphique du vecteur −→Vs (en vert sur la figure) est
l'opposée du symétrique du vecteur −→Ve par rapport à la droite horizontale.

Sur la figure ci-dessus le bord de la paroi où a lieu le contact a pour équation x = h (avec h > 0) et la boule
avant le contact se déplace dans le demi-plan d'équation x ≤h .


- Question 1 

On sait qu'au moment de l'impact, la boule va effectuer 
un mouvement symétrique par rapport à la droite horizontale,
donc sur l'axe h. Une transformation de symétrie équivaut à
déterminer le complément d'une même coordonné.

Donc avec Ve(Vx,Vy), on aura Vs(-Vx, Vy). 
Cela permettra d'effectuer un déplacement opposé sur l'axe horizontale.

- Question 2
Pour x=h, sur le bord droite de la boule, la condition est Xc + r >= h.

- Question 3 

Pour le bord gauche, comme cela s'applique dans le sens inverse sur X, 
la condition sera donc: Xc - r < 0 avec x=0.

- Question 4 

Sur l'axe vertical avec Y=h, les conditions sont similaires car 
elle s'applique juste maintenant à la coordonée y du vecteur:

Avec Ve(Vx,Vy), on aura Vs(Vx, -Vy).

### Partie 4: modélisation du rebond sur un obstacle circulaire fixe

L'obstacle circulaire fixe a pour centre F(xf yf) et pour rayon R.
La boule de flipper a pour centre C(xc yc) et p our rayon r. 

Elle arrive avec une vitesse −→ve et repart avec une vitesse −→vs. 
Le vecteur −→vs est l'opp osé du vecteur symétrique de −→ve par rapp ort à la droite (CF)