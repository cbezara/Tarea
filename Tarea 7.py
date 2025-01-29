import random
# Definir funciones para cada ataque
def impactrueno(salud, defensa):
    daño = 20 / defensa
    return salud - daño, defensa  

def cola_de_hierro(salud, defensa):
    daño = 15 / defensa
    nueva_defensa = max(0.5, defensa - 0.1)  
    return salud - daño, nueva_defensa

def ataque_rapido(salud, defensa):
    daño = 10 / defensa
    return salud - daño, defensa

def electrobola(salud, defensa):
    daño = 25 / defensa
    return salud - daño, defensa

def llamarada(salud, defensa):
    daño = 30 / defensa
    nueva_defensa = max(0.5, defensa - 0.2)
    return salud - daño, nueva_defensa

def garra_dragon(salud, defensa):
    daño = 20 / defensa
    return salud - daño, defensa

def ascuas(salud, defensa):
    daño = 15 / defensa
    return salud - daño, defensa

# Diccionario de ataques para cada Pokémon
ataques_pikachu = {
    "Impactrueno": impactrueno,
    "Cola de Hierro": cola_de_hierro,
    "Ataque Rápido": ataque_rapido,
    "Electrobola": electrobola,
}

ataques_charmander = {
    "Llamarada": llamarada,
    "Garra Dragón": garra_dragon,
    "Ascuas": ascuas,
    "Ataque Rápido": ataque_rapido,  
}

# Diccionarios para cada Pokémon
pikachu = {"nombre": "Pikachu", "salud": 100, "defensa": 1.0, "ataques": ataques_pikachu}
charmander = {"nombre": "Charmander", "salud": 100, "defensa": 1.0, "ataques": ataques_charmander}

# Función para mostrar los ataques de un Pokémon
def mostrar_ataques(pokemon):
    print(f"Ataques de {pokemon['nombre']}:")
    for ataque in pokemon["ataques"]:
        print(f" - {ataque}")

# Función para ejecutar un ataque y devolver nuevos valores sin modificar directamente al Pokémon
def ejecutar_ataque(ataque, salud, defensa):
    return ataque(salud, defensa)  

# Batalla Pokémon
def batalla(pokemon1, pokemon2):
    while pokemon1["salud"] > 0 and pokemon2["salud"] > 0:
        print(f"\n{pokemon1['nombre']} Salud: {pokemon1['salud']:.1f}, Defensa: {pokemon1['defensa']:.2f}")
        print(f"{pokemon2['nombre']} Salud: {pokemon2['salud']:.1f}, Defensa: {pokemon2['defensa']:.2f}")

        # Turno del jugador
        mostrar_ataques(pokemon1)
        ataque_jugador = input(f"Elige un ataque para {pokemon1['nombre']}: ")
        if ataque_jugador not in pokemon1["ataques"]:
            print("Ataque no válido. Pierdes el turno.")
        else:
            # Ejecutar ataque y actualizar valores del Pokémon oponente
            pokemon2["salud"], pokemon2["defensa"] = ejecutar_ataque(
                pokemon1["ataques"][ataque_jugador], pokemon2["salud"], pokemon2["defensa"]
            )

        # Comprobar si el oponente fue derrotado
        if pokemon2["salud"] <= 0:
            print(f"\n{pokemon2['nombre']} ha sido derrotado. ¡{pokemon1['nombre']} gana!")
            break

        # Turno de la computadora
        ataque_computadora = random.choice(list(pokemon2["ataques"].keys()))
        print(f"{pokemon2['nombre']} usó {ataque_computadora}!")

        # Ejecutar ataque y actualizar valores del Pokémon del jugador
        pokemon1["salud"], pokemon1["defensa"] = ejecutar_ataque(
            pokemon2["ataques"][ataque_computadora], pokemon1["salud"], pokemon1["defensa"]
        )

        # Comprobar si el jugador fue derrotado
        if pokemon1["salud"] <= 0:
            print(f"\n{pokemon1['nombre']} ha sido derrotado. ¡{pokemon2['nombre']} gana!")
            break

# Iniciar la batalla
batalla(pikachu, charmander)