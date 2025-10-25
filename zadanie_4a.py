gol = int(input("Liczba goli: "))
bonus =  int()

punkty_za_gole = gol * 10

if gol > 10:
    bonus = bonus + 10
    wynik = punkty_za_gole + bonus
    print(f'Wynik drużyny wynosi: {wynik}')
elif gol > 5:
    bonus = bonus + 10
    wynik = punkty_za_gole + bonus
    print(f'Wynik drużyny wynosi: {wynik}')


