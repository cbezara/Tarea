nombre = input ("Escribe tu nombre (la primera letra debe ser en mayúscula): ")
if nombre [0].islower():
    print("Error, la primera letra del nombre debe ser escrita en mayúscula")
    quit ()

sexo = input("Escribe tu sexo: ")
if (sexo != "masculino") and (sexo != "femenino") and (sexo != "Masculino") and (sexo != "Femenino"):
    print("ERROR, el sexo debe ser masculino o femenino")
    quit ()
elif sexo == "masculino" or sexo == "Masculino":
    print ("Bienvenido", nombre)
elif sexo == "femenino" or sexo == "Femenino":
    print ("Bienvenida", nombre)

print("Seleccione el número de su región (1-Venezuela, 2- Japón, 3-Argentina)")
reg=int(input())
if(reg>3):
    print("ERROR, la región indicada no es valida")
    quit()
else:
    if(reg==1):
        reg="Venezuela"
        print("Seleccione el número de su cosa favorita de Venezuela (1- Playas, 2-Arepas, 3-Música)")
        cosa=int(input())
        if(cosa==1):
            cosa= "Las playas"
        elif(cosa==2):
            cosa= "Las arepas"
        elif(cosa==3):
            cosa= "La música"
        elif(cosa>3):
            print("Error, su cosa favorita no es válida")
            quit()
    elif(reg==2):
        reg="Japón"
        print("Seleccione el número de su cosa favorita de Japón (1- Sushi, 2-Tecnología, 3-Anime)")
        cosa=int(input())
        if(cosa==1):
            cosa= "El sushi"
        elif(cosa==2):
            cosa= "La tecnología"
        elif(cosa==3):
            cosa= "El anime"
        elif(cosa>3):
            print("Error, su cosa favorita no es válida")
            quit()
    elif(reg==3):
        reg="Argentina"
        print("Seleccione el número de su cosa favorita de Argentina (1-Mate, 2-Alfajores, 3-Fútbol)")
        cosa=int(input())
        if(cosa==1):
            cosa= "El mate"
        elif(cosa==2):
            cosa= "Los alfajores"
        elif(cosa==3):
            cosa= "El fútbol"
        elif(cosa>3):
            print("Error, su cosa favorita no es valida")
            quit()
print("El perfil del usuario es el siguiente:") 
print("Nombre:", nombre) 
print("Sexo:", sexo) 
print("Región:", reg) 
print("Cosa favorita:", cosa) 