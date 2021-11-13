# Adivine-el-Numero

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/guerramorante/Adivine-el-Numero.git)
https://github.com/guerramorante/Adivine-el-Numero.git

Hemos resuelto un juego de adivinar con valores enteros entre 0 y 99

```import random
numero = random.randint (0,99)
print("\t.: Adivina el numero")
numero_de_intentos = 0
while True:
    numero1 = int(input("Introduzca un número del 1 al 100:"))
    numero_de_intentos += 1
    if numero1 == numero:
       print("¡Esta es la respuesta!") 
       break
    else:
        if numero1 > numero:
           print("Prueba con un numero menor")
        else: 
           print("Prueba con un numero mayor")
print(f"\nNúmero de intentos: {numero_de_intentos}")```
