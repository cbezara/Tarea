def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def contar_anios_bisiestos_con_while(anio):
    if anio < 1900 or anio > 2199: 
        raise ValueError("El año debe estar entre 1900 y 2199")
    
    contador = 0
    i = 1900
    while i <= anio: 
        if es_bisiesto(i): 
            contador += 1
        i += 1
    return contador

try:
    año = int(input("Introduce un año entre 1900 y 2199: "))
    print("Número de años bisiestos hasta {}: {}".format(año, contar_anios_bisiestos_con_while(año)))
except ValueError as e:
    print(e)