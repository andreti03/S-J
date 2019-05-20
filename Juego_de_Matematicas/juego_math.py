import random
import tkinter as tk
from tkinter import ttk

class Operaciones:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def suma(self):
        return self.x + self.y
    
    def resta(self):
        return self.x - self.y
    
    def mult(self):
        return self.x * self.y
    
    def div(self):
        return self.x // self.y
    
    def residuo(self):
        return self.x % self.y
        
    def __strsuma__(self):
        return "¿Cuánto es {0} + {1}?".format(self.x, self.y)
    
    def __strresta__(self):
        return "¿Cuánto es {0} - {1}?".format(self.x, self.y)
    
    def __strmult__(self):
        return "¿Cuánto es {0} x {1}?".format(self.x, self.y)
    
    def __strdiv__(self):
        return "¿Cuánto es {0} ÷ {1}?".format(self.x, self.y)
    
    def __strres__(self):
        return "¿Cuánto es el residuo de {0} ÷ {1}?".format(self.x, self.y)
    
    
    
def iterate_suma():
    sumando1 = random.randrange(1, 11)
    sumando2 = random.randrange(1, 11)
    suma = Operaciones(sumando1, sumando2)
    vents = tk.Tk()
    vents.title("Suma")
    vents.geometry("300x350")
    vents.config(bg = "lightgreen")
    entry = ttk.Entry(vents)
    entry.place(x=86, y=50)
    tit = tk.Label(vents, text= suma.__strsuma__(), bg = "red", fg ="white", font = ("courier",12), justify="center")
    tit.place(x=63, y=10)
    def comparar():
        if entry.get()== str(suma.suma()):
            tk.Label(vents,text="CORRECTO",bg="lightgreen").place(x=120, y=150)
            print("¡GOOD!")
        else:
            tk.Label(vents,text="INCORRECTO",bg="lightgreen").place(x=120, y=150)
            print("¡NOT GOOD!")
        vents.update_idletasks()
    def close():
        vents.destroy()
    button = ttk.Button(vents, text="Verificar",command= comparar)
    buttonq = ttk.Button(vents, text="Salir",command= close)
    buttonq.place(x=150, y=100)
    button.place(x=71, y=100)


def iterate_suma2():
    for q in range(2):
        iterate_suma()

def iterate_suma3():
    for q in range(3):
        iterate_suma()

def iterate_suma3():
    for q in range(4):
        iterate_suma()

def iterate_suma5():
    for q in range(5):
        iterate_suma()

    
def suma():
    vent3 = tk.Tk()
    vent3.title("Suma")
    vent3.geometry("350x400")
    vent3.config(bg="lightblue")
    Td= tk.Label(vent3,text="Bienvenido! al menu de Sumas ",bg="lightblue")
    Nota = tk.StringVar()
    Td2= tk.Label(vent3,text="Elige el numero de Sumas que deseas realizar",bg="lightblue")
    Td.place(x=0,y=0)
    Td2.place(x=0,y=20)
    tk.Button(vent3, text="1", command = iterate_suma, bg="white").place(x=12, y=50)
    tk.Button(vent3, text="2", command = iterate_suma2, bg="white").place(x=47, y=50)
    tk.Button(vent3, text="3", command = iterate_suma3, bg="white").place(x=82, y=50)
    tk.Button(vent3, text="4", command = iterate_suma4, bg="white").place(x=117, y=50)
    tk.Button(vent3, text="5", command = iterate_suma5, bg="white").place(x=152, y=50)
    tk.Button(vent3,text="Siguente" ,bg="lightblue").place(x=150,y=360)
    tk.Button(vent3,text="Cancelar" ,bg="lightblue").place(x=60,y=360)

def iterate_resta():
    minuendo = random.randrange(1, 11)
    sustraendo = random.randrange(1, minuendo + 1)
    resta = Operaciones(minuendo, sustraendo)
    ventr = tk.Tk()
    ventr.title("Resta")
    ventr.geometry("300x350")
    ventr.config(bg = "lightgreen")
    entry = ttk.Entry(ventr)
    entry.place(x=86, y=50)
    tit = tk.Label(ventr, text= resta.__strresta__(), bg = "red", fg ="white", font = ("courier",12), justify="center")
    tit.place(x=63, y=10)
    def comparar():
        if entry.get()== str(resta.resta()):
            tk.Label(ventr,text="CORRECTO",bg="lightgreen").place(x=120, y=150)
            print("¡GOOD!")
        else:
            tk.Label(ventr,text="INCORRECTO",bg="lightgreen").place(x=120, y=150)
            print("¡NOT GOOD!")
        ventr.update_idletasks()
    def close():
        ventr.destroy()
    button = ttk.Button(ventr, text="Verificar",command= comparar)
    buttonq = ttk.Button(ventr, text="Salir",command= close)
    buttonq.place(x=150, y=100)
    button.place(x=71, y=100)

def iterate_resta2():
    for q in range(2):
        iterate_resta()

def iterate_resta3():
    for q in range(3):
        iterate_resta()

def iterate_resta4():
    for q in range(4):
        iterate_resta()

def iterate_resta5():
    for q in range(5):
        iterate_resta()

def resta():
    vent1 = tk.Tk()
    vent1.title("Resta")
    vent1.geometry("350x400")
    vent1.config(bg="lightblue")
    Td= tk.Label(vent1,text="Bienvenido! al menu de Resta ",bg="lightblue")
    Nota = tk.StringVar()
    Td2= tk.Label(vent1,text="Elige el numero de Restas que deseas realizar ",bg="lightblue")
    Td.place(x=0,y=0)
    Td2.place(x=0,y=20)
    tk.Button(vent1, text="1", command = iterate_resta, bg="white").place(x=12, y=50)
    tk.Button(vent1, text="2", command = iterate_resta2,  bg="white").place(x=47, y=50)
    tk.Button(vent1, text="3", command = iterate_resta3,  bg="white").place(x=82, y=50)
    tk.Button(vent1, text="4", command = iterate_resta4,  bg="white").place(x=117, y=50)
    tk.Button(vent1, text="5", command = iterate_resta5,  bg="white").place(x=152, y=50)
    tk.Button(vent1,text="Siguente" ,bg="lightblue").place(x=150,y=360)
    tk.Button(vent1,text="Cancelar" ,bg="lightblue").place(x=60,y=360)   

def iterate_mult():
    factor1 = random.randrange(1, 11)
    factor2 = random.randrange(1, 11)
    producto = Operaciones(factor1, factor2)
    ventm = tk.Tk()
    ventm.title("Multiplicación")
    ventm.geometry("300x350")
    ventm.config(bg = "lightgreen")
    entry = ttk.Entry(ventm)
    entry.place(x=86, y=50)
    tit = tk.Label(ventm, text= producto.__strmult__(), bg = "red", fg ="white", font = ("courier",12), justify="center")
    tit.place(x=63, y=10)
    def comparar():
        if entry.get()== str(producto.mult()):
            tk.Label(ventm,text="CORRECTO",bg="lightgreen").place(x=120, y=150)
            print("¡GOOD!")
        else:
            tk.Label(ventm,text="INCORRECTO",bg="lightgreen").place(x=120, y=150)
            print("¡NOT GOOD!")
        vents.update_idletasks()
    def close():
        vents.destroy()
    button = ttk.Button(ventm, text="Verificar",command= comparar)
    buttonq = ttk.Button(ventm, text="Salir",command= close)
    buttonq.place(x=150, y=100)
    button.place(x=71, y=100)


def iterate_mult2():
    for q in range(2):
        iterate_mult()

def iterate_mult3():
    for q in range(3):
        iterate_mult()

def iterate_mult4():
    for q in range(4):
        iterate_suma()

def iterate_mult5():
    for q in range(5):
        iterate_mult()

    
def mult():
    vent = tk.Tk()
    vent.title("Multiplicacion")
    vent.geometry("350x400")
    vent.config(bg="lightblue")
    Td= tk.Label(vent,text="Bienvenido! al menu de Multiplicaciones ",bg="lightblue")
    Td2= tk.Label(vent,text="Elige el numero de Multiplicaciones que deseas ",bg="lightblue")
    Td.place(x=0,y=0)
    Td2.place(x=0,y=20)
    tk.Button(vent, text="1", command = iterate_mult, bg="white").place(x=12, y=50)
    tk.Button(vent, text="2", command = iterate_mult2, bg="white").place(x=47, y=50)
    tk.Button(vent, text="3", command = iterate_mult3, bg="white").place(x=82, y=50)
    tk.Button(vent, text="4", command = iterate_mult4, bg="white").place(x=117, y=50)
    tk.Button(vent, text="5", command = iterate_mult5, bg="white").place(x=152, y=50)
    tk.Button(vent,text="Siguente" ,bg="lightblue").place(x=150,y=360)
    tk.Button(vent,text="Cancelar" ,bg="lightblue").place(x=60,y=360)
    

def iterate_div():
    numerador = random.randrange(1, 11)
    denominador = random.randrange(1, numerador + 1)
    cociente = Operaciones(numerador, denominador)
    ventd = tk.Tk()
    ventd.title("División")
    ventd.geometry("300x390")
    ventd.config(bg = "lightgreen")
    entry = ttk.Entry(ventd)
    entry.place(x=86, y=50)
    entry2 = ttk.Entry(ventd)
    entry2.place(x=86, y=132)
    tit = tk.Label(ventd, text= cociente.__strdiv__(), bg = "red", fg ="white", font = ("courier",12), justify="center")
    tit.place(x=63, y=10)
    tit2 =tk.Label(ventd, text = cociente.__strres__(), bg = "red", fg ="white", font = ("courier", 12), justify="center")
    tit2.place(x=0, y=90)
    def comparar():
        if entry.get()== str(cociente.div()) and entry2.get()== str(cociente.residuo()):
            tk.Label(ventd,text="CORRECTO",bg="lightgreen").place(x=120, y=212)
            print("¡GOOD!")
        else:
            tk.Label(ventd,text="INCORRECTO",bg="lightgreen").place(x=120, y=212)
            print("¡NOT GOOD!")
        vents.update_idletasks()
    def close():
        vents.destroy()
    button = ttk.Button(ventd, text="Verificar",command= comparar)
    buttonq = ttk.Button(ventd, text="Salir",command= close)
    buttonq.place(x=150, y=172)
    button.place(x=71, y=172)


def iterate_div2():
    for q in range(2):
        iterate_div()

def iterate_div3():
    for q in range(3):
        iterate_div()

def iterate_div4():
    for q in range(4):
        iterate_div()

def iterate_div5():
    for q in range(5):
        iterate_div()
    
def div():
    vent2 = tk.Tk()
    vent2.title("Division")
    vent2.geometry("350x400")
    vent2.config(bg="lightblue")
    Td= tk.Label(vent2,text="Bienvenido! al menu de Divisiones ",bg="lightblue")
    Nota = tk.StringVar()
    Td2= tk.Label(vent2,text="Elige el numero de Divisiones que deseas realizar ",bg="lightblue")
    Td.place(x=0,y=0)
    Td2.place(x=0,y=20)
    tk.Button(vent2, text="1", command = iterate_div, bg="white").place(x=12, y=50)
    tk.Button(vent2, text="2", command = iterate_div2, bg="white").place(x=47, y=50)
    tk.Button(vent2, text="3", command = iterate_div3, bg="white").place(x=82, y=50)
    tk.Button(vent2, text="4", command = iterate_div4, bg="white").place(x=117, y=50)
    tk.Button(vent2, text="5", command = iterate_div5, bg="white").place(x=152, y=50)
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
            

   
ventana = tk.Tk()
ventana.title("Math")
ventana.geometry("550x500")
ventana.config(bg="lightgreen")

ubicar_botones()
label1 = tk.Label(ventana, wraplength= 500, text="!Bienvenido a un curso de matemática elemental! Elige que tipo de curso te gustaría realizar\
     Selecciona alguna de las siguientes opciones  suma - resta - multiplicacion - division: ", font=("courier", 12, "bold"), bg="lightgreen", justify=tk.LEFT)#Ubica el texto anteriormente(linea 10)
label1.place(x=10,y=0)


ventana.mainloop()