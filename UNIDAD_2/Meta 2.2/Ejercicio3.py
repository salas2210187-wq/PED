"""
NOMBRE: Gonzalez Salas Yuvia Itzel
GRUPO: 951
FECHA: 12 de octubre de 2025
DESCRIPCIÓN:
3. Desarrollar una clase llamada OlimpiadaSQL que herede de  SQLConnect. Debe agregar los atributos correspondientes de la clase padre.
Debe agregar los siguientes métodos:
a. insertar(id, year): Método para insertar datos en la Tabla Olimpiada, debe recibir como parámetro las columnas de la tabla y debe retornar True si se inserta el dato o False en caso contrario.
b. editar(id, year_nuevo): Método para editar el año en la Tabla Olimpiada. Validar que el año no exista en la tabla.
c. eliminar(id): Método para eliminar un elemento de la Tabla Olimpiada. Debe tener como parámetro la llave primaria, retorna True si logró eliminarse y False en caso contrario.
d. consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro de la Tabla Olimpiada. Ejemplo: “id = 1” , “year > 1990”

"""
from UNIDAD_2.Meta2.Ejercicio1 import SQLConnect
from mysql.connector import Error

class OlimpiadaSQL(SQLConnect):
    def __init__(self):
        super().__init__(
            host="127.0.0.1",
            user="root",
            password="12345678",
            database="olimpiadas"
        )

    def insertar(self, year):
        try:
            #Conectar
            conexion = self.conectar()
            cursor = conexion.cursor()

            #Ejecutar comandos de SQL
            sql = "INSERT INTO Olimpiada (year_olimpiada) VALUES (%s)" #al estar declarado en mysql como auto_increment, no se pone el id
            valores = (year,) #cuando una tupla tiene un unico valor, porque si no, lo toma como valor entero y va a marcar error
            cursor.execute(sql,valores)
            conexion.commit()
            print("Los datos se insertaron correctamente")
            cursor.close()
            return True

        except Error as e:
            print("Error al insertar los datos:", e)
            return False

        finally:
            self.desconectar()

    def editar(self,id, year_nuevo):
        try:
            #Conectar
            conexion = self.conectar()
            cursor = conexion.cursor()

            #Validar que no exista el nombre
            validar = "SELECT COUNT(*) FROM Olimpiada WHERE year_olimpiada = %s"
            valor_validado = (year_nuevo,)
            cursor.execute(validar, valor_validado)
            resultado = cursor.fetchone()[0]

            #Si es 1, no se edita porque ya existe
            if resultado > 0:
                print("El año ya existe")
                return False

            #Si no es, se puede editar
            else:
                #Ejecutar comandos de SQL
                sql = "UPDATE Olimpiada SET year_olimpiada = %s WHERE id = %s"
                valores = (year_nuevo, id)
                cursor.execute(sql, valores)
                conexion.commit()
                print(f"El año con ID {id} se actualizó correctamente")
                cursor.close()
                return True

        except Error as e:
            print("Error al editar el año:", e)
            return False

        finally:
            self.desconectar()

    def eliminar(self,id):
        try:
            #Conectar
            conexion = self.conectar()
            cursor = conexion.cursor()

            #Ejecutar comandos de SQL
            sql = "DELETE FROM Olimpiada WHERE id = %s"
            valores = (id,)  #cuando una tupla tiene un unico valor, porque si no, lo toma como valor entero y va a marcar error
            cursor.execute(sql, valores)
            conexion.commit()
            print(f"El año con ID {id} se eliminó correctamente")
            cursor.close()
            return True

        except Error as e:
            print("Error al eliminar el año:", e)
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
                #Ejecutar comandos de SQL
                sql = "SELECT * FROM Olimpiada WHERE year_olimpiada = %s"
                valores = (filter,) #cuando una tupla tiene un unico valor, porque si no, lo toma como valor entero y va a marcar error
                cursor.execute(sql, valores)

            else:
                sql = "SELECT * FROM Olimpiada"
                cursor.execute(sql)

            #Utilizar fetchall para traer todos las filas que cumplen con la condicion de la consulta
            resultados = cursor.fetchall()
            cursor.close()
            return resultados

        except Error as e:
            print("Error en la consulta:", e)

        finally:
            self.desconectar()

olimpiada = OlimpiadaSQL()
#insertar
olimpiada.insertar(2022)
olimpiada.insertar(2024)
#consultar
consulta = olimpiada.consultar(2022)
print(consulta)
#editar
olimpiada.editar(1, 2028)
#eliminar
olimpiada.eliminar(1)
#consultar
consulta2 = olimpiada.consultar(2024)
print(consulta2)