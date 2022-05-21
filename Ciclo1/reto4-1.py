import json

pedidos = input()
edificio = input()

edificio = edificio.upper()
edificio = list(edificio)

pedidos = json.loads(pedidos)

cantidad = 0
ediFound = []

for key in edificio:
    if key in pedidos:
        cantidad += pedidos[key]
        ediFound.append(key)

print(cantidad)
print(' '.join(ediFound))