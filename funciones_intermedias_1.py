# funciones_intermedias_1.py

matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# 🔹 Cambiar 3 por 6 en matriz
matriz[1][0] = 6

# 🔹 Cambiar nombre del primer cantante
cantantes[0]["nombre"] = "Enrique Martin Morales"

# 🔹 Cambiar "Cancún" por "Monterrey"
ciudades["México"][2] = "Monterrey"

# 🔹 Cambiar latitud
coordenadas[0]["latitud"] = 9.9355431
def iterarDiccionario(lista):
    for dic in lista:
        linea = ""
        for clave, valor in dic.items():
            linea += f"{clave} - {valor}, "
        print(linea.strip(", "))  # elimina la última coma

cantantes_lista = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario2(llave, lista):
    for dic in lista:
        print(dic[llave])  # imprime el valor de la clave

def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")  # tamaño + nombre
        for elemento in lista:
            print(elemento)
        print()  # línea en blanco
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}
print("Matriz:", matriz)
print("Cantantes:", cantantes)
print("Ciudades:", ciudades)
print("Coordenadas:", coordenadas)