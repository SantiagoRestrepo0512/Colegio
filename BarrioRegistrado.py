#3 ¿Cuántos estudiantes viven en el barrio "San Benito"?
import json

def contar_barrios_registrados(archivo_barrios):
    with open(archivo_barrios, "r", encoding="utf-8") as file:
        barrios = json.load(file)

    cantidad = len(set(barrio["barrio"] for barrio in barrios))
    return cantidad

archivo_barrios = "barrios.json"

print(f"Cantidad de barrios registrados: {contar_barrios_registrados(archivo_barrios)}")
