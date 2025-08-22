# 1. Declara una variable text con la frase “Aprendiendo Python” y luego imprime la longitud de la cadena usando len().

text = "Aprendiendo Python"
len(text)
print(len(text))

# 2. Concatena dos cadenas: “Hola” y “Python”, y muestra el resultado en una sola línea.

a = "Hola"
b = "Python"
len(a + b)
print(len (a + b))

# 3. Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.

print("¡Hola, mundo!\nBienvenidos al curso de Python")

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.

nombre = "Jaume"
apellido = "Pallàs"
edad = 18
print(f"Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}")

# 5. Desempaqueta los caracteres de la palabra “Python” en variables separadas y luego imprímelos uno por uno.

a,b,c,d,e,f = "Python"
print(a,b,c,d,e,f)

# 6. Extrae un “slice” de la palabra “Programación” para obtener los caracteres desde la posición 3 hasta la 7.

palabra = "programación"
print(palabra[3:7])

# 7. Invierte la cadena “Python” usando slicing y muestra el resultado.

b = "Python"
print(b[::-1])

# 8. Convierte la cadena “aprendiendo python” en mayúsculas usando el metodo adecuado e imprímela.

c = "aprendiendo python"
print(c.upper())

# 9. Cuenta cuántas veces aparece la letra “n” en la cadena “Programación en Python”.

b = "Python"
print(b.count("n"))

# 10. Verifica si la cadena “12345” es numérica usando el metodo adecuado e imprime el resultado.

numero = "12345"
print(numero.isnumeric())
