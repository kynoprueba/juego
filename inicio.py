from modulo1 import Ingeniero
from maquina import Maquina


e=Ingeniero(10,'ingles','rock')
print(e.calcular('autocad'))

m=Maquina()
salida=m.mover()




valor=m.piezas

if valor <= salida:
    print('es un valor mayor')
else:
    print('es valor menor a 10')



