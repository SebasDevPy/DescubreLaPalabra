import json

def leer_puntuaciones_json():
    try:
        with open('puntuaciones.json', 'r', encoding="utf-8") as file:
            puntuaciones = json.load(file)
            puntuaciones_ordenadas = dict(sorted(puntuaciones.items(), key=lambda item: item[1], reverse=True))
    except FileNotFoundError:
        print("Archivo JSON de puntuaciones no encontrado. Creando uno nuevo...")
        puntuaciones_ordenadas = {}
    except Exception as e:
        print(f"Error al leer puntuaciones desde JSON: {e}")
        puntuaciones_ordenadas = {}
    return puntuaciones_ordenadas

def guardar_puntuaciones_json(puntuaciones):
    try:
        with open('puntuaciones.json', 'w', enconding="utf-8") as file:
            json.dump(puntuaciones, file, indent=4)
        print("Puntuaciones guardadas correctamente en puntuaciones.json")
    except Exception as e:
        print(f"Error al guardar puntuaciones en JSON: {e}")


