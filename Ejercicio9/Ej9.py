# El ejercicio consistirá en crear, leer, actualizar y eliminar (CRUD) registros de estudiantes en una base de datos utilizando una interfaz gráfica.
# Base de Datos:
# CREATE DATABASE escuela;
# USE escuela;
# CREATE TABLE estudiantes (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     nombre VARCHAR(100),
#     edad INT,
#     curso VARCHAR(100)
# );
# La aplicación tendrá 4 botones: “Agregar Estudiante”, “Actualizar Estudiante”, “Eliminar Estudiante” y “Limpiar Campos”
# Ejemplo de uso:
# 1.	Al iniciar la aplicación, se mostrarán los estudiantes existentes en la base de datos en la lista.
# 2.	Puedes agregar nuevos estudiantes usando el botón "Agregar Estudiante".
# 3.	Puedes seleccionar un estudiante de la lista y luego actualizar sus datos con el botón "Actualizar Estudiante".
# 4.	También puedes eliminar estudiantes seleccionados con el botón "Eliminar Estudiante".


#Importamos para utilizarlos
import tkinter as tk
from tkinter import ttk, messagebox
import mariadb
import sys


#Método para conectar a base de datos
def conectarBd():
    try:
        return mariadb.connect(
            user="escuela",
            password="root",
            host="127.0.0.1",
            port=3306,
            database="escuela",
        )
    except mariadb.Error as e:
        print("Error conectando a la base de datos: ", e)
        sys.exit(1)

conexion = conectarBd()
cursor = conexion.cursor()


#Método para obtener a los estudiantes seleccionados
def obtenerEstudiantes():
    cursor.execute("select * from estudiantes")
    return cursor.fetchall()


#Método para actualizar a los estudiantes seleccionados
def actualizarLista():
    lista_estudiantes.delete(*lista_estudiantes.get_children())
    for estudiante in obtenerEstudiantes():
        lista_estudiantes.insert("", "end", values=estudiante)


#Métodos para crear un nuevo estudiante
def agregarEstudiante():
    nombre, edad, curso = entry_nombre.get(), entry_edad.get(), entry_curso.get()
    if not (nombre and edad and curso):
        messagebox.showerror("Error", "todos los campos son obligatorios")
        return
    try:
        cursor.execute("insert into estudiantes (nombre, edad, curso) values (?, ?, ?)", (nombre, edad, curso))
        conexion.commit()
        actualizarLista()
        limpiarCampos()
    except mariadb.Error as e:
        print("Error al crear usuario: ", e)


#Métodos para crear un nuevo estudiante
def seleccionarEstudiante(event):
    seleccionado = lista_estudiantes.focus()
    valores = lista_estudiantes.item(seleccionado, "values")
    if valores:
        entry_id.config(state="normal")
        entry_id.delete(0, tk.END)
        entry_id.insert(0, valores[0])
        entry_id.config(state="readonly")
        entry_nombre.delete(0, tk.END)
        entry_nombre.insert(0, valores[1])
        entry_edad.delete(0, tk.END)
        entry_edad.insert(0, valores[2])
        entry_curso.delete(0, tk.END)
        entry_curso.insert(0, valores[3])


#Métodos para actualizar a los estudiantes seleccionados
def actualizarEstudiante():
    estudiante_id = entry_id.get()
    nombre, edad, curso = entry_nombre.get(), entry_edad.get(), entry_curso.get()
    if not estudiante_id:
        messagebox.showerror("Error", "selecciona un estudiante")
        return
    try:
        cursor.execute("update estudiantes set nombre=?, edad=?, curso=? where id=?", (nombre, edad, curso, estudiante_id))
        conexion.commit()
        actualizarLista()
        limpiarCampos()
    except mariadb.Error as e:
        print("Error al actualizar usuario: ", e)


#Métodos para eliminar a los estudiantes seleccionados
def eliminarEstudiante():
    estudiante_id = entry_id.get()
    if not estudiante_id:
        messagebox.showerror("Error", "selecciona un estudiante")
        return
    try:
        cursor.execute("delete from estudiantes where id=?", (estudiante_id))
        conexion.commit()
        actualizarLista()
        limpiarCampos()
    except mariadb.Error as e:
        print("Error al eliminar usuario: ", e)


#Métodos para limpiar a los campos de los label seleccionados
def limpiarCampos():
    entry_id.config(state="normal")
    entry_id.delete(0, tk.END)
    entry_id.config(state="readonly")
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_curso.delete(0, tk.END)


# Crear la interfaz
tk_app = tk.Tk()
tk_app.title("Estudiantes")

#Id label
tk.Label(tk_app, text="Id").grid(row=0, column=0)
entry_id = tk.Entry(tk_app, state="readonly")
entry_id.grid(row=0, column=1)

#Nombre label
tk.Label(tk_app, text="Nombre").grid(row=1, column=0)
entry_nombre = tk.Entry(tk_app)
entry_nombre.grid(row=1, column=1)

#Edad label
tk.Label(tk_app, text="Edad").grid(row=2, column=0)
entry_edad = tk.Entry(tk_app)
entry_edad.grid(row=2, column=1)

#Curso label
tk.Label(tk_app, text="Curso").grid(row=3, column=0)
entry_curso = tk.Entry(tk_app)
entry_curso.grid(row=3, column=1)

#Botón agregar
btn_agregar = tk.Button(tk_app, text="Agregar estudiante", command=agregarEstudiante)
btn_agregar.grid(row=4, column=0, columnspan=2)

#Botón actualizar
btn_actualizar = tk.Button(tk_app, text="Actualizar estudiante", command=actualizarEstudiante)
btn_actualizar.grid(row=5, column=0, columnspan=2)

#Botón eliminar
btn_eliminar = tk.Button(tk_app, text="Eliminar estudiante", command=eliminarEstudiante)
btn_eliminar.grid(row=6, column=0, columnspan=2)

#Botón limpiar
btn_limpiar = tk.Button(tk_app, text="Limpiar campos", command=limpiarCampos)
btn_limpiar.grid(row=7, column=0, columnspan=2)

lista_estudiantes = ttk.Treeview(tk_app, columns=("Id", "Nombre", "Edad", "Curso"), show="headings")
lista_estudiantes.heading("Id", text="Id")
lista_estudiantes.heading("Nombre", text="Nombre")
lista_estudiantes.heading("Edad", text="Edad")
lista_estudiantes.heading("Curso", text="Curso")
lista_estudiantes.bind("BotonSeleccionar", seleccionarEstudiante)
lista_estudiantes.grid(row=8, column=0, columnspan=2)

actualizarLista()
tk_app.mainloop()
