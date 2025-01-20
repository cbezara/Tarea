def contar_anios_bisiestos_sin_ciclos(anio):
    if anio < 1900 or anio > 2199:
        raise ValueError("El año debe estar entre 1900 y 2199")
    
    total_div_4 = (anio // 4) - ((1900 - 1) // 4)
    
    total_div_100 = (anio // 100) - ((1900 - 1) // 100)
    
    total_div_400 = (anio // 400) - ((1900 - 1) // 400)
    
    return total_div_4 - total_div_100 + total_div_400

try:
    año = int(input("Introduce un año entre 1900 y 2199: "))
    print("Número de años bisiestos hasta {}: {}".format(año, contar_anios_bisiestos_sin_ciclos(año)))
except ValueError as e:
    print(e)