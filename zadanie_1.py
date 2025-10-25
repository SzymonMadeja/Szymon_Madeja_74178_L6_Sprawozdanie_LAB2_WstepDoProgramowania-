wynik = int(input("Podaj wynik egzaminu (ile procent): "))

if wynik >= 80:
    print("Zdano egzamin w terminie 0")
elif wynik >= 50 and wynik <=80:
    print("Możesz poprawić wynik egzaminu")
else:
    print("Musisz poprawić wynik egzaminu")