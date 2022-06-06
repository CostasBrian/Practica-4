import sqlite3

miConexion = sqlite3.connect("Peluqueria")
miCursor = miConexion.cursor()
miCursor.execute("CREATE TABLE IF NOT EXISTS PERROS(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_PERRO VARCHAR(30) UNIQUE, DUEÑO VARCHAR(30), DOMICILIO VARCHAR (30), TELEFONO INTEGER(15), MOTIVO_DE_VISITA INTEGER(3))")
miConexion.commit()
miConexion.close()


class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Peluqueria")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()