import calendar
import datetime
import tkinter as tk

 
class Calendario:
    def __init__(self, Ventana, values):
        self.values = values
        self.Ventana = Ventana
        self.Ventana.config(bg="lightgreen")
        self.cal = calendar.TextCalendar(calendar.SUNDAY)
        self.year = datetime.date.today().year
        self.month = datetime.date.today().month
        self.day = datetime.date.today().day
        self.wid = []
        self.day_selected = 1
        self.month_selected = self.month
        self.year_selected = self.year
        self.day_selected = self.day
        self.day_name = ''
         
        self.Imprimir_Cal(self.year, self.month)
         
    def Lipmiar(self):
        for w in self.wid[:]:
            w.grid_forget()
            #w.destroy()
            self.wid.remove(w)
     
    def Mes_Anterior(self):
        if self.month > 1:
            self.month -= 1
        else:
            self.month = 12
            self.year -= 1
        #self.selected = (self.month, self.year)
        self.Lipmiar()
        self.Imprimir_Cal(self.year, self.month)
 
    def Mes_Siguiente(self):
        if self.month < 12:
            self.month += 1
        else:
            self.month = 1
            self.year += 1
         
        #self.selected = (self.month, self.year)
        self.Lipmiar()
        self.Imprimir_Cal(self.year, self.month)
    
    def AñoAnterior():
    	self.year-=1
    	if self.year==self.year:
    		self.year-=0

    def AñoSiguiente():
    	self.year+=1
    	if self.year==self.year:
    		self.year+=0  	

         
    def Seleccionar(self, day, name):
        self.day_selected = self.day
        self.month_selected = self.month
        self.year_selected = self.year
        self.day_name = name
        self.vent = tk.Tk()
        self.vent.title("Notas")
        self.vent.geometry("300x400")
        self.vent.config(bg="lightblue")
        Td= tk.Label(self.vent,text="Bienvenido! aca podras realizar ",bg="lightblue",font=("courier", 10, "bold"))
        Td.grid(row=1,column=0)
        Td2= tk.Label(self.vent,text="los apuntes necesarios",bg="lightblue",font=("courier", 10, "bold"))
        Td2.grid(row=2,column=0)
         
        #data
        self.values['day_selected'] = self.day
        self.values['month_selected'] = self.month
        self.values['year_selected'] = self.year
        self.values['day_name'] = name
        self.values['month_name'] = calendar.month_name[self.month_selected]
        self.Lipmiar()
        self.Imprimir_Cal(self.year, self.month)
         
    def Imprimir_Cal(self, y, m):

        Mes_Anterior = tk.Button(self.Ventana,bg="lightgreen", font=("courier", 10, "bold"), text='Mes Anterior', command=self.Mes_Anterior)
        self.wid.append(Mes_Anterior)
        Mes_Anterior.grid(row=9, column=1)

        Mes_Siguiente = tk.Button(self.Ventana,bg="lightgreen", font=("courier", 10, "bold"), text='Mes Siguiente', command=self.Mes_Siguiente)
        self.wid.append(Mes_Siguiente)
        Mes_Siguiente.grid(row=9, column=5)
         
        Mes = tk.Label(self.Ventana,bg="lightgreen", font=("courier", 24, "bold"), height=2, text='{}   {}'.format(calendar.month_abbr[m], str(y)))
        self.wid.append(Mes)
        Mes.grid(row=0, column=2, columnspan=3)
         
         
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        for num, name in enumerate(days):
            t = tk.Label(self.Ventana,bg="lightgreen", font=("courier", 24, "bold"), text=name[:3])
            self.wid.append(t)
            t.grid(row=1, column=num)
         
        for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
            for d, day in enumerate(week):
                if day:
                    #print(calendar.day_name[day])
                    u="{0:02d}".format(day)
                    b = tk.Button(self.Ventana,bg="lightgreen", text=u, font=("courier", 24, "bold"), command=lambda day=day:self.Seleccionar(day, calendar.day_name[(day-1) % 7]))
                    self.wid.append(b)
                    b.grid(row=w, column=d)
                     
        Fecha = tk.Label(self.Ventana,bg="lightgreen", font=("courier", 24, "bold"), height=2, text='{} {} {} {}'.format(
            self.day_name, calendar.month_name[self.month_selected], self.day_selected, self.year_selected))
        self.wid.append(Fecha)
        Fecha.grid(row=8, column=0, columnspan=7)
         
        ok = tk.Button(self.Ventana,bg="lightgreen", font=("courier", 15, "bold") , width=5, text='OK', command=self.Cerrar)
        self.wid.append(ok)
        ok.grid(row=9, column=2, columnspan=3, pady=10)
         
    def Cerrar(self):
        self.Ventana.destroy()
 
 
if __name__ == '__main__':
 
    class Control:
        def __init__(self, Ventana):
            self.Ventana = Ventana
            self.Abrir_Cale_Btn = tk.Button(self.Ventana, text='Abrir Calendario',command=self.Crear_calendario,bg="lightgreen")
            self.Cerrar_Btn = tk.Button(self.Ventana, text='Cancelar',command=self.Cerrar ,bg="lightgreen")
            self.Abrir_Cale_Btn.place(x=80,y=10)
            self.Cerrar_Btn.place(x=100,y=50)
            self.data = {}
             
        def Crear_calendario(self):
            child = tk.Toplevel()
            cal = Calendario(child, self.data)
             
        def Cerrar(self):
            self.Ventana.destroy()
             
 
    Init_Win = tk.Tk()
    Init_Win.title("Calendario")
    Init_Win.geometry("250x100")
    Init_Win.config(bg="lightgreen")
    Calendar = Control(Init_Win)
    Init_Win.mainloop()
