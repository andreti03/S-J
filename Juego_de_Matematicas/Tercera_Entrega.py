import random
import tkinter as tk

def mult():
    vent = tk.Tk()
    vent.title("Multiplicacion")
    vent.geometry("350x400")
#    vent.iconbitmap(r"C:\Users\DELL\Desktop\Proyecto_Programacion\Juego_de_Matematicas\Board_37532.ico")
    vent.config(bg="lightblue")
    Td= tk.Label(vent,text="Bienvenido! al menu de Multiplicaciones ",bg="lightblue")
    Nota = tk.StringVar()
    texto = tk.Entry(vent, textvariable=Nota).place(x=5,y=60)
    Td2= tk.Label(vent,text="Escribe el numero de Multiplicaciones que deseas ",bg="lightblue")
    Td.place(x=0,y=0)
    Td2.place(x=0,y=20)
    tk.Button(vent,text="Siguente" ,bg="lightblue").place(x=150,y=360)
    tk.Button(vent,text="Cancelar" ,bg="lightblue").place(x=60,y=360)
    
def suma():
    vent3 = tk.Tk()
    vent3.title("Suma")
    vent3.geometry("350x400")
#    vent3.iconbitmap(r"C:\Users\DELL\Desktop\Proyecto_Programacion\Juego_de_Matematicas\Board_37532.ico")
    vent3.config(bg="lightblue")
    Td= tk.Label(vent3,text="Bienvenido! al menu de Sumas ",bg="lightblue")
    Nota = tk.StringVar()
    texto = tk.Entry(vent3, textvariable=Nota).place(x=5,y=60)
    Td2= tk.Label(vent3,text="Escribe el numero de Sumas que deseas realizar",bg="lightblue")
    Td.place(x=0,y=0)
    Td2.place(x=0,y=20)
    tk.Button(vent3,text="Siguente" ,bg="lightblue").place(x=150,y=360)
    tk.Button(vent3,text="Cancelar" ,bg="lightblue").place(x=60,y=360)    

def F_suma(n):
    sumador = 0
    for q in range(n):
            venta = tk.Tk()
            venta.title("Suma")
            venta.geometry("300x400")
#            venta.iconbitmap(r"C:\Users\DELL\Desktop\Proyecto_Programacion\Juego_de_Matematicas\Board_37532.ico")
            venta.config(bg="lightblue")
            
    


def resta():
    vent1 = tk.Tk()
    vent1.title("Resta")
#    vent1.iconbitmap(r"C:\Users\DELL\Desktop\Proyecto_Programacion\Juego_de_Matematicas\Board_37532.ico")
    vent1.geometry("350x400")
    vent1.config(bg="lightblue")
    Td= tk.Label(vent1,text="Bienvenido! al menu de Resta ",bg="lightblue")
    Nota = tk.StringVar()
    texto = tk.Entry(vent1, textvariable=Nota).place(x=5,y=60)
    Td2= tk.Label(vent1,text="Escribe el numero de Restas que deseas realizar ",bg="lightblue")
    Td.place(x=0,y=0)
    Td2.place(x=0,y=20)
    tk.Button(vent1,text="Siguente" ,bg="lightblue").place(x=150,y=360)
    tk.Button(vent1,text="Cancelar" ,bg="lightblue").place(x=60,y=360)    
    
def div():
    vent2 = tk.Tk()
    vent2.title("Division")
    vent2.geometry("350x400")
#    vent2.iconbitmap(r"C:\Users\DELL\Desktop\Proyecto_Programacion\Juego_de_Matematicas\Board_37532.ico")
    vent2.config(bg="lightblue")
    Td= tk.Label(vent2,text="Bienvenido! al menu de Divisiones ",bg="lightblue")
    Nota = tk.StringVar()
    texto = tk.Entry(vent2, textvariable=Nota).place(x=5,y=60)
    Td2= tk.Label(vent2,text="Escribe el numero de Divisiones que deseas realizar ",bg="lightblue")
    Td.place(x=0,y=0)
    Td2.place(x=0,y=20)
    tk.Button(vent2,text="Siguente" ,bg="lightblue").place(x=150,y=360)
    tk.Button(vent2,text="Cancelar" ,bg="lightblue").place(x=60,y=360)

def randum():
    n = random.randint(0,3)
    if n == 0:
        suma()
    elif n == 1:
        resta()
    elif n == 2:
        mult()
    elif n == 3:
        div()


def ubicar_botones():
    BotonSuma = tk.Button(ventana,text="Suma",command=suma,bg="lightgreen", font=("courier", 12, "bold")).place(x=250,y=100)
    BotonResta = tk.Button(ventana,text="Resta", command=resta,bg="lightgreen", font=("courier", 12, "bold")).place(x=245,y=145)
    BotonMulti = tk.Button(ventana,text="Multiplicación", command=mult,bg="lightgreen", font=("courier", 12, "bold")).place(x=200,y=190)
    BotonDivis = tk.Button(ventana,text="División", command=div,bg="lightgreen", font=("courier", 12, "bold")).place(x=230,y=235)
    BotonRandom = tk.Button(ventana,text="Random",command=randum,bg="lightgreen", font=("courier", 12, "bold")).place(x=240,y=280)
            
def what_test(n):

    N = n.upper()

    if N == "SUMA":
        x= tk.Label(ventana, wraplength= 500, text="¡Bienvenido a un curso de suma!" "¿Cuántas preguntas quiere?"\
            , font=("courier", 12, "bold"), bg="lightgreen", justify=tk.LEFT).place(x=10,y=0)
        if type(x)== int:
            return suma(x) 
    elif N == "RESTA":
        x = tk.Label(ventana, wraplength= 500, text="¡Bienvenido a un curso de resta!"  "¿Cuántas preguntas quiere?"\
            , font=("courier", 12, "bold"), bg="lightgreen", justify=tk.LEFT).place(x=10,y=0)
        if type(x)== int:
            return resta(x)
    elif N == "MULTIPLICACION":
        x = tk.Label(ventana, wraplength= 500, text="¡Bienvenido a un curso de multiplicación!" "¿Cuántas preguntas quiere?"\
            , font=("courier", 12, "bold"), bg="lightgreen", justify=tk.LEFT).place(x=10,y=0)
        if type(x)== int:
            return mult(x)
    elif N == "DIVISION":
        x = tk.Label(ventana, wraplength= 500, text="¡Bienvenido a un curso de división!" "¿Cuántas preguntas quiere?"\
            , font=("courier", 12, "bold"), bg="lightgreen", justify=tk.LEFT).place(x=10,y=0)
        if type(x)== int:
            return div(x)
        
ventana = tk.Tk()
ventana.title("Math")
#ventana.iconbitmap(r"C:\Users\DELL\Desktop\Programacion\Juego de Matematicas\calculator-512.ico")
ventana.geometry("550x500")
ventana.config(bg="lightgreen")

ubicar_botones()
label1 = tk.Label(ventana, wraplength= 500, text="!Bienvenido a un curso de matemática elemental! Elige que tipo de curso te gustaría realizar\
     Selecciona alguna de las siguientes opciones  suma - resta - multiplicacion - division: ", font=("courier", 12, "bold"), bg="lightgreen", justify=tk.LEFT)#Ubica el texto anteriormente(linea 10)
label1.place(x=10,y=0)


ventana.mainloop()