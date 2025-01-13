taza = 1
cda = taza/16
cdta = cda/3
vagua = float(input("Escribe el número de tazas de agua de tu arepa: ")) * taza
vharina = float(input("Escribe el número de tazas de harina PAN de tu arepa: ")) * taza
vsal = float(input("Escribe el número de cucharaditas de sal de tu arepa: ")) * cdta
vaceite = float(input("Escribe el número de cucharadas de aceite de tu arepa: ")) * cda
vtotal = float(vagua + vharina + vsal + vaceite)
total1=(float(vtotal) *0.90)
r = round(total1,2)
print("El volumen total de la arepa es: " , r ,"tazas")
