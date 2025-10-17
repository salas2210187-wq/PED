"""
NOMBRE: Gonzalez Salas Yuvia Itzel
GRUPO: 951
FECHA: 12 de octubre de 2025
DESCRIPCIÓN:
4. Desarrollar una clase llamada ResultadosSQL que herede de  SQLConnect. Debe agregar los atributos correspondientes de la clase padre.
Debe agregar los siguientes métodos:
a. insertar(idOlimpiada, idPais, idGenero, oro, plata, bronce): Método para insertar datos en la Tabla Resultados, debe recibir como parámetro las columnas de la tabla y debe retornar True si se inserta el dato o False en caso contrario.
b. editar(idOlimpiada, idPais, idGenero, oro, plata, bronce): Método para editar oro, plata, bronce en la Tabla Resultados. Validar que sean valores enteros positivos.
c. eliminar(idOlimpiada, idPais, idGenero): Método para eliminar un elemento de la Tabla Resultados. Debe tener como parámetro la llave primaria compuesta, retorna True si logró eliminarse y False en caso contrario.
d. consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro de la Tabla Resultados. Ejemplo: “idPais = 1” , “idPais = 1 and idOlimpiada=2”

"""

from UNIDAD_2.Meta2.Ejercicio1 import SQLConnect
from mysql.connector import Error

class ResultadosSQL(SQLConnect):
    def __init__(self):
        super().__init__(
            host="127.0.0.1",
            user="root",
            password="12345678",
            database="olimpiadas"
        )
    def insertar(self,idOlimpiada, idPais, idGenero, oro, plata, bronce):
        try:
            #Conectar
            conexion = self.conectar()
            cursor = conexion.cursor()

            #Ejecutar comandos de SQL
            sql = "INSERT INTO Resultados (idOlimpiada, idPais, idGenero, oro, plata, bronce) VALUES (%s, %s, %s, %s, %s, %s)"
            valores = (idOlimpiada, idPais, idGenero, oro, plata, bronce)
            cursor.execute(sql,valores)
            conexion.commit()
            print("Los datos se insertaron correctamente")
            cursor.close()
            return True

        except Error as e:
            print("Error al insertar los datos: ", e)
            return False

        finally:
            self.desconectar()

    def editar(self,idOlimpiada, idPais, idGenero, oro, plata, bronce):
        try:
            #Conectar
            conexion = self.conectar()
            cursor = conexion.cursor()

            #Validar que sean valores enteros positivos
            if idOlimpiada > 0 and idPais > 0 and idGenero > 0 and oro > 0 and plata > 0 and bronce > 0:
                #Ejecutar comandos de SQL
                sql = "UPDATE Resultados SET oro = %s, plata = %s, bronce = %s WHERE idOlimpiada = %s AND idPais = %s AND idGenero = %s"
                valores = (oro, plata, bronce, idOlimpiada, idPais,idGenero)
                cursor.execute(sql, valores)
                conexion.commit()
                print(f"Los datos se actualizaron correctamente")
                cursor.close()
                return True

            else:
                print("Los valores no son enteros positivos")
                return False

        except Error as e:
            print("Error al editar los datos:", e)
            return False

        finally:
            self.desconectar()

    def eliminar(self,idOlimpiada, idPais, idGenero):
        try:
            #Conectar
            conexion = self.conectar()
            cursor = conexion.cursor()

            #Ejecutar comandos de SQL
            sql = "DELETE FROM Resultados WHERE idOlimpiada = %s AND idPais = %s AND idGenero = %s"
            valores = (idOlimpiada, idPais,idGenero)
            cursor.execute(sql, valores)
            conexion.commit()
            print(f"Los datos se eliminaron correctamente")
            cursor.close()
            return True

        except Error as e:
            print("Error al eliminar los datos:", e)
            return False

        finally:
            self.desconectar()

    def consultar(self,filter):
        try:
            #Conectar
            conexion = self.conectar()
            cursor = conexion.cursor()

            #Validar si hay filtro
            if filter:
                sql = "SELECT * FROM Resultados WHERE " + filter
                cursor.execute(sql)

            else:
                sql = "SELECT * FROM Resultados"
                cursor.execute(sql)

            #Utilizar fetchall para traer todos las filas que cumplen con la condicion de la consulta
            resultados = cursor.fetchall()
            cursor.close()
            return resultados

        except Error as e:
            print("Error en la consulta:", e)

        finally:
            self.desconectar()

resultado = ResultadosSQL()
#insertar
resultado.insertar(1, 1, 1, 3, 2, 1)
resultado.insertar(2, 2, 2, 6, 4, 2)
#consultar
consulta = resultado.consultar("idPais = 1")
print(consulta)
#editar
resultado.editar(1, 1, 1, 5, 4, 3)
#eliminar
resultado.eliminar(1, 1, 1)
#consultar
consulta2 = resultado.consultar("idPais = 2 and idOlimpiada = 2")
print(consulta2)