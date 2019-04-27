import random

CHOICE = str(input("!Bienvenido a un curso de matemática elemental!" + 
               "\n" + "Elige que tipo de curso te gustaría realizar" + 
               "\n" + "Escribe alguna de las siguientes opciones SIN tildes"
               + "\n" + "suma - resta - multiplicacion - division" + "\n"
               + ": \t"))

def mult(n):
    sumador = 0
    for q in range(n):
        a = random.randrange(1, 11)
        b = random.randrange(1, 11)
        c = a * b
        h = int(input(f"¿Cuánto es {a} x {b}?: "))
        if c == h:
            print("Correcto")
            sumador += 1
        else:
            print("Incorrecto")
    total = (sumador/n) * 100
    r = round(total)
    print(f"Su puntaje es de {r}% respuestas correctas")
    
def suma(n):
    sumador = 0
    for q in range(n):
        a = random.randrange(1, 11)
        b = random.randrange(1, 11)
        c = a + b
        h = int(input(f"¿Cuánto es {a} + {b}?: "))
        if c == h:
            print("Correcto")
            sumador += 1
        else:
            print("Incorrecto")
    total = (sumador/n) * 100
    r = round(total)
    print(f"Su puntaje es de {r}% respuestas correctas")
    
def resta(n):
    sumador = 0
    for q in range(n):
        a = random.randrange(1, 11)
        b = random.randrange(1, a + 1)
        c = a - b
        h = int(input(f"¿Cuánto es {a} - {b}?: "))
        if c == h:
            print("Correcto")
            sumador += 1
        else:
            print("Incorrecto")
    total = (sumador/n) * 100
    r = round(total)
    print(f"Su puntaje es de {r}% respuestas correctas")
    
def div(n):
    sumador = 0
    for q in range(n):
        a = random.randrange(1, 11)
        b = random.randrange(1, a + 1)
        c = a // b
        residuo = a % b
        h = int(input(f"¿Cuánto es {a} ÷ {b}?: "))
        m = int(input("¿Cuánto es el residuo?: "))
        if c == h and residuo == m:
            print("Correcto")
            sumador += 1
        else:
            print("Incorrecto")
    total = (sumador/n) * 100
    r = round(total)
    print(f"Su puntaje es de {r}% respuestas correctas")

            
def what_test(n):

    N = n.upper()
    if N == "SUMA":
        x= int(input("¡Bienvenido a un curso de suma!" + "\n" + 
              "¿Cuántas preguntas quiere?" + "\n" + ": \t"))
        if type(x)== int:
            return suma(x) 
    elif N == "RESTA":
        x = (int(input("¡Bienvenido a un curso de resta!" + "\n" + 
              "¿Cuántas preguntas quiere?" + "\n" + ": \t")))
        if type(x)== int:
            return resta(x)
    elif N == "MULTIPLICACION":
        x = (int(input("¡Bienvenido a un curso de multiplicación!" + "\n" + 
              "¿Cuántas preguntas quiere?" + "\n" + ": \t")))
        if type(x)== int:
            return mult(x)
    elif N == "DIVISION":
        x = (int(input("¡Bienvenido a un curso de división!" + "\n" + 
              "¿Cuántas preguntas quiere?" + "\n" + ": \t")))
        if type(x)== int:
            return div(x)
        
        
what_test(CHOICE)