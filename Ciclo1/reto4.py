
n = int(input("Digite el numero de argumentos: "))

letra = []
numero = []
for i in range(n):
    let = input("Ingrese la letra: ")
    num = int(input("Ingrese el numero:"))
    
    letra.append(let)
    numero.append(num)

for i in range(len(letra)):
    letra[i] = letra[i].upper()

dic = dict(zip(letra,numero))

edi =  input("Ingrese la lista de edificios: ")
edi = edi.upper()
edi = list(edi)

con = 0
l = []

for key in dic:
    if key in edi:
        con += dic[key]
        l.append(key)

print(con)
print(l)


