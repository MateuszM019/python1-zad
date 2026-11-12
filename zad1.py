ekwipunek = {
     "vandal": {"ilosc": 1, "waga": 9, "wartosc": 20},
    "leczenie": {"ilosc": 2, "waga": 4, "wartosc": 10}        
 }

gold = 50
maksymalna_waga = 40

def pokaz_przedmioty(ekwipunek):
    for nazwa,przedmioty in ekwipunek.items():
        print(nazwa,przedmioty["ilosc"])

def dodaj_przedmiot(ekwipunek):
    nazwa_przedmiotu = input("Podaj nazwe nowego przedmiotu: ")

    if nazwa_przedmiotu in ekwipunek:
        waga = ekwipunek[nazwa_przedmiotu]["waga"]
    else:
        waga = int(input("Podaj wagę nowego przedmiotu: "))
        wartosc = int(input("Podaj wartość nowego przedmiotu: "))

    if policz_wage(ekwipunek) + waga > maksymalna_waga:
        print("Ekwipunek jest za ciężki.")
        return

    if nazwa_przedmiotu in ekwipunek:
        ekwipunek[nazwa_przedmiotu]["ilosc"] += 1
    else:
        ekwipunek[nazwa_przedmiotu] = {"ilosc": 1, "waga": waga , "wartosc":wartosc}

def uzyj_przedmiot(ekwipunek):
    nazwa_uzywanego_przedmiotu = input("Podaj nazwe uzywanego przedmiotu: ")
    
    if nazwa_uzywanego_przedmiotu in ekwipunek:
        ekwipunek[nazwa_uzywanego_przedmiotu]["ilosc"] -= 1
        print("Zostało sztuk:", ekwipunek[nazwa_uzywanego_przedmiotu]["ilosc"])

        if ekwipunek[nazwa_uzywanego_przedmiotu]["ilosc"] == 0:
            del ekwipunek[nazwa_uzywanego_przedmiotu]
            print(nazwa_uzywanego_przedmiotu,"zostal usuniety")

    else:
        print("Nie posiadasz takiego przedmiotu")


def sprawdz_przedmiot(ekwipunek):
    nazwa_do_sprawdzenia = input("Podaj nazwe przedmiotu do sprawdzenia: ")
    if nazwa_do_sprawdzenia in ekwipunek:
        print("posiadasz ten przedmiot")
    else:
        print("Nie masz tego przedmiotu")

def policz_wage(ekwipunek):
    suma = 0
    for przedmiot in ekwipunek.values():
        suma += przedmiot["ilosc"] * przedmiot["waga"]
    return suma

def sprzedaj_przedmiot(ekwipunek, gold):
    nazwa = input("Co chcesz sprzedać? ")

    if nazwa not in ekwipunek:
        print("Nie masz tego przedmiotu.")
        return gold

    wartosc = ekwipunek[nazwa]["wartosc"]
    ekwipunek[nazwa]["ilosc"] -= 1

    if ekwipunek[nazwa]["ilosc"] == 0:
        del ekwipunek[nazwa]

    print("Sprzedano", nazwa, "za", wartosc, "złota.")
    return gold + wartosc


while True:
    print("Wybierz opcje za pomoca numerkow aby wyswietlic zawartosc")
    print()
    print("1-Pokaz przedmioty")
    print("2-Dodaj przedmioty")
    print("3-Użyj przedmiotu")
    print("4-Sprawdź przedmiot")
    print("5-Sprzedaj przedmiot")
    print("6-Wyjdź")

    opcja = int(input("Wybierz numer: "))
    if opcja == 1:
        pokaz_przedmioty(ekwipunek)

    elif opcja == 2:
        dodaj_przedmiot(ekwipunek)

    elif opcja == 3:
        uzyj_przedmiot(ekwipunek)

    elif opcja == 4:
        sprawdz_przedmiot(ekwipunek)

    elif opcja == 5:
        sprzedaj_przedmiot(ekwipunek, gold)
        
    elif opcja == 6:
        break
    else:
        print("Ta opcja nie istnieje")





