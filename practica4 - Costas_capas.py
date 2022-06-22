import sqlite3
"""-------------------------------------------------------------------------------------------------------------------------"""

miConexion = sqlite3.connect("Peluqueria")
miCursor = miConexion.cursor()
miCursor.execute("CREATE TABLE IF NOT EXISTS PERROS(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_PERRO VARCHAR(30) UNIQUE, DUEÑO VARCHAR(30), DOMICILIO VARCHAR (30), TELEFONO INTEGER(15), MOTIVO_BAÑO INTEGER(3), MOTIVO_BAÑOyCORTE INTEGER(3))")
miConexion.commit()
miConexion.close()

"""-------------------------------------------------------------------------------------------------------------------------"""
class ProgramaPrincipal:
    
    def menu(self):
        while True:
            print("\n****Menu de opciones Peluqueria Canina****")
            print("1- Cargar perro")
            print("2- Modificar datos de un perro")
            print("3- Borrar un perro")
            print("4-Cargar visita")
            print("5-Mostrar lista completa")   
            print("0- Salir de menu")
            opcion = int(input("Por favor ingrese una opcion\n"))
            
            if opcion == 1:
                nombre_perro = input("Por favor ingrese el nombre del perro: ")
                dueño = input("Por favor ingrese el nombre del dueño: ")
                domicilio = input("Por favor ingrese el domicilio: ")
                telefono = int(input("Por favor ingrese un telefono: "))
                motivo1 = 0
                motivo2 = 0
                nuevo_perro = Perro(nombre_perro, dueño, domicilio, telefono, motivo1, motivo2)
                nuevo_perro.cargar_perro()     #el perro ingresado utiliza el metodo de carga de datos
                self.menu()
                
                
            if opcion == 2:
                accion = classBusqueda()     #creo objeto accion de clase busqueda  #es necesario??
                perro_buscado = input("ingrese nombre de perro a buscar:  ")
                campo_a_modificar = int(input("que desea modificar?:\n1_domicilio\n2_telefono\n3_ambos\n"))
                accion.buscarPerro(perro_buscado, campo_a_modificar)    #ejecuto metodo de instancia buscarPerro
                self.menu()
                
            if opcion == 3:
                accion = classEliminar()
                eliminar = input("ingrese nombre de perro a eliminar:  ")
                accion.eliminarPerro(eliminar)
                self.menu()
                        
            if opcion == 4:
                accion = motivoVisita()
                nombre = input("ingrese nombre de perro\n")
                visita = int(input("por favor ingrese motivo de la visita:\n1_Baño\n2_Baño y Corte\n"))
                accion.modificarVisita(nombre, visita)
                self.menu
                
            if opcion == 5:
                accion = classMostrar()
                accion.mostrarLista()
                self.menu()
            break
        
"""-------------------------------------------------------------------------------------------------------------------------"""
class Perro:
    def __init__(self, nombre_perro, dueño, domicilio, telefono, motivo1, motivo2):
        self.nombre_perro = nombre_perro
        self.dueño = dueño
        self.domicilio = domicilio
        self.telefono = telefono
        self.motivo1 = motivo1
        self.motivo2 = motivo2
        
    def cargar_perro(self):
        conexion = Conexiones() # se crea objeto conexion de clse conexiones
        conexion.abrirConexion()    # objeto conexion utiliza los metodos de la clase conexiones
        conexion.miCursor.execute("INSERT INTO PERROS VALUES(NULL, '{}', '{}', '{}', '{}', '{}', '{}')".format(self.nombre_perro, self.dueño, self.domicilio, self.telefono, self.motivo1, self.motivo2))
        conexion.miConexion.commit()
        conexion.cerrarConexion()
        print("Perro cargado exitosamente")
        
    def __str__(self):
        return ("\n + {} \n {}, \n {}, \n {}, \n {}, \n {}".format("sfdfsdf", self.dueño, self.domicilio, self.telefono, self.motivo1, self.motivo2))
        
    
"""-------------------------------------------------------------------------------------------------------------------------"""

    
class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Peluqueria")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()


"""-------------------------------------------------------------------------------------------------------------------------"""
class classBusqueda():
    
    def buscarPerro(self, buscado, opc): 
        if opc == 1:
            new_domicilio = input("ingrese nuevo domicilio:  ")
            buscar = Conexiones()
            buscar.abrirConexion()
            buscar.miCursor.execute("UPDATE PERROS SET DOMICILIO= ? WHERE NOMBRE_PERRO = ?", (new_domicilio, buscado))
            buscar.miConexion.commit()
            buscar.cerrarConexion()
        elif opc == 2:
            new_telefono = int(input("ingrese nuevo telefono:  "))
            buscar = Conexiones()
            buscar.abrirConexion()
            buscar.miCursor.execute("UPDATE PERROS SET TELEFONO = ? WHERE NOMBRE_PERRO = ?", (new_telefono, buscado))
            buscar.miConexion.commit()
            buscar.cerrarConexion()
        else:
            new_domicilio = input("ingrese nuevo domicilio:  ")
            new_telefono = int(input("ingrese nuevo telefono:  "))
            buscar = Conexiones()
            buscar.abrirConexion()
            buscar.miCursor.execute("UPDATE PERROS SET DOMICILIO= ?, TELEFONO = ? WHERE NOMBRE_PERRO = ?", (new_domicilio, new_telefono, buscado))
            buscar.miConexion.commit()
            buscar.cerrarConexion()
        print("Datos modificados correctamente")

"""-------------------------------------------------------------------------------------------------------------------------"""

class classEliminar():
    def eliminarPerro(self, eliminar):
        eliminado = Conexiones()
        eliminado.abrirConexion()
        eliminado.miCursor.execute("DELETE FROM PERROS WHERE NOMBRE_PERRO = ?", (eliminar,))
        eliminado.miConexion.commit()
        eliminado.cerrarConexion()     
        print("Datos eliminados correctamente")
 
"""-------------------------------------------------------------------------------------------------------------------------"""
class motivoVisita():
    def modificarVisita(self, nombre, motivo):
        visita = Conexiones()
        visita.abrirConexion()
        if motivo == 1:
            visita.miCursor.execute("UPDATE PERROS SET MOTIVO_BAÑO= 1 WHERE NOMBRE_PERRO = ?", (nombre))
        else:
            visita.miCursor.execute("UPDATE PERROS SET MOTIVO_BAÑOyCORTE = 1 WHERE NOMBRE_PERRO = ?", (nombre))
        visita.miConexion.commit()
        visita.cerrarConexion()
        print("visita ingresada correctamente")
"""-------------------------------------------------------------------------------------------------------------------------"""

class classMostrar():
    def mostrarLista(self):
        mostrar = Conexiones()
        mostrar.abrirConexion()
        mostrar.miCursor.execute("SELECT * FROM PERROS")
        lista = mostrar.miCursor.fetchall()
        print(lista)
        mostrar.miConexion.commit()
        mostrar.cerrarConexion() 
       
"""-------------------------------------------------------------------------------------------------------------------------"""
     
programa = ProgramaPrincipal()  #se crea objeto programa de clase prograam principal
programa.menu()    #el objeto menu utiliza el metodo menu para volver a llamar

"""-------------------------------------------------------------------------------------------------------------------------"""
'''______________________________________________Programa Terminado_________________________________________________________'''