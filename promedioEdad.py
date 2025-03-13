# 1- ¿Cuál es el promedio de edad de los estudiantes?

import json

def calcular_promedio_edad(archivo_estudiantes):
    with open(archivo_estudiantes, "r", encoding="utf-8") as file:
        estudiantes = json.load(file)

    promedio = sum(estudiante["edad"] for estudiante in estudiantes) / len(estudiantes)
    return promedio

# Ruta del archivo
archivo_estudiantes = "estudiantes.json"

# Calcular y mostrar el resultado
print(f"Los estudiantes tiene una edad promedio de : {calcular_promedio_edad(archivo_estudiantes):.2f} años")