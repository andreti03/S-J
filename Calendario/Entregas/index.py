from tkinter import ttk
from tkinter import *
import Calendario
import sqlite3

class Product:
    # connection dir property
    db_name = "database.db"

    def __init__(self, window):
        # Initializations 
        self.wind = window
        self.wind.title("ANOTAR")
    
        # Creating a Frame Container 
        frame = LabelFrame(self.wind, text = "Registro de actividades")
        frame.grid(row = 0, column = 0, columnspan = 5, pady = 20)

        # Fecha
        Label(frame, text = "Fecha: ").grid(row = 1, column = 0)
        self.Fecha = Entry(frame)
        self.Fecha.grid(row = 1, column = 1)

        # Actividad
        Label(frame, text = "Actividad: ").grid(row = 2, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 2, column = 1)

        # Descripcion
        Label(frame, text = "Descripción: ").grid(row = 3, column = 0)
        self.descri = Entry(frame)
        self.descri.grid(row = 3, column = 1) 

        # Button Add Product 
        ttk.Button(frame, text = "Guardar", command = self.add_activ).grid(row = 4, columnspan = 2, sticky = W + E)

        # Output Messages 
        self.message = Label(self.wind,text = "", fg = "red")
        self.message.grid(row = 4, column = 0, columnspan = 2, sticky = W + E)

        # Table
        self.columnas = ("#0","#1","#2") 
        self.tree = ttk.Treeview(self.wind,height = 10, columns = self.columnas)
        self.tree.grid(row = 5, column = 0, columnspan = 2)
        self.tree.heading("#0", text = "Actividad", anchor = CENTER)
        self.tree.heading("#1", text = "Descripción", anchor = CENTER)
        self.tree.heading("#2", text = "Fecha", anchor = CENTER)

        # Buttons
        ttk.Button(self.wind, text = "Eliminar", command = self.delete_activ).grid(row = 6, column = 0, sticky = W + E)
        ttk.Button(self.wind, text = "Editar", command = self.edit_activ).grid(row = 6, column = 1, sticky = W + E)

        # Filling the Rows
        self.get_products()

    # Function to Execute Database Querys
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    # Get Products from Database
    def get_products(self):
        # cleaning Table 
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = "SELECT * FROM product ORDER BY name DESC"
        db_rows = self.run_query(query)
        # filling data
        for row in db_rows:
            self.tree.insert("", 0, text = row[1], values = row[2])

    # User Input Validation
    def validation(self):
        return len(self.name.get()) != 0 and len(self.descri.get()) != 0 

    def add_activ(self):
        if self.validation():
            query = "INSERT INTO product VALUES(NULL, ?, ?)"
            parameters =  (self.name.get(), self.descri.get())
            self.run_query(query, parameters)
            self.message["text"] = "La actividad {} se agrego Correctamente".format(self.name.get())
            self.name.delete(0, END)
            self.descri.delete(0, END)
        else:
            self.message["text"] = "Actividad y Descripción necesaria"
        self.get_products()

    def delete_activ(self):
        self.message["text"] = ""
        try:
           self.tree.item(self.tree.selection())["text"][0]
        except IndexError as e:
            self.message["text"] = "Señale la actividad a eliminar"
            return
        self.message["text"] = ""
        name = self.tree.item(self.tree.selection())["text"]
        query = "DELETE FROM product WHERE name = ?"
        self.run_query(query, (name, ))
        self.message["text"] = "Actividad {} eliminada correctamente".format(name)
        self.get_products()

    def edit_activ(self):
        self.message["text"] = ""
        try:
            self.tree.item(self.tree.selection())["values"][0]
        except IndexError as e:
            self.message["text"] = "Por favor, seleccione la actividad"
            return
        name = self.tree.item(self.tree.selection())["text"]
        old_descri = self.tree.item(self.tree.selection())["values"][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = "Editar Actividad"
        # Old Name
        Label(self.edit_wind, text = "Actividad anterior: ").grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = name), state = "readonly").grid(row = 0, column = 2)
        # New Name
        Label(self.edit_wind, text = "Nueva Actividad: ").grid(row = 1, column = 1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row = 1, column = 2)

        # Old Price 
        Label(self.edit_wind, text = "Descripción anterior:").grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_descri), state = "readonly").grid(row = 2, column = 2)
        # New Price
        Label(self.edit_wind, text = "Nueva descripción: ").grid(row = 3, column = 1)
        new_descrip= Entry(self.edit_wind)
        new_descrip.grid(row = 3, column = 2)

        ttk.Button(self.edit_wind, text = "Finalizar", command = lambda: self.edit_records(new_name.get(), name, new_descrip.get(), old_descri)).grid(row = 4, column = 2, sticky = W)
        self.edit_wind.mainloop()

    def edit_records(self, new_name, name, new_descrip, old_descri):
        query = "UPDATE product SET name = ?, price = ? WHERE name = ? AND price = ?"
        parameters = (new_name, new_descrip,name, old_descri)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message["text"] = " {} Se ha editado correctamente".format(name)
        self.get_products()



