import tkinter as tk
import datetime
import calendar

year = datetime.date.today().year 
month = datetime.date.today().month
def sera():

    elemento=[]
    
    def crear_calendario():
        str1 = calendar.month(year,month)
        label1.configure(text=str1)
    
    #FUNCIONES DE LOS BOTONES 
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
    
    def ubicar_botones():
        BotonMs = tk.Button(ventana,text="Mes Siguiente",command=mesSiguiente ,bg="lightgreen").place(x=203,y=340)
        BotonMa = tk.Button(ventana,text="Mes Anterior",command=mesAnterior, bg="lightgreen").place(x=95,y=340)
        BotonAs = tk.Button(ventana,text="Año Siguiente",command=AñoSiguiente, bg="lightgreen").place(x=230,y=370)
        BotonAa = tk.Button(ventana,text="Año anterior",command=AñoAnterior, bg="lightgreen").place(x=70,y=370)
        BotonX = tk.Button(ventana,text="XOR",bg="lightgreen").place(x=177, y=370)
    
    def Anotar():
        vent = tk.Tk()
        vent.title("Notas")
        vent.geometry("300x400")
        vent.config(bg="lightblue")
        Td= tk.Label(vent,text="Bienvenido! aca podras realizar ",bg="lightblue")
        Td2= tk.Label(vent,text="los apuntes necesarios",bg="lightblue")
        Td.place(x=0,y=0)
        Td2.place(x=0,y=20)
        tk.Button(vent,text="Guardar" ,bg="lightblue").place(x=150,y=360)
        tk.Button(vent,text="Cancelar" ,bg="lightblue").place(x=60,y=360)
        Nota = tk.StringVar()
        texto = tk.Entry(vent, textvariable=Nota).place(x=0,y=80)
        
    
    def leer_lista(a_list):
        print(a_list)          
        for q in a_list:
            for i in range(len(a_list)):
                if q==0:
                    print("X")
                elif q !=0 and q<7:
                    u="{0:02d}".format(i+1)
                    tk.Button(ventana,text=u ,command=Anotar ,font=("courier", 19, "bold"),bg="lightgreen").place(x=224 + i*56,y=70)
                elif q>=2 and q<14:
                    u="{0:02d}".format(i+4)
                    tk.Button(ventana,text=u ,command=Anotar ,font=("courier", 19,"bold"),bg="lightgreen").place(x=0 + i*56,y=110)
        
                elif q>=9 and q<21:
                    u="{0:02d}".format(i+11)
                    tk.Button(ventana,text=u ,command=Anotar ,font=("courier", 19, "bold"),bg="lightgreen").place(x=0+i*56,y=145)
        
                elif q>=16 and q<28:
                    u="{0:02d}".format(i+18)
                    tk.Button(ventana,text=u ,command=Anotar ,font=("courier", 19, "bold"),bg="lightgreen").place(x=0+i*56,y=180)
        
                elif q>=30 and q<=31:
                    u="{0:02d}".format(i+25)
                    tk.Button(ventana,text=u ,command=Anotar ,font=("courier", 19, "bold"),bg="lightgreen").place(x=0+i*56,y=220)
 
    
    def calendar_lista():
        calendario = calendar.Calendar()
        for q in calendario.monthdayscalendar(year, month):
            elemento.append(q)
    
    calendar_lista()
    #print(elemento)
    A=elemento[0]
    B=elemento[1]
    C=elemento[2]
    D=elemento[3]
    E=elemento[4]

    
    label1 = tk.Label(ventana, text="", font=("courier", 24, "bold"), bg="lightgreen", justify=tk.LEFT)
    label1.grid(row=1,column=1)
    crear_calendario()
    ubicar_botones()
    
    leer_lista(A)
    leer_lista(B)
    leer_lista(C)
    leer_lista(D)
    leer_lista(E)
    
ventana = tk.Tk()
ventana.title("Calendario")
ventana.iconbitmap(r"C:\Users\DELL\Desktop\Programacion\Calendario\calculator-512.ico")
ventana.geometry("390x400")
ventana.config(bg="lightgreen")
sera()
ventana.mainloop()
