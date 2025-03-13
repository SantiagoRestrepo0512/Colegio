# 7- ¿Cuántos estudiantes que vivan en el barrio "Guayaquil" han obtenido un promedio general por encima de 3.8?

import json

def contar_estudiantes_guayaquil_promedio(archivo_notas, archivo_barrios, limite):
    with open(archivo_notas, "r", encoding="utf-8") as file:
        notas = json.load(file)
    with open(archivo_barrios, "r", encoding="utf-8") as file:
        barrios = json.load(file)

    estudiantes_guayaquil = {barrio["identificacion"] for barrio in barrios if barrio["barrio"] == "Guayaquil"}
    
    promedios = {}
    for nota in notas:
        if nota["identificacion"] in estudiantes_guayaquil:
            if nota["identificacion"] not in promedios:
                promedios[nota["identificacion"]] = []
            promedios[nota["identificacion"]].append(nota["nota_final"])

    cantidad = sum(1 for promedio in promedios.values() if sum(promedio) / len(promedio) > limite)
    return cantidad


archivo_notas = "notas.json"
archivo_barrios = "barrios.json"


print(f"La cantidad de estudiantes que viven en guayaquil que obtuvieron un promedio mayor a 3.8: {contar_estudiantes_guayaquil_promedio(archivo_notas, archivo_barrios, 3.8)}")