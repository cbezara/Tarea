import random
# Diccionarios para almacenar la información de los Pokémon y sus ataques
pikachu = {
    "nombre": "Pikachu",
    "salud": 100,
    "defensa": 1.0,
    "ataques": {
        "Impactrueno": {"daño": 20, "defensa": 0},
        "Cola de Hierro": {"daño": 15, "defensa": -0.1},
        "Ataque Rápido": {"daño": 10, "defensa": 0},
        "Electrobola": {"daño": 25, "defensa": 0},
    },
}

charmander = {
    "nombre": "Charmander",
    "salud": 100,
    "defensa": 1.0,
    "ataques": {
        "Llamarada": {"daño": 30, "defensa": -0.2},
        "Garra Dragón": {"daño": 20, "defensa": 0},
        "Ascuas": {"daño": 15, "defensa": 0},
        "Ataque Rápido": {"daño": 10, "defensa": 0},
    },
}

# Función para mostrar los ataques de un Pokémon
def mostrar_ataques(pokemon):
    print(f"Ataques de {pokemon['nombre']}:")
    for ataque in pokemon["ataques"]:
        print(f" - {ataque} (Daño: {pokemon['ataques'][ataque]['daño']}, Defensa: {pokemon['ataques'][ataque]['defensa']})")

# Función para ejecutar un ataque
def ejecutar_ataque(atacante, defensor, ataque):
    daño_base = atacante["ataques"][ataque]["daño"]
    daño_real = daño_base * defensor["defensa"]
    defensor["salud"] -= daño_real
    defensor["defensa"] += atacante["ataques"][ataque]["defensa"]
    if defensor["defensa"] < 0.5:  # Limitar reducción de defensa
        defensor["defensa"] = 0.5
    print(
        f"{atacante['nombre']} usó {ataque}! {defensor['nombre']} recibió {daño_real:.1f} de daño."
    )

# Batalla Pokémon
def batalla(pokemon1, pokemon2):
    while pokemon1["salud"] > 0 and pokemon2["salud"] > 0:
        print(f"\n{pokemon1['nombre']} Salud: {pokemon1['salud']:.1f}, Defensa: {pokemon1['defensa']:.2f}")
        print(f"{pokemon2['nombre']} Salud: {pokemon2['salud']:.1f}, Defensa: {pokemon2['defensa']:.2f}")

        # Turno del jugador
        mostrar_ataques(pokemon1)
        ataque_jugador = input(f"Elige un ataque para {pokemon1['nombre']}: ").strip()
        if ataque_jugador not in pokemon1["ataques"]:
            print("Ataque no válido. Pierdes el turno.")
        else:
            ejecutar_ataque(pokemon1, pokemon2, ataque_jugador)

        # Comprobar si el oponente fue derrotado
        if pokemon2["salud"] <= 0:
            print(f"\n{pokemon2['nombre']} ha sido derrotado. ¡{pokemon1['nombre']} gana!")
            break

        # Turno de la computadora
        ataque_computadora = random.choice(list(pokemon2["ataques"].keys()))
        ejecutar_ataque(pokemon2, pokemon1, ataque_computadora)

        # Comprobar si el jugador fue derrotado
        if pokemon1["salud"] <= 0:
            print(f"\n{pokemon1['nombre']} ha sido derrotado. ¡{pokemon2['nombre']} gana!")
            break

# Iniciar la batalla
batalla(pikachu, charmander)
