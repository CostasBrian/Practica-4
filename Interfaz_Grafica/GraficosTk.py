import tkinter as tk
from tkinter import *
import sqlite3


"""-------------------------------------------------------------------------------------------------------------------------"""
'''creo la base de datos'''
miConexion = sqlite3.connect("Peluqueria")
miCursor = miConexion.cursor()
miCursor.execute("CREATE TABLE IF NOT EXISTS PERROS(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_PERRO VARCHAR(30), DUEÑO VARCHAR(30), DOMICILIO VARCHAR (30), TELEFONO INTEGER(15), MOTIVO_DE_VISITA INTEGER(3))")
miConexion.commit()
miConexion.close()

#----------------------------------------------------------------------------------------------------------------------------------------------
"""configuro la ventana raiz"""
raiz = tk.Tk()  
raiz.title("Peluqueria")  
raiz.resizable(False, False) 
raiz.geometry("550x700+70+0")   
raiz.config(bg="black")     

#----------------------------------------------------------------------------------------------------------------------------------------------
def ventana_carga():
    vent_carga= Toplevel()
    vent_carga.title("Carga de Perros")
    vent_carga.geometry("550x350+70+0")
    
    label = Label(vent_carga, text="Nombre del perro: ")
    label.grid(row=0, column=0)
    nombre_perro = Entry(vent_carga, width=15)
    nombre_perro.grid(row=0, column=1)
    print(nombre_perro.get())
    
    label = Label(vent_carga, text="Nombre del dueño: ")
    label.grid(row=1, column=0)
    dueño = Entry(vent_carga, width=15)
    dueño.grid(row=1, column=1)
    
    label = Label(vent_carga, text="Domicilio: ")
    label.grid(row=2, column=0)
    domicilio = Entry(vent_carga, width=15)
    domicilio.grid(row=2, column=1)
    
    label = Label(vent_carga, text="Telefono: ")
    label.grid(row=3, column=0)
    telefono = Entry(vent_carga, width=15)
    telefono.grid(row=3, column=1)
    
    label = Label(vent_carga, text="Motivo de la visita:\n1_Baño  2_Baño y Corte\n")
    label.grid(row=4, column=0)
    motivo = Entry(vent_carga, width=15)
    motivo.grid(row=4, column=1)
    
    dato1 = nombre_perro.get()
    dato2 = dueño.get()
    dato3 = domicilio.get()
    dato4 = telefono.get()
    dato5 = motivo.get()
    
    nuevo_perro = Perro(dato1, dato2, dato3, dato4, dato5)
    
    boton_guardar = Button(vent_carga, text="Guardar", width=25, command = nuevo_perro.cargar_perro)
    boton_guardar.grid(row=7, column=1)
         

#----------------------------------------------------------------------------------------------------------------------------------------------
"""configuro el frame1"""
miFrame = Frame(raiz, width=-550, height=500)   #objeto de clase frame que pertenece a raiz
miFrame.pack()
miFrame.config(bg="gray80")
#miFrame.config(bd=5, relief="solid", cursor="pencil", )
#----------------------------------------------------------------------------------------------------------------------------------------------

'''label dentro de titulo del frame1'''
miLabel= Label(miFrame, text="Bienvenidos a la peluqueria canina", fg="blue", font=("comic sans", 24, "bold"))#texto, color de texto, fuente
miLabel.config(bg ="gray80")
miLabel.grid(row=0, column=0) #posiciona cada objeto
miLabel_2= Label(miFrame, text="Menu de opciones", fg="black", font=("comic sans", 18, "bold"),)
miLabel_2.config(bg ="gray80")
miLabel_2.grid(row=1, column=0) #posiciona cada objeto

'''botones de opcion'''
boton1 = Button(miFrame, text="Cargar perro", width=25, anchor="w", command=ventana_carga)
boton1.grid(row=2, column=0)
boton2 = Button(miFrame, text="Modificar datos de un perro", width=25, anchor="w")
boton2.grid(row=3, column=0)
boton3 = Button(miFrame, text="Borrar un perro", width=25, anchor="w")
boton3.grid(row=4, column=0)
boton4 = Button(miFrame, text="Cargar visit", width=25, anchor="w")
boton4.grid(row=5, column=0)
boton5 = Button(miFrame, text="Mostrar lista completa", width=25, anchor="w")
boton5.grid(row=6, column=0)
botonUn0 = Button(miFrame, text="Cerrar aplicacion", width=25, anchor="w")
botonUn0.grid(row=7, column=0)

'''label de pregunta'''
pregunta = Label(miFrame, text="Por favor seleccione una opcion", fg="black",  font=("comic sans", 10, "bold"))
pregunta.config(bg ="gray80")
pregunta.grid(row=8, column=0)

"""-------------------------------------------------------------------------------------------------------------------------"""
class Perro:
    def __init__(self, nombre_perro, dueño, domicilio, telefono, motivo):
        self.nombre_perro = nombre_perro
        self.dueño = dueño
        self.domicilio = domicilio
        self.telefono = telefono
        self.motivo = motivo
        
    #@staticmethod
    def cargar_perro(self):
        conexion = Conexiones() # se crea objeto conexion de clse conexiones
        conexion.abrirConexion()    # objeto conexion utiliza los metodos de la clase conexiones
        conexion.miCursor.execute("INSERT INTO PERROS VALUES(NULL, '{}', '{}', '{}', '{}', '{}')".format(self.nombre_perro, self.dueño, self.domicilio, self.telefono, self.motivo))
        conexion.miConexion.commit()
        conexion.cerrarConexion()
        print("Perro cargado exitosamente")
        


"""-------------------------------------------------------------------------------------------------------------------------"""
class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Peluqueria")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()

raiz.mainloop()

