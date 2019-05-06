import tkinter as tk
import datetime
import calendar

year = datetime.date.today().year 
month = datetime.date.today().month

def sera():

    elemento=[]

      
    #FUNCIONES DE LOS BOTONES 
    def mesAnterior():
        global month,year
        month-=1
        if month==0:
            month=12
            year-=1
        crear_calendario()
        #calendar_lista()
        
    def mesSiguiente():
        global month,year
        month+=1
        if month==13:
            month=1
            year+=1
        calendario = calendar.Calendar()
        for q in calendario.monthdayscalendar((year+1), (month+1)):
            elemento.append(q)
        A=elemento[0]
        B=elemento[1]
        C=elemento[2]
        D=elemento[3]
        E=elemento[4]
        print(A,B,C,D,E)
        print("=========================================================================")
        leer_lista(A,B,C,D,E)
        crear_calendario()

        
    def AñoAnterior():
        global month,year
        year-=1
        if year==year:
            year-=0
        crear_calendario()
        #calendar_lista()
        
    def AñoSiguiente():
        global month,year
        year+=1
        if year==year:
            year+=0
        crear_calendario()
        #calendar_lista()
        
    def crear_calendario():
      str1 = calendar.month(year,month)
      label1.configure(text=str1)

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
        
    
    def leer_lista(a_list,a_list2,a_list3,a_list4,a_list5):
        romper = False
        for q in a_list:
            e=q-a_list[0]-1
            for i in range(len(a_list)):
                if a_list[i]==0:
                    e+=1                
            u="{0:02d}".format(q)
            a=(70)
            h=(e*56)
            if type(q)is int:
                boton = tk.Button(ventana,text =u,font=("courier", 19, "bold"),bg="lightgreen").place(x=h,y=(a))
            else:
                romper = True
            e+=1
            
        for q in a_list2:
            e=q-a_list2[0]
            u="{0:02d}".format(q)
            a=((1*40)+70)
            h=(e*56)
            if type(q)is int:
                boton = tk.Button(ventana,text =u,font=("courier", 19, "bold"),bg="lightgreen").place(x=e*56,y=(a))
            else:
                romper = True
        for q in a_list3:
            e=q-a_list3[0]
            u="{0:02d}".format(q)
            a=((2*40)+70)
            h=(e*56)
            if type(q)is int:
                boton = tk.Button(ventana,text =u,font=("courier", 19, "bold",),bg="lightgreen").place(x=e*56,y=(a))
            else:
                romper = True
        for q in a_list4:
            e=q-a_list4[0]
            u="{0:02d}".format(q)
            a=((3*40)+70)
            h=(e*56)
            if type(q)is int:
                boton = tk.Button(ventana,text =u,font=("courier", 19, "bold"),bg="lightgreen").place(x=e*56,y=(a))
            else:
                romper = True
        for q in a_list5:
            e=q-a_list5[0]
            u="{0:02d}".format(q)
            a=((4*40)+70)
            h=(e*56)
            if type(q)is int:
                boton = tk.Button(ventana,text =u,font=("courier", 19, "bold"),bg="lightgreen").place(x=e*56,y=(a))
            else:
                romper = True  
            
    def calendar_lista():
        global month, year
        calendario = calendar.Calendar()
        for q in calendario.monthdayscalendar(year, month):
            elemento.append(q)
        A=elemento[0]
        B=elemento[1]
        C=elemento[2]
        D=elemento[3]
        E=elemento[4]
        print(A,B,C,D,E)
        print("=========================================================================")
        leer_lista(A,B,C,D,E)
    
    calendar_lista()


    
    label1 = tk.Label(ventana, text="", font=("courier", 24, "bold"), bg="lightgreen", justify=tk.LEFT)
    label1.grid(row=1,column=1)
    crear_calendario()
    ubicar_botones()

    
ventana = tk.Tk()
ventana.title("Calendario")
ventana.geometry("393x400")
ventana.config(bg="lightgreen")
sera()
ventana.mainloop()













