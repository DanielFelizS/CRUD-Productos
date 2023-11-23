from tkinter import *
from tkinter import ttk
import conexion

class interfaz:
    def __init__(self, app):
        self.app = app 
        self.app.title('Productos + SQL')
        self.app.geometry("1000x500")
        self.app.resizable(False , False)
        self.elementos()
    
    def elementos(self):
        label_1 = Label(self.app, text = 'Id', fg = '#1e90ff')
        label_1.pack()
        self.Id = Entry(self.app, width = 30)
        self.Id.pack()
        label_2 = Label(self.app, text = 'Precio', fg = '#1e90ff')
        label_2.pack()
        self.Precio = Entry(self.app, width = 30)
        self.Precio.pack()
        label_3 = Label(self.app, text = 'Descripción', fg = '#1e90ff')
        label_3.pack()
        self.Descrip = Entry(self.app, width = 30)
        self.Descrip.pack()
        Agregar = Button(self.app, text = 'Agregar', command = self.agregar_producto)
        Agregar.pack()
        Eliminar = Button(self.app, text = 'Eliminar', command = self.eliminar_producto)
        Eliminar.pack()
        Actualizar = Button(self.app, text = 'Actualizar', command = self.actualizar_producto)
        Actualizar.pack()
        Buscar = Button(self.app, text = "Buscar", command = self.buscar_producto)
        Buscar.pack()
        self.tabla = ttk.Treeview(self.app, columns=("Id","Precio", "Descripcion"), height = 15)
        self.tabla.heading("Id", text="Id")
        self.tabla.heading("Precio", text="Precio")
        self.tabla.heading("Descripcion", text="Descripcion")
        self.tabla.pack()

    def agregar_producto(self):
        iD = self.Id.get()
        precio = self.Precio.get()
        descripcion = self.Descrip.get()
        conexion.agregar_producto(iD, precio, descripcion)
        self.tabla.insert("", "end", values=(iD, precio, descripcion))
    
    def eliminar_producto(self):
        iD = self.Id.get()
        conexion.eliminar_producto(iD)
        precio = self.Precio.get()
        descripcion = self.Descrip.get()
        item = self.tabla.selection()[0]
        self.tabla.delete(item)
    
    def actualizar_producto(self):
        iD = self.Id.get()
        precio = self.Precio.get()
        descripcion = self.Descrip.get()
        conexion.actualizar_producto(iD, precio, descripcion)
        item = self.tabla.selection()[0]
        self.tabla.item(item, values=(iD, precio, descripcion))

    def buscar_producto(self):
        descripcion = self.Descrip.get()
        conexion.buscar_producto(descripcion, self.tabla)

obj = interfaz(Tk())
obj.app.mainloop()
