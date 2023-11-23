import pyodbc
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def conectar():
    try:
        conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-HIESJ07;DATABASE=Almacén;Trusted_Connection=yes')
        print('La conexión fue exitosa')
        return conexion
    except Exception as ex:
        messagebox.showerror("Error", "La conexión dio error")

def agregar_producto(Id, precio, descripcion):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"exec productos_datos '{Id}', '{precio}', '{descripcion}'")
        conexion.commit()
        messagebox.showinfo('Información','El producto fue agregado a la base de datos')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")

def eliminar_producto(Id):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"exec eliminar_datos '{Id}'")
        conexion.commit()
        messagebox.showinfo('Información','El producto fue eliminado de la base de datos')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")

def actualizar_producto(Id, precio, descripcion):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"exec actualizar_datos '{Id}', '{precio}', '{descripcion}'")
        conexion.commit()
        messagebox.showinfo('Información','El producto fue actualizado correctamente')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")

def buscar_producto(descripcion, tabla):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM Productos WHERE descripcion LIKE '%{descripcion}%' ORDER BY Id DESC")
        resultados = cursor.fetchall()
        if resultados:
            tabla.delete(*tabla.get_children())
            for resultado in resultados:
                tabla.insert("", "end", values=(*resultado,))
        else:
            messagebox.showinfo('Información','No se encontraron productos con la descripción especificada')
    except ValueError:
        messagebox.showerror("Error", "Los datos no son correctos")