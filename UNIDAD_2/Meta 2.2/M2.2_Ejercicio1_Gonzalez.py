"""
NOMBRE: Gonzalez Salas Yuvia Itzel
GRUPO: 951
FECHA: 12 de octubre de 2025
DESCRIPCIÓN:
1. Desarrollar una clase llamada SQLConnect que tenga como atributos: host, user, password, database, driver (Caso SQL SERVER).
	Debe tener los siguientes métodos:
conectar() : Debe conectarse a la base de datos usando los atributos, debe retornar el objeto de conexión.
desconectar(): Debe desconectar la base de datos. No debe retornar nada. Investigar método close().

"""
from mysql.connector import connect,Error

class SQLConnect:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def conectar(self):
        try:
            self.conexion = connect(host=self.host, user=self.user, password= self.password, database= self.database)
            return self.conexion
        except Error as e:
            print("Error en la conexión",e)

    def desconectar(self):
        if self.conexion:
            self.conexion.close()
        else:
            print("No hay conexión por cerrar")

establecer_conexion = SQLConnect("127.0.0.1","root","12345678","olimpiadas")
establecer_conexion.conectar()
establecer_conexion.desconectar()
