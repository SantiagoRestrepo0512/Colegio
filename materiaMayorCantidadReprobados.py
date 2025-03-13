import json

def materia_mas_reprobada(archivo_notas):
    with open(archivo_notas, "r", encoding="utf-8") as file:
        notas = json.load(file)

    reprobados = {}
    for nota in notas:
        if nota["nota_final"] < 3.0:
            reprobados[nota["nombre_materia"]] = reprobados.get(nota["nombre_materia"], 0) + 1

    return max(reprobados, key=reprobados.get) if reprobados else None

# Ruta del archivo
archivo_notas = "notas.json"

# Determinar y mostrar el resultado
print(f"Materia con más reprobados: {materia_mas_reprobada(archivo_notas)}")