%pip install playsound=1.2.2
import numpy as np
import random
from playsound import playsound
import os

tablero1_US = np.full((10,10), "~")
tablero2_US = np.full((10,10), "~")
tablero1_Japon = np.full((10,10), "~")
tablero2_Japon = np.full((10,10), "~")

def crea_barco(tablero, fila_ini, columna_ini, eslora, orientacion):
    
    num_max_filas, num_max_columnas = tablero.shape

    # Validación de coordenadas iniciales
    if not (0 <= fila_ini < num_max_filas):
        raise ValueError("La coordenada inicial de fila está fuera del tablero")
    if not (0 <= columna_ini < num_max_columnas):
        raise ValueError("La coordenada inicial de columna está fuera del tablero")

    orientacion = orientacion.strip().upper()
    
    # Validar que el barco cabe en el tablero según orientación
    if orientacion == "N" and fila_ini - (eslora - 1) < 0:
        raise ValueError("El barco no cabe hacia el norte.")
    elif orientacion == "S" and fila_ini + (eslora - 1) >= num_max_filas:
        raise ValueError("El barco no cabe hacia el sur.")
    elif orientacion == "E" and columna_ini + (eslora - 1) >= num_max_columnas:
        raise ValueError("El barco no cabe hacia el este.")
    elif orientacion == "O" and columna_ini - (eslora - 1) < 0:
        raise ValueError("El barco no cabe hacia el oeste.")

    # Construir el barco
    barco = [(fila_ini, columna_ini)]
    fila, columna = fila_ini, columna_ini
    for _ in range(eslora - 1):
        if orientacion == "N":
            fila -= 1
        elif orientacion == "S":
            fila += 1
        elif orientacion == "E":
            columna += 1
        elif orientacion == "O":
            columna -= 1
        barco.append((fila, columna))
    
    print(barco)
    return barco

print("Jugador, representas a US, es hora de que crees y coloques tus acorazados. \nEl Utah, con una eslora 2, entra la fila de inicio (0,9), la columna de inicio (0,9), 2 (eslora) y la orientación (N, S, E, O),\nel Nevada y el Missouri con una eslora de 3, el Oklahoma con una eslora de 4 y el Arizona con una eslora de 5" )

fila_ini = input("Entra la fila inicial: ")
columna_ini = input("Entra la columna inicial: ")
eslora = 2
orientacion = str(input("Entra la orientación del barco: "))

USS_Utah = crea_barco(tablero1_US, fila_ini, columna_ini, eslora, orientacion)

fila_ini = input("Entra la fila inicial: ")
columna_ini = input("Entra la columna inicial: ")
eslora = 3
orientacion = str(input("Entra la orientación del barco: "))

USS_Nevada = crea_barco(tablero1_US, fila_ini, columna_ini, eslora, orientacion)

fila_ini = input("Entra la fila inicial: ")
columna_ini = input("Entra la columna inicial: ")
eslora = 3
orientacion = str(input("Entra la orientación del barco: "))

USS_Missouri = crea_barco(tablero1_US, fila_ini, columna_ini, eslora, orientacion)

fila_ini = input("Entra la fila inicial: ")
columna_ini = input("Entra la columna inicial: ")
eslora = 4
orientacion = str(input("Entra la orientación del barco: "))

USS_Oklahoma = crea_barco(tablero1_US, fila_ini, columna_ini, eslora, orientacion)

fila_ini = input("Entra la fila inicial: ")
columna_ini = input("Entra la columna inicial: ")
eslora = 5
orientacion = str(input("Entra la orientación del barco: "))

USS_Arizona = crea_barco(tablero1_US, fila_ini, columna_ini, eslora, orientacion)

def colaca_barco(tablero1_US, barco):
    tablero_temp = tablero1_US.copy()
    num_max_filas = tablero1_US.shape[0]
    num_max_columnas = tablero1_US.shape[1]
    for pieza in barco: 
        fila = pieza[0]
        columna = pieza[1] 

        if fila < 0 or fila >= num_max_filas:
            print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if columna < 0 or columna >= num_max_columnas:
            print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if tablero1_US[pieza] == "O":
            print(f"No se puede poner la {pieza} porque hay otro barco")
            return False
        tablero_temp[pieza] = "O"
    return tablero_temp

tablero1_US = colaca_barco (tablero1_US, USS_Utah)

tablero1_US = colaca_barco(tablero1_US, USS_Nevada)

tablero1_US = colaca_barco(tablero1_US, USS_Missouri)

tablero1_US = colaca_barco(tablero1_US, USS_Oklahoma)

tablero1_US = colaca_barco(tablero1_US, USS_Arizona)

print(tablero1_US)

print("Ahora el ordenador, que representa a Japón, creará y colocará sus portaaviones aleatoriamente.\nEl Akagi con una eslora de 5, el Shokaku con una eslora de 4, el Kaga y el Hiryu con una eslora de 3, y el Soryu con una eslora de 2")

def colaca_barco_plus(tablero1_Japon, barco):
    tablero_temp = tablero1_Japon.copy()
    num_max_filas = tablero1_Japon.shape[0]
    num_max_columnas = tablero1_Japon.shape[1]
    for pieza in barco: 
        fila = pieza[0]
        columna = pieza[1] 

        if fila < 0 or fila >= num_max_filas:
            print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if columna < 0 or columna >= num_max_columnas:
            print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if tablero1_Japon[pieza] == "O":
            print(f"No se puede poner la {pieza} porque hay otro barco")
            return False
        tablero_temp[pieza] = "O"
    return tablero_temp

def crea_barco_aleatorio(tablero1_Japon, eslora, num_intentos = 10):
    num_max_filas = tablero1_Japon.shape[0]
    num_max_columnas = tablero1_Japon.shape[1]
    while True:
        barco = []
        pieza_original = (random.randint(0,num_max_filas-1), random.randint(0,num_max_columnas-1))
        print("Pieza original:", pieza_original)
        barco.append(pieza_original)
        orientacion = random.choice(["N", "S", "E", "O"])
        print("Con orientacion:", orientacion)
        fila = pieza_original[0]
        columna = pieza_original[1]
        for i in range(eslora -1):
            if orientacion == "N":
                fila -= 1
            elif orientacion == "S":
                fila += 1
            elif orientacion == "E":
                columna += 1
            else:
                columna -= 1
            pieza = (fila, columna)
            barco.append(pieza)
    
        tablero_temp = colaca_barco_plus(tablero1_Japon, barco)
        if type(tablero_temp) == np.ndarray:
            return tablero_temp
        print("Tengo que intentar colocar otro barco")

tablero1_Japon = crea_barco_aleatorio(tablero1_Japon, eslora = 2, num_intentos = 10)

tablero1_Japon = crea_barco_aleatorio(tablero1_Japon, eslora = 3, num_intentos = 10)

tablero1_Japon = crea_barco_aleatorio(tablero1_Japon, eslora = 3, num_intentos = 10)

tablero1_Japon = crea_barco_aleatorio(tablero1_Japon, eslora = 4, num_intentos = 10)

tablero1_Japon = crea_barco_aleatorio(tablero1_Japon, eslora = 5, num_intentos = 10)

print(tablero1_Japon)

def disparo_US(tablero1_Japon, coordenada):
    sound_path = r"C:\Users\bgran\Music\dropped-a-bomb-and-it-exploded.mp3"
    
    if not os.path.isfile(sound_path):
        print(f"Error: No se encontró el archivo en {sound_path}")
    else:
        try:
            playsound(sound_path)
        except Exception as e:
            print(f"Ocurrió un error al reproducir el sonido: {e}")
    
    if tablero1_Japon[coordenada] == "O":
        tablero1_Japon[coordenada] = "X"
        print("Tocado")
        if tablero1_Japon[coordenada] == "X":
            tablero2_US[coordenada] = "X"
            print(tablero2_US)
            
    elif tablero1_Japon[coordenada] == "X":
        print("Ya has disparado ahí")
    else:
        tablero1_Japon[coordenada] = "a"
        print("Agua")
        if tablero1_Japon[coordenada] == "a":
            tablero2_US[coordenada] = "a"
            print(tablero2_US)

def disparo_Japón(tablero1_US):
    sound_path = r"C:\Users\bgran\Music\dropped-a-bomb-and-it-exploded.mp3"
    
    if not os.path.isfile(sound_path):
        print(f"Error: No se encontró el archivo en {sound_path}")
    else:
        try:
            playsound(sound_path)
        except Exception as e:
            print(f"Ocurrió un error al reproducir el sonido: {e}")
    
    num_max_filas = tablero1_US.shape[0]
    num_max_columnas = tablero1_US.shape[1]
    coordenada = (random.randint(0,num_max_filas-1), random.randint(0,num_max_columnas-1))
    if tablero1_US[coordenada] == "O":
        tablero1_US[coordenada] = "X"
        print("Tocado")
        if tablero1_US[coordenada] == "X":
            tablero2_Japon[coordenada] = "X"
            print(tablero2_US)
    elif tablero1_US[coordenada] == "X":
        print("Ya has disparado ahí")
    else:
        tablero1_US[coordenada] = "a"
        print("Agua")
        if tablero1_US[coordenada] == "a":
            tablero2_Japon[coordenada] = "a"
            print(tablero2_Japon)

print("Ya habéis creado vuestros acorazados y portaaviones, y los habéis colocado en vuestros tableros.\n¿Podrás cambiar el curso de la historia?¡Mucha suerte!¡Comencemos!")

def chequeo_victoria(tablero):
    """Devuelve True si no quedan barcos en el tablero."""
    return not np.any(tablero == "O")

def turno():
    while True:
        print("Turno de US")
        fila = int(input("Introduce la coordenada"))
        columna = int(input("Introduce la coordenada"))
        coordenada = (fila, columna)
        print(coordenada)
        disparo_US(tablero1_Japon, coordenada)
        if chequeo_victoria(tablero1_Japon) == True:
            print("Has evitado la tragedia. ¡Has ganado!")
            break
        else:
            print("Turno de Japón")
            disparo_Japón(tablero1_US)
            if chequeo_victoria(tablero1_US) == True:
                print("La tragedia se repite. ¡Has perdido!")
                break
turno()
