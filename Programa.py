#programa para generar un número aleatorio en python

import random

#la funcion input captura un datos desde el teclado
# como si fuera una cadna de texto (string)

a= input('Limite inferior:')
b= input('Limite superior:')

#convetir a y b a entesros
a=int(a)
b=int(b)
respuesta= random.randint(a,b)
print(respuesta)