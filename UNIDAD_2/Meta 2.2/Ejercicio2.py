"""
NOMBRE: Gonzalez Salas Yuvia Itzel
GRUPO: 951
FECHA: 12 de octubre de 2025
DESCRIPCIÓN:
2. Desarrollar una clase llamada PaisSQL que herede de  SQLConnect. Debe agregar los atributos correspondientes de la clase padre.
Debe agregar los siguientes métodos:
a. insertar(id, nombre): Método para insertar datos en la Tabla Pais, debe recibir como parámetro las columnas de la tabla y debe retornar True si se inserta el dato o False en caso contrario.
b. editar(id, nombre_nuevo): Método para editar el nombre en la Tabla País. Validar que nombre no exista en la tabla.
c. eliminar(id): Método para eliminar un elemento de la Tabla País. Debe tener como parámetro la llave primaria, retorna True si logró eliminarse y False en caso contrario.
d. consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro de la Tabla País. Ejemplo: “id = 1” , “nombre like %A%”

"""
from UNIDAD_2.Meta2.Ejercicio1 import SQLConnect
from mysql.connector import Error

class PaisSQL(SQLConnect):
    def __init__(self):
        super().__init__(
            host="127.0.0.1",
            user="root",
            password="12345678",
            database="olimpiadas"
        )

    def insertar(self, nombre):
        try:
            #Conectar
            conexion = self.conectar()
            cursor = conexion.cursor()

            #Ejecutar comandos de SQL
            sql = "INSERT INTO Pais (nombre) VALUES (%s)" #al estar declarado en mysql como auto_increment, no se pone el id
            valores = (nombre,) #cuando una tupla tiene un unico valor, porque si no, lo toma como valor entero y va a marcar error
            cursor.execute(sql, valores)
            conexion.commit()
            cursor.close()
            print("El país se agregó correctamente")
            return True

        except Error as e:
            print("Error al insertar país:", e)
            return False

        finally:
            self.desconectar()

    def editar(self, id, nombre_nuevo):
        try:
            #Conectar
            conexion = self.conectar()
            cursor = conexion.cursor()

            #Validar que no exista el nombre
            validar = "SELECT COUNT(*) FROM Pais WHERE nombre LIKE %s"
            valor_validado = ("%" + nombre_nuevo + "%",)
            cursor.execute(validar, valor_validado)
            resultado = cursor.fetchone()[0]

            #Si es 1, no se edita porque ya existe
            if resultado > 0:
                print("El nombre ya existe")
                return False

            #Si no es, se puede editar
            else:
                #Ejecutar comandos de SQL
                sql = "UPDATE Pais SET nombre = %s WHERE id = %s"
                valores = (nombre_nuevo, id)
                cursor.execute(sql, valores)
                conexion.commit()
                print(f"El país con ID {id} se actualizó correctamente")
                cursor.close()
                return True

        except Error as e:
            print("Error al editar el país:", e)
            return False

        finally:
            self.desconectar()

    def eliminar(self, id):
        try:
            #Conectar
            conexion = self.conectar()
            cursor = conexion.cursor()

            #Ejecutar comandos de SQL
            sql = "DELETE FROM Pais WHERE id = %s"
            valores = (id,) #cuando una tupla tiene un unico valor, porque si no, lo toma como valor entero y va a marcar error
            cursor.execute(sql, valores)
            conexion.commit()
            print(f"El país con ID {id} se eliminó correctamente")
            cursor.close()
            return True

        except Error as e:
            print("Error al eliminar el país:", e)
            return False

        finally:
            self.desconectar()

    def consultar(self, filter):
        try:
            #Conectar
            conexion = self.conectar()
            cursor = conexion.cursor()

            #Validar si hay filtro
            if filter:
                #Ejecutar comandos de SQL
                sql = "SELECT * FROM Pais WHERE nombre LIKE %s"
                valores = ("%" + filter + "%",)
                cursor.execute(sql, valores)

            else:
                sql = "SELECT * FROM Pais"
                cursor.execute(sql)

            #Utilizar fetchall para traer todos las filas que cumplen con la condicion de la consulta
            resultados = cursor.fetchall()
            cursor.close()
            return resultados

        except Error as e:
            print("Error en la consulta:", e)

        finally:
            self.desconectar()

pais = PaisSQL()
#insertar
pais.insertar("MX")
pais.insertar("USA")
#consultar
consulta = pais.consultar("M")
print(consulta)
#editar
pais.editar(1, "Mexico")
#eliminar
pais.eliminar(1)
#consultar
consulta2 = pais.consultar("U")
print(consulta2)
