plik = open("notowania_gieldowe.txt","r")

with plik as plik:
    plik.write("ALR, 113")

print(plik.read(plik))