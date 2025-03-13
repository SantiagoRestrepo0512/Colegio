# 4- ¿Cuántos estudiantes aprobaron la materia "Base de Datos"?

import json

def contar_estudiantes_aprobados(archivo_notas, materia):
    with open(archivo_notas, "r", encoding="utf-8") as file:
        notas = json.load(file)

    cantidad = sum(1 for nota in notas if nota["nombre_materia"] == materia and nota["nota_final"] >= 3.0)
    return cantidad

# Ruta del archivo
archivo_notas = "notas.json"

# Contar y mostrar el resultado
print(f"La cantidad de estudiantes que lograron aprobar base de datos fue: {contar_estudiantes_aprobados(archivo_notas, 'Base de Datos')}")