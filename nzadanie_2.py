x = float(input("Podaj liczbę x: "))
y = float(input("Podaj liczbę y: "))
z = float(input("Podaj liczbę z: "))

lista = []

if x < y and x < z:
    lista.append(x)
    if y < z:
        lista.append(y)
        lista.append(z)
        print(lista)
    elif y > z:
        lista.append(z)
        lista.append(y)
        print(lista)
elif y < x and y < z:
    lista.append(y)
    if x > z:
        lista.append(z)
        lista.append(x)
        print(lista)
    else:
        lista.append(x)
        lista.append(z)
        print(lista)
elif z < x and z < y:
    lista.append(z)
    if x > y:
        lista.append(y)
        lista.append(x)
        print(lista)
    else:
        lista.append(x)
        lista.append(y)
        print(lista)