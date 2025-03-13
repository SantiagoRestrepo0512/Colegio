import json
#5
def calcular_promedio_materia(archivo_notas, materia):
    with open(archivo_notas, "r", encoding="utf-8") as file:
        notas = json.load(file)

    notas_materia = [nota["nota_final"] for nota in notas if nota["nombre_materia"] == materia]
    return sum(notas_materia) / len(notas_materia) if notas_materia else 0

# Ruta del archivo
archivo_notas = "notas.json"

# Calcular y mostrar el resultado
print(f"Promedio en Herramientas III: {calcular_promedio_materia(archivo_notas, 'Herramientas III'):.2f}")