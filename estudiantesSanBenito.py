import json
#2
def contar_estudiantes_san_benito(archivo_barrios):
    with open(archivo_barrios, "r", encoding="utf-8") as file:
        barrios = json.load(file)

    cantidad = sum(1 for barrio in barrios if barrio["barrio"] == "San Benito")
    return cantidad

# Ruta del archivo
archivo_barrios = "barrios.json"

# Contar y mostrar el resultado
print(f"Estudiantes en San Benito: {contar_estudiantes_san_benito(archivo_barrios)}")