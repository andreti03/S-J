import random

CHOICE = str(input("!Bienvenido a un curso de matemática elemental!" + 
               "\n" + "Elige que tipo de curso te gustaría realizar" + 
               "\n" + "Elige alguna de las siguientes opciones"
               + "\n" + "suma - resta - multiplicación - división" + "\n"
               + ": \t"))

def mult(n):
    """hacer n número de preguntas de multiplicación"""
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
    """hacer n número de preguntas de suma"""
    sumador = 0
    for q in range(n):
        a = random.randrange(1, 31)
        b = random.randrange(1, 31)
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
    """hacer n número de preguntas de resta"""
    sumador = 0
    for q in range(n):
        a = random.randrange(1, 31)
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
    """hacer n número de preguntas de división"""
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
    """pregunta un string n para la prueba que se quiere hacer"""

    N = n.upper()#capitalizar el string para evitar errores de elección
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
    elif N == "MULTIPLICACION" or N == "MULTIPLICACIÓN":#se usa or para evitar errores de tilde
        x = (int(input("¡Bienvenido a un curso de multiplicación!" + "\n" + 
              "¿Cuántas preguntas quiere?" + "\n" + ": \t")))
        if type(x)== int:
            return mult(x)
    elif N == "DIVISION" or N == "DIVISIÓN":#se usa or para evitar errores de tilde
        x = (int(input("¡Bienvenido a un curso de división!" + "\n" + 
              "¿Cuántas preguntas quiere?" + "\n" + ": \t")))
        if type(x)== int:
            return div(x)
        
        
what_test(CHOICE)