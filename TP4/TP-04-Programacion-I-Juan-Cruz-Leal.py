#Ejercicio 1
"""
    1) Crea un programa que imprima en pantalla todos 
    los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente,
mostrando un número por línea.

"""
# Recorremos los números del 0 al 100
#Incluimos 101 ya que range(n) toma valores hasta n-1
for i in range(101):
    print(i)

#Ejercicio 2
"""
 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.

"""
# Pedimos al usuario un número
numero = int(input("Ingrese un número entero: "))

# Convertimos a positivo para contar dígitos correctamente
numero_abs = abs(numero)

# Contamos los dígitos convirtiendo el número a string
cantidad_digitos = len(str(numero_abs))

print("Cantidad de dígitos:", cantidad_digitos)


#Ejercicio 3
    
"""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
    
"""
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Aseguramos que num1 sea menor que num2
if num1 > num2:
    num1, num2 = num2, num1

suma = 0
for i in range(num1 + 1, num2):
    suma += i

print("La suma es:", suma)


#Ejercicio 4
"""
    4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
    
"""

suma = 0

while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break
    suma += num

print("La suma total es:", suma)

#Ejercicio 5
"""
    5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
    
"""
import random

numero_secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivine el número entre 0 y 9: "))
    intentos += 1
    if intento == numero_secreto:
        break

print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")


#Ejercicio 6
"""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.

"""
# Recorremos desde 100 hasta 0 de 1 en 1
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)


#Ejercicio 7
"""
    7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
    
"""
num = int(input("Ingrese un número entero positivo: "))

suma = 0
for i in range(0, num + 1):
    suma += i

print("La suma es:", suma)


#Ejercicio 8
"""
    8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
    
"""
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(100):
    num = int(input(f"Ingrese el número {i+1}: "))
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

#Ejercicio 9
"""
    9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)

"""
suma = 0
cantidad = 100 

for i in range(cantidad):
    num = int(input(f"Ingrese el número {i+1}: "))
    suma += num

media = suma / cantidad
print("La media es:", media)


#Ejercicio 10
"""
    10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745
    
"""
numero = int(input("Ingrese un número: "))

# Detectamos el signo
signo = -1 if numero < 0 else 1
numero_abs = abs(numero)

# Invertimos usando strings
numero_invertido = int(str(numero_abs)[::-1]) * signo

print("Número invertido:", numero_invertido)
