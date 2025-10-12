"""
Nombre: Gonzalez Salas Yuvia Itzel
Grupo: 951
Fecha: 31 de agosto de 2025
Sistema de Reserva. Desarrolla un sistema de reservas utilizando sets. Crea conjuntos para representar habitaciones
disponibles y habitaciones reservadas en un hotel. Permite a los usuarios realizar reservas, liberar habitaciones y
mostrar la disponibilidad actual.
NOTA: No utilizar menú,  solo las funciones , realizar las pruebas necesarias para verificar funcionamiento adecuado.

"""

HabDisponibles = {100, 105, 110, 115, 120, 125, 130} #Set para las habitaciones disponibles
HabReservadas = set() #Set vacio para las reservas

def Reservar(room): #Se cambia Habitacion por room para hacerlo mas corto
    if room in HabDisponibles:
        HabDisponibles.remove(room) #Si el room se encuentra en habitaciones disponibles, se quita
        HabReservadas.add(room) #y luego se manda a reservas
        print(f"La reservación se realizó correctamente, su habitación es: {room}.")
    elif room in HabReservadas:
        print("Lo sentimos, esa habitación ya esta reservada, por favor, intente con otro número.")
    else:
        print(f"ERROR. La habitación {room} no existe, por favor, intente con otro número.")
def Liberar(room):
    if room in HabReservadas:
        HabReservadas.remove(room)
        HabDisponibles.add(room)
        print(f"La habitación {room} se liberó correctamente.")
    elif room in HabDisponibles:
        print("Esta habitación ya se encuentra disponible, intente con otro número")
    else:
        print(f"ERROR. La habitación {room} no existe, por favor, intente con otro número.")
def MostrarDisponibles():
    print(f"Las habitaciones disponibles son: {HabDisponibles}")
    print(f"Las habitaciones reservadas son: {HabReservadas}")
    print("------------------------------------------------------")
#Pruebas
MostrarDisponibles()
Reservar(100)
Reservar(105)
Reservar(145)  #Habitación que no existe
MostrarDisponibles()
Liberar(100)
Liberar(125)  #Habitación que ya está disponible
MostrarDisponibles()

print("••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")

"""
Encriptación y Desencriptación de Mensajes Secretos. Tú y tu mejor amigo están creando un sistema secreto para enviar 
mensajes entre ustedes sin que nadie más pueda entenderlos. Deciden utilizar un método de encriptación y desencriptación
basado en listas o diccionarios.

Parte 1: Encriptación. Crear una función llamada encriptar_mensaje que tome como entrada un mensaje de texto y utilice 
un diccionario para reemplazar cada letra por un código secreto. El diccionario de encriptación debe asignar a cada 
letra una cadena de caracteres alfanuméricos aleatorios. Ejemplo de diccionario:

diccionario_encriptacion = {'a': '$%3', 'b': '8@*', 'c': '2&9', ...}

Parte 2: Desencriptación. Crear una función llamada desencriptar_mensaje que tome como entrada un mensaje encriptado 
y utilice el mismo diccionario para revertir el proceso y obtener el mensaje original.
"""

#Diccionario para las escriptaciones
encriptados = {'a': '$%3', 'b': '8@*', 'c': '2&9', 'd': '1#4', 'e': '7!x',
    'f': 'z$0', 'g': 'p&2', 'h': 'k*3', 'i': 'm7!', 'j': 'o9^',
    'k': 't@8', 'l': 'q$6', 'm': 'r*5', 'n': 'w1#', 'o': 'y7%',
    'p': 'u!9', 'q': 'i&0', 'r': 'e*4', 's': 'v2$', 't': 'c^3',
    'u': 'g!1', 'v': 'h@7', 'w': 'l#8', 'x': 'n%2', 'y': 's$5',
    'z': 'd!6', ' ': '__'}

def EncriptarMensaje(mensaje):
    mensaje = mensaje.lower() #todo a minusculas para facilitar su manipulacion
    encriptar = "" #variable vacia para guardar el mensaje ya encriptado
    for letra in mensaje:
        if letra in encriptados:
            encriptar += encriptados[letra] + " "
        else:
            encriptar += letra + " " #si no está en el diccionario, se deja igual
    return encriptar.strip()

def DesencriptarMensaje(encriptar):
    # Dividir el mensaje encriptado en fragmentos
    partes_encriptadas = encriptar.split()

    mensaje_desencriptado = ""

    # Recorrer cada parte del mensaje encriptado
    for parte in partes_encriptadas:
        letra_original = ""
        for letra,codigo in encriptados.items():
            if codigo == parte:
                letra_original += letra
                break

        if letra_original != "":
            mensaje_desencriptado += letra_original + ""

        else:
            mensaje_desencriptado += parte + ""

    return mensaje_desencriptado


#Probar
Conversacion = "hola amigo"
print("El mensaje original:", Conversacion)

encriptado = EncriptarMensaje(Conversacion)
print("El mensaje encriptado:", encriptado)

desencriptado = DesencriptarMensaje(encriptado)
print("El mensaje desencriptado:", desencriptado)

"""

Inventario de Productos. Gestiona un inventario de productos en una tienda utilizando diccionarios. Las claves pueden 
ser los códigos de producto y los valores pueden ser diccionarios con información como el nombre, precio y cantidad 
en stock. Debe tener funciones para agregar, editar, eliminar producto, además de funciones para realizar venta e 
imprimir inventario.

"""
