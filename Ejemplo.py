#Tipos de datos
a=1
b=1.2
c='Hola'
d=True
print('-------Imprimir los tipos de datos--------------')
print(a, 'es de tipo: ', type(a))
print(b, 'es de tipo: ', type(b))
print(c, 'es de tipo: ', type(c))
print(d, 'es de tipo: ', type(d))
print('-------Operaciones tipos de datos--------------')
var='Juan'
num=5
print('-------Operación de un entero con un str--------------')
print(var*num)
print('-------Concatenar str--------------')
var1='Hola'
var2=' Mundo'
print(var1 + var2)

print('-------Funciones--------------')
def sumar(x,y):
	return x+y

print('El resultado de la función es: ', sumar(1,2))
