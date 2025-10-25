nazwa_pliku = 'Raport_maj.xlsx'

rozszerzenie_pliku = nazwa_pliku.endswith(".xlsx")

if rozszerzenie_pliku == True:
    print("Tak")
else:
    print("Nie")