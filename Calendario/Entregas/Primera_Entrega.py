import tkinter as tk
import datetime
import calendar

#VALORES DE LAS VARIABLES PRINCIPALES 
year = datetime.date.today().year
month = datetime.date.today().month

"""
Esta funcion ubica un texto en la interfaz grafica
"""
def crear_calendario():
	str1 = calendar.month(year,month)
	label1.configure(text=str1)


#FUNCIONES DE LOS BOTONES 
"""
Se busca interactuar con la interfaz grafica de manera adecuada y facil, 
definiendo los comandos que se usaran en los botones que se ubicaran en la ventana.

"""
def mesAnterior():
	global month,year
	month-=1
	if month==0:
		month=12
		year-=1
	crear_calendario()	

def mesSiguiente():
	global month,year
	month+=1
	if month==13:
		month=1
		year+=1
	crear_calendario()	

def AñoAnterior():
	global month,year
	year-=1
	if year==year:
		year-=0
	crear_calendario()	

def AñoSiguiente():
	global month,year
	year+=1
	if year==year:
		year+=0  	
	crear_calendario()	

#GRAFICAR LOS BOTONES 
"""
Esta funcion ubica espacialmente los botones con cada uno de sus comandos para asi interactuar 
mucho mas facil y rapido.

"""
def ubicar_botones():
    BotonMs = tk.Button(ventana,text="Mes Siguiente",command=mesSiguiente,bg="lightgreen").place(x=195,y=340)
    BotonMa = tk.Button(ventana,text="Mes Anterior",command=mesAnterior,bg="lightgreen").place(x=113,y=340)
    BotonAs = tk.Button(ventana,text="Año Siguiente",command=AñoSiguiente,bg="lightgreen").place(x=218,y=370)
    BotonAa = tk.Button(ventana,text="Año anterior",command=AñoAnterior,bg="lightgreen").place(x=100,y=370)
    BotonX = tk.Button(ventana,text="XOR",bg="lightgreen").place(x=180,y=370)

#SE GENERA LA VENTANA
"""
Con ayuda de la interfaz grafica Tkinter se cra una ventana, con un tamaño  y caracteristicas elegidas 
para mejor visualizacion por parte de el usuario 
"""
ventana = tk.Tk()
ventana.title("Calendario")
ventana.geometry("390x400")
ventana.config(bg="lightgreen")

label1 = tk.Label(ventana, text="", font=("courier", 24, "bold"), bg="lightgreen", justify=tk.LEFT)#Ubica el texto anteriormente(linea 10)
label1.grid(row=1,column=1)

ubicar_botones()
crear_calendario()

ventana.mainloop()