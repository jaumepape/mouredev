# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.

tuple_1 = (10, 20, 30, 40, 50)
print(tuple_1)

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.

tuple_2 = (100, 200, 300, 400, 500)
print(tuple_2[1])

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.

tuple_3 = (1, 2, 3)
# las tuplas son inmutables
list_3 = list(tuple_3)
list_3[0] = 10
tuple_3 = tuple(list_3)
print(tuple_3)
print(type(tuple_3))

# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).

tuple_4 = (1, 2, 3, 3, 4, 5, 3)
print(tuple_4.count(3))

# 5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").

tuple_5 = ("Java", "Python", "JavaScript", "Python")
print(tuple_5.index("Python"))

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.

tuple_6 = (1, 2, 3)
tuple_7 = (4, 5, 6)
print(tuple_6 + tuple_7)

# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).

tuple_8 = (10, 20, 30, 40, 50)
print(tuple_8[2:4])

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.

tuple_9 = ("rojo", "verde", "azul")
list_10 = list(tuple_9)
list_10[1] = "amarillo"
tuple_10 = tuple(list_10)
print(tuple_10)

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.

my_tuple = (1, 2, 3, 4, 5)
del my_tuple

# 10. Crea una tupla con un solo elemento (el número 100) e imprímela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.

tuple_11 = (100,)
print(tuple_11)