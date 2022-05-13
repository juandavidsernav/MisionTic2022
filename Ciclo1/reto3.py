# Ingresas las letras deseadas 
letras =  input("Ingrese las letras deseadas: ")
#Las letras pueden tener mas de un espacio
#con strip() deja solo un espacio entre cada letra ingresada
letras = letras.strip()
# Para no recorrer espacios con un ciclo for, elimino los espacios con replace()
letras = letras.replace(" ","")
#Finalmene, el output solicita que las letras sean mayusculas
letras = letras.upper()
#creo una lista para adjuntar los strings condicionados
letras2 = []    

#creo un contador y un string para concatenar
contador = 1
largo = ""

#Este ciclo recorre el texto
for i in letras:
    #Si la lista esta vacia, incluye el primer valor
    if len(letras2) == 0:
        letras2.append(i)
    #Si la lista tiene valores, la revisa al reves para ver si lo incluye o no
    #y asi no incluir repetidos
    elif len(letras2) > 0:
        if letras2[-1] != i:
            letras2.append(i)

#Aqui concateno los resultados
resultado = ''.join(letras2)
#Como  los resultados salen juntos, list separa letra a letra
resultado = list(resultado)
print(resultado)

#Este apartado pertenece a la cantidad de letras repetidas
if len(letras) > 0:
    #Itero en el rango de 1 hasta la longitud
    #asi no se desborda el ciclo
    #Inicio el rango en 1 para lograr comparar el anterior
    for i in range(1, len(letras)):
        #Si la letra en la posicion 1 es 
        #igual a la letra de la posicion 0
        # me acumula el contador, sino, lo reinicia en 1
        if letras[i-1] == letras[i]:
            contador += 1
        else:
            largo += "" + str(contador)
            contador = 1

    largo += ("" + str(contador))
else:
    i = 0
    largo += ("" + str(contador))

#Imprimo en formato lista
largo = list(largo)
print(largo)

