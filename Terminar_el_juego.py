import random
while True:
    print("Adivina el numero")
    print("""Escoja nivel de dificultad
Nivel 1 simple: entre 0 y 100
Nivel 2 intermedio: entre 0 y 1000
Nivel 3 avanzado: entre 0 y 1000000
Nivel 4 experto: entre 0 y 1000000000000""")
    level=int(input("Escriba su opción (de 1 a 4): "))
    if level <=4:
        if level ==1:
            print("Has seleccionado el nivel simple, tienes que adivinar un numero entre 0 y 100 y solo tienes 15 intentos")
        elif level ==2:
            print("Has seleccionado el nivel intermedio, tienes que adivinar un numero entre 0 y 1000 y solo tienes 35 intentos")
        elif level ==3:
            print("Has seleccinado el nivel avanzado, tienes que adivinar un numero entre 0 y 1000000 y solo tienes 70")
        elif level ==4:
            print("Has seleccionado el nivel experto, tienes que adivinar un numero entre 0 y 1000000000000 y tienes 190 intentos")
    else:
        print("Este nivel no existe")
    if level == 1:
       import random 
       numero=random.randint (0,100)
       print("\t.: Escoja un numero")
       numero_de_intentos = 0
       while True:
        numero1 = int(input("Introduzca un número del 0 al 100:"))
        numero_de_intentos += 1
        mumero_de_intentos_max = 15
        if numero1 == numero:
           print("¡Esta es la respuesta!") 
           break
        else:
            if numero1 > numero:
               print("Prueba con un numero menor")
            else: 
               print("Prueba con un numero mayor")
       print(f"\nNúmero de intentos: {numero_de_intentos}")
    if level ==2:
        import random
        numero=random.randint (0,1000)
        print("\t.: Escoja un numero")
        numero_de_intentos = 0
        while True:
         numero1 = int(input("Introduzca un numero del 0 al 1000:"))
         numero_de_intentos += 1
         numero_de_intentos_max = 35
         if numero1== numero:
             print("¡Esta es la respuesta correcta!")
             break
         else:
             if numero1 > numero:
                 print("Pruebe un numero menor")
             else:
                 print("Pruebe un numero mayor")
         print(f"\nNúmero de intentos: {numero_de_intentos}")
    if level == 3:
        import random
        numero=random.randint (0,1000000)
        print("\t.: Escoja un numero")
        numero_de_intentos = 0
        while True:
         numero1 = int(input("Introduzca un numero del 0 al 1000000:"))
         numero_de_intentos += 1
         numero_de_intentos_max = 70
         if numero1== numero:
             print("¡Esta es la respuesta correcta!")
             break
         else:
             if numero1 > numero:
                 print("Pruebe un numero menor")
             else:
                 print("Pruebe un numero mayor")
         print(f"\nNúmero de intentos: {numero_de_intentos}")
    if level == 4:
        import random
        numero=random.randint (0,1000000000000)
        print("\t.: Escoja un numero")
        numero_de_intentos = 0
        while True:
         numero1 = int(input("Introduzca un numero del 0 al 1000000000000:"))
         numero_de_intentos += 1
         numero_de_intentos_max = 190
         if numero1== numero:
             print("¡Esta es la respuesta correcta!")
             break
         else:
             if numero1 > numero:
                 print("Pruebe un numero menor")
             else:
                 print("Pruebe un numero mayor")
         print(f"\nNúmero de intentos: {numero_de_intentos}")


