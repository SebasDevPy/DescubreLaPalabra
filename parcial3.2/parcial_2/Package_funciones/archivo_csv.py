import csv

def leer_nickname_desde_csv():
    lista_jugadores = []
    contador_jugadores_id = 0
    
    try:
        with open("jugadores.csv", mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                jugador = {
                    "id": int(row["id"]),
                    "nickname": row["nickname"],
                    "puntuacion": int(row["puntuacion"])
                }
                lista_jugadores.append(jugador)
                contador_jugadores_id = max(contador_jugadores_id, int(row["id"]))
        print("Jugadores cargados correctamente desde jugadores.csv")
    except FileNotFoundError:
        print("El archivo jugadores.csv no existe. Se creará uno nuevo al guardar el primer jugador.")
    except Exception as e:
        print(f"Error al leer jugadores desde jugadores.csv: {e}")
    
    return lista_jugadores, contador_jugadores_id

def guardar_jugadores_en_csv(lista_jugadores):
    try:
        jugadores_existentes = set()  # Conjunto para mantener un registro de jugadores existentes
        with open('jugadores.csv', 'w', newline='', encoding='utf-8') as file:
            headers = ['id', 'nickname', 'puntuacion']
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for jugador in lista_jugadores:
                if jugador['nickname'] not in jugadores_existentes:
                    writer.writerow(jugador)  # Escribir jugador solo si no existe en el conjunto
                    jugadores_existentes.add(jugador['nickname'])  # Agregar jugador al conjunto de existentes
        print("Jugadores guardados correctamente en jugadores.csv")
    except Exception as e:
        print(f"Error al guardar jugadores en CSV: {e}")
