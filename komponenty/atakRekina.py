import time

def atakRekina(pieniadze):

    print("Jest już kolejny dzień, idziesz na śniadanie")
    time.sleep(1)
    print("Postanowiłeś, że dzisiaj spędzisz dzień na plaży")
    time.sleep(1)

    def atak_rekina():
        print("Zauważasz cień w wodzie")
        time.sleep(1)
        print("To rekin!!! Płynie w twoją strone")
        time.sleep(1)
        print("co robisz ?")
        time.sleep(1)

    def sposob_obrony():
        print("Wybierz sposób obrony:")
        print("1. Szybko odpływasz")
        print("2. Nie robisz gwałtowych ruchów i powoli płyniesz do brzegu")
        print("3. Rzucasz w wode coś co odwróci jego uwage")
        print("4. Postanawiasz z nim zawalczyć")
    
        wybor4 = input("Twój wybór: ")
        return wybor4

    def rozpocznij_gre():
        atak_rekina()

        wybor_sposobu = sposob_obrony()

        if wybor_sposobu == "1":
            print("Przeżyłeś, ale rekin odgryzł twoją nogę.")
        elif wybor_sposobu == "2":
            print("Najlepszy sposób, udało ci się spokojnie dopłynąć")
        elif wybor_sposobu == "3":
            print("Rekin popłynął za przedmiotem, ale potem znów do ciebie wrócił i był bardziej rozwścieczony. Umarłeś, koniec gry")
            exit()
        elif wybor_sposobu == "4":
            print("Najgorsza decyzja. Umierasz , koniec gry")
            exit()
        else:
            print("nieprawidłowy wybór.")

    rozpocznij_gre()

    print("Wróciłeś z plaży i teraz idziesz kupić pamiątki")

    pieniadze = pieniadze - 300
    print("Zostało ci", pieniadze)
    time.sleep(1)