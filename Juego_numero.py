import random
numero = random.randint (0,100)
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
print(f"\nNúmero de intentos: {numero_de_intentos}")
