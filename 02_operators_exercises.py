# 1. Realiza las siguientes operaciones aritméticas:
# •	Suma: 15 + 25
# •	Resta: 50 - 22
# •	Multiplicación: 8 * 7
# •	División: 100 / 20

# 2. Calcula el resto de la división de 37 entre 5 y almacénalo en una variable remainder. Luego imprímelo.

a = 37
b = 5
remainder = a % b
print(remainder)

# 3. Convierte el número 7 en una cadena de texto y concaténalo con la frase “ es mi número favorito”. Imprime el resultado.

a = 7
str_a = str(a)
print (f'Mi número favorito es {str_a}')

# 4. Repite la palabra “Python” 10 veces usando el operador de multiplicación para cadenas y luego imprímela.

lenguaje = "Python "
print(lenguaje * 10)

# 5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si a es mayor que b y almacena el resultado en una variable booleana resultado. Imprime el valor de resultado.

a = 12
b = 8
resultado = a > b
print(resultado)

# 6. Compara dos cadenas de texto (“apple” y “banana”) usando los operadores > y < y explica cuál tiene mayor orden alfabético.

a = "apple"
b = "banana"
print(a > b)

# 7. Realiza una comparación lógica usando and para verificar si el número 10 es mayor que 5 y menor que 20. Imprime el resultado.

a = 20
b = 5
c = 10
print(a > b and a < c)

# 8. Usa el operador or para verificar si el número 7 es menor que 3 o mayor que 5. Imprime el resultado.

a = 7
b = 3
c = 5
print(a < b or a > c)

# 9. Aplica el operador not para invertir el resultado de la comparación 15 > 20. ¿Cuál es el resultado?

a = 15
b = 20
print(not a > b)

# 10. Combina operadores aritméticos y lógicos: Verifica si el número resultante de la expresión (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.

a = 5
b = 3
c = 2

abc = (a * b) + c
print(abc > 10 and abc < 20)