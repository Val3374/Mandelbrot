import plotly.express as px
from numpy import *

n_max =  100
taille = 1000
a = linspace(-2, 1, taille)
b = linspace(-1.5, 1.5, taille)
A, B = meshgrid(a, b)
C = A + 1j * B

XY = zeros((taille, taille))
for i in range(n_max):
    XY = XY * XY + C

XY = abs(XY)
XY[XY > 2] = 0

fig = px.imshow(XY, template="plotly_dark")
fig.show()
