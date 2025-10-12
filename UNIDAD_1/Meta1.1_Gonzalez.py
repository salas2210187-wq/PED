"""
Nombre: Gonzalez Salas Yuvia Itzel
Grupo: 951
Fecha: 31 de agosto de 2025

Estadística Básica. Cree una clase llamada Estadística que contiene como atributo una lista de números naturales la cual
puede contener repetidos. Debe contener los siguientes métodos:
a) Frecuencia de Números. Dada la lista, devuelve una lista de tuplas con el número de veces que aparece cada número en
la lista. La tupla debe tener el número y la cantidad de veces que aparece.
b)Moda. Dada la lista, devuelva la moda de la lista (el valor más repetido). Puedes usar la función anterior como ayuda.
c)Histograma. Dada la lista, muestra el histograma de la lista. Puedes reusar los métodos anteriores.

"""

#Crear una clase llamada Estadistica
class Estadistica():
    def __init__(self, Lista): #Constructor con los argumentos
        self.Lista = Lista #Atributo

    def Frecuencia(self):
        frecuencia = [] #lista para guardar las frecuencias
        valores = [] #lista para los numeros
        #Hacer un ciclo que recorra la lista
        for numero in self.Lista:
            #Mediante una condicion vamos a verificar que el numero no se encuentra ya en la lista de numeros
            if numero not in valores:
                #Si no esta, se agrega
                valores.append(numero)
                #Se define un contador para saber la frecuencia
                contador = 0
                #Despues un ciclo para agregar la frecuencia de cada numero
                for x in self.Lista:
                    #Se compara con el valor para ir guardando cuantas veces se repite
                    if x == numero:
                        contador += 1 #Si lo es, se le suma uno al contador
                frecuencia.append((numero, contador)) #Se crea tupla y se agrega a la lista de frecuencias
        #Retornamos la lista de tuplas
        return frecuencia

    def Moda(self):
        frecuencias = self.Frecuencia() #Asignar a la variable la funcion de Frecuencia para poder trabajar con ella
        moda = 0 #Variable para guardar el numero
        CantidadMax = 0 #Variable para guardar la frecuencia mas alta

        for numero, cantidad in frecuencias: #se recorre la lista de Frecuencias
            if cantidad > CantidadMax:
                CantidadMax = cantidad
                moda = numero
        print("La moda es:", moda)
        print("Se repite:", CantidadMax)

    def Histograma(self):
        frecuencias = self.Frecuencia() #Obtenemos la lista de frecuencias

        for numero, cantidad in frecuencias: #Recorremos las tuplas
            print(f"{numero}: {'*' * cantidad}") #Imprimimos número y asteriscos según la frecuencia

#Instanciar clase
lista = Estadistica([1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1])
print("Frecuencias:", lista.Frecuencia())
lista.Moda()
lista.Histograma()


print("-------------------------------------------------------------------------------------")
"""

Historial de Cambios en una Hoja de Cálculo. Simula el historial de cambios en una hoja de cálculo, donde los usuarios
pueden realizar cambios en las celdas. Usa una lista como pila para almacenar los cambios y permite a los usuarios
deshacer múltiples cambios.
• Implementa funciones para registrar un cambio en la hoja de cálculo (por ejemplo, cambiar el valor de una celda) y
deshacer el último cambio.
• Cada cambio debe incluir la celda modificada y el valor anterior.
• Simula una serie de cambios y la función de deshacer.

"""

class HojaCalculo: #definir una clase
    def __init__(self,filas,columnas): #definir un constructor
        self.hoja = [] #definimos la lista que sera la hoja
        #despues un ciclo para llenarla
        for i in range(filas):
            fila = [] #para llenar cada fila
            for j in range(columnas): #2do ciclo para las columnas
                fila.append("") #se inicia con la celda vacia
            self.hoja.append(fila) #agregar a la hoja

        self.Historial = [] #lista para guardar el historial

    def MostrarHoja(self): #metodo para mostrar la hoja
        for fila in self.hoja:
            print(fila)
    #para este metodo se necesitan 3 argumentos obligatorios: fila, columna y valor
    def CambiarValor(self, fila, columna, valor):
        ValorAnt = self.hoja[fila][columna] #para guardar el valor anterior
        self.Historial.append((fila, columna, ValorAnt)) #guardar los valores en la pila
        self.hoja[fila][columna] = valor #guardamos el valor indicando en que fila y clumna
    def Deshacer(self):
        #Antes de deshacer debemos validar
        if not self.Historial:
            print("No hay cambios por deshacer")
        fila, columna,ValorAnt = self.Historial.pop() #sacamos el ultimo valor de la pila Historial con pop
        ValorActual = self.hoja[fila][columna] #se guarda el valor que se tiene actualmente
        self.hoja[fila][columna] = ValorAnt #se reemplaza el valor actual por el anterior
        print(f"Se realizaron cambios en la celda {fila}, se reemplazo ({ValorActual}) por ({ValorAnt})")

#Instanciar clase
hoja = HojaCalculo(2,3)
hoja.MostrarHoja()
hoja.CambiarValor(1,1, "A")
hoja.CambiarValor(1,2, "B")
hoja.MostrarHoja()
hoja.CambiarValor(1,1,"C")
hoja.MostrarHoja()
hoja.Deshacer()
hoja.MostrarHoja()


"""
Navegación en un Almacén. En este ejercicio, el personaje es un robot que debe recoger productos en un almacén.
El almacén está representado como una cuadrícula (grid), donde cada celda puede estar vacía (.), contener un obstáculo
(#), o contener un producto (P), el inicio siempre es la posición 0,0. El robot comienza en la esquina superior
izquierda del almacén y puede moverse hacia la derecha (R), abajo (D), izquierda (L), arriba(U). El objetivo es recoger
todos los productos siguiendo una secuencia de movimientos dados y luego retornar al punto de inicio.
NOTA: LOS MOVIMIENTOS IZQUIERDA (L) Y ARRIBA (U) SE ACTIVAN SOLO PARA RETORNAR AL PUNTO DE INICIO.
a) Crear el Almacén: Representa el almacén como una lista de listas (una matriz) donde cada sublista es una fila del almacén.
b) Registrar Movimientos: Implementa una función que tome la lista de movimientos y verifique si el robot recoge todos los
productos y retorna al punto de inicio sin chocar con obstáculos.
c) Verificar Obstáculos: Si el robot encuentra un obstáculo durante su camino, el movimiento es inválido.
d) Retornar Resultado: La función debe retornar True si los movimientos son válidos, recogen todos los productos y llevan
al robot de vuelta al punto de inicio, o False en caso contrario.

"""


def VerificarMovimientos(almacen, movimientos):
    #Posicion actual
    x= 0
    y = 0

    #Productos recogidos
    productos = 0

    #Verificar los movimientos
    for mover in movimientos:
        if mover == "R":
            x += 1
        elif mover == "D":
            y += 1
        elif mover == "L":
            x -= 1
        elif mover == "U":
            y -=1
        else:
            print("Movimiento incorrecto")

#No comprendí muy bien como realizar el resto

almacen = [
[ '.',  '.',  '#',  'P'],
[ '.',  '#',  '.',  '.'],
[ 'P',  '.',  'P',  '.'],
[ '#',  '.',  '#',  '.'] ]

movimientos_correctos = ['D', 'D', 'R', 'R', 'U', 'R', 'U', 'D', 'L', 'D', 'L', 'L', 'U', 'U']
#print(verificar_recogida_productos(almacen, movimientos_correctos)) # True


def Validar(operaciones,inicial, cp, mapa):
    -
    -
    -
    -

    return True/False #variable
if __name__ == __main__:
    operaciones = []
    inicial = (0,0)
    cp = 3
    mapa = []
    t = Validar(operaciones, resto de parametros)
    print(t)