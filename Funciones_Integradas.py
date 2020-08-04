from math import pi
'''
str funcion para cambiar un valor a cadena
bin para cambiar un valor a binario
hex para cambiar a hexadecimal
int para cambiar a un entero
roud redondeo
len cantidad de caracteres que tiene la cadena

'''
'''Ejercio 1
a = float(input('indicar el valor de a :'))
b = float(input('indicar el valor de b:'))
c = float(input('indicar el valor de c:'))

print(f'el valor de a es:{a}')
print(f'el valor de b es:{b}')
print(f'el valor de c es:{c}')

resultado = (a**3*(b**2-2*a*c))/(2*b)
print(f'el resultado es {resultado}')
'''
'''Ejercicio 2 con bool
exp1 = (3 + 5 * 8) < 3
exp2 = (((-6/3) * 4) + 2 < 2)
A = float(input('ingresar valor de variable A:'))
B = float(input('ingresar valor de variable B:'))

resultado = exp1 and exp2 or (A > B)

print(f'el resultado es:{resultado}')
'''
'''Ejercicio 3 intercambiar variables

a = int(input('A.-'))
b = int(input('B.-'))
a , b = b, a
print(f'el nuevo valor de A es:{a} y el nuevo valor de B es {b}')

'''
'''Ejercicio 4

Radio = float(input(f'indicar el radio del circulo: '))
area = pi * Radio**2
longitud = 2 *pi * Radio


print(f'el area de un circulo es {longitud:.2f} y el area es {area:.2f} ')
'''

# :.2f, son los decimales que se deben visualizar para un tipo float
# f es el formato para ocupar las {}


'''Ejercicio 5'''
compra = float(input(f'indica el valor de tu compra: '))
v_des = 0.15
Resultado = compra * v_des
total = compra - Resultado

print(f'el valor total es:{total:.2f}')



























