#Ingreso las iniciales del equipo correspondiente
equipoa = input("Digite las iniciales del equipo a: ")
equipob = input("Digite las iniciales del equipo b: ")

#Digito las iniciales de los anotadores del partido
anotadores = input("Digite los anotadores del partido:")

#Las iniciales deben estar en mayusculas
equipoa = equipoa.upper()
equipob = equipob.upper()
anotadores = anotadores.upper()

print(equipoa)
print(equipob)

contadora = 0
contadorb = 0

#El for recorre cada letra dentro de los datos ingresados
for letra in anotadores:

    #Si la letra aparece en ambos equipos, se cuenta a ambos la anotacion
    if letra in equipoa and letra in equipob:
        contadora += 1
        contadorb += 1
    #Si la letra esta en el equipoa, se indica un gol
    elif letra in equipoa:
        contadora += 1
    #Si la letra esta en el equipoa, se indica un gol
    elif letra in equipob:
        contadorb += 1
    #end="", imprime horizontalmente la condicion
    if contadora > contadorb:
        print("X", end="")
        
    elif contadorb > contadora:
        print("Y", end="")
    else:
        print("Z", end="")
