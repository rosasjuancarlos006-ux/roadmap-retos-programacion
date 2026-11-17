#--------------
#Operadores 
#--------------
#Operadores Aritmeticos

suma = 5 + 2
print("Suma: ", suma)

resta = 5 - 2
print("Resta: ", resta)

multiplicacion = 5 * 2
print("Multiplicacion: ", multiplicacion)

division = 5 / 2
print("Division: ", division)

division_entera = 5 // 2
print("Division Entera: ", division_entera)

potenciacion = 5 ** 2
print("Potenciacion: ", potenciacion)

modulo = 5 % 2
print("Modulo: ", modulo)

#Operadores de comparacion

igual = 5 == 2
print("Igual: ", igual)

diferente_de = 5 != 2
print("Diferente de: ", diferente_de)

mayor_que = 5 > 2
print("Mayor que: ", mayor_que)

menor_que = 5 < 2
print("Menor que: ", menor_que)

mayor_o_igual_que = 5 >= 2
print("Mayor o igual que: ", mayor_o_igual_que)

menor_o_igual_que = 5 <= 2
print("Menor o igual que: ", menor_o_igual_que)

#Operadores de asignacion

x = 5 # = asigna un valor
print("Valor de x: ", x)

x += 2 # += suma y asigna
print("Valor de x despues de x += 2: ", x)

x -= 2 # -= resta y asigna
print("Valor de x despues de x -= 2: ", x)

x *= 2 # *= multiplica y asigna
print("Valor de x despues de x *= 2: ", x)

x /= 2 # /= divide y asignas
print("Valor de x despues de x /= 2: ", x)

x //= 2 # //= divide y asigna el resultado entero
print("Valor de x despues de x //= 2: ", x) 

x **= 2 # **= eleva a la potencia y asigna
print("Valor de x despues de x **= 2: ", x)

# Operadores logicos
a = True
b = False

print("a and b: ", a and b)
print("a or b: ", a or b)
print("not a: ", not a)

#Operadores de pertenencia

palabra = "Hola"

print("a" in palabra)

print("z" not in palabra)

#Operadores de identidad

Palabra = "Python"

print(Palabra is int)

print(Palabra is not int)

#Operadores bit a bit

print(5 & 4) #AND
print(5 | 4) #OR
print(5 ^ 4) #XOR
print(~5) #NOT

#------------------
#Estructuras de control
#------------------

# Estructura condicional if
x = 10
y = 5
operador = input("Ingrese un operador (+, -, *, /): ")

if operador == "+":
    resultado = x + y
    print("El resultado de la suma es: ", resultado)
elif operador == "-":
    resultado = x - y
    print("El resultado de la resta es: ", resultado)
elif operador == "*":
    resultado = x * y
    print("El resultado de la multiplicacion es: ", resultado)
elif operador == "/":
    if y != 0:
        resultado = x/y
        print("El resultado de la division es: ", resultado)
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Error: Operador no valido.")

#Estructura condicional match

"""
Ahora, replicaremos el ejemplo anterior, pero esta vez utilizando la sentencia match, que es similiar a un switch
"""

match operador: 
    case "+":
        resultado = x + y
        print("El resultado de la suma es: ", resultado)
    case "-":
        resultado = x - y
        print("El resultado de la resta es: ", resultado)
    case "*":
        resultado = x * y
        print("El resultado de la multiplicacion es: ", resultado)
    case "/":
        if y != 0:
            resultado = x/y
            print("El resultado de la division es: ", resultado)
        else:
            print("Error: No se puede dividir entre cero.")
    case _:
        print("Error: Operador no valido.")


#Estructura de control for
for i in range(5):
    if i == 3:
        continue
    else:
        print("Iteracion: ", i)

#Estructura de control while
contador = 0

while contador < 10:
    print("Iteracion: ", contador)
    contador += 1

# Excepciones

"""
Retomaremos el ejemplo de la division por cero
"""

numero1 = float(input("Ingresa el primer numero: "))
numero2 = float(input("Ingresa el segundo numero: "))

try:
    resultado = numero1 / numero2
    print("El resultado de la division es: ", resultado)

except ZeroDivisionError as e: 
    print("Error: No se puede dividir entre cero.", e) 


"""
Ejercicio practico:
Crear un programa que imprima los numeros de 10 al 55 (incluidos), que sean pares y que no sea ni el 16 ni multiplos de 3.
"""

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)