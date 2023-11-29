import time

def wyboryTrzeciegoDnia(imie): 
    print(imie, "zostały ci 3 dni")
    time.sleep(1)

    print("Wybierz zestaw atrakcji na dzisiaj")
    print("1. spacer, wycieczka po mieście z przewodnikiem, nurkowanie na 10 metrach")
    print("2. pływanie jachtem, zwiedzenie pobliskiego miasta")
    print("3. lot paralotnią, odwiedzenie zoo, hotelowe zawody pływackie")

    decyzja = input("Twój wybór: ")
    if decyzja == "1":
        print("Super spedziłeś dzień")
    elif decyzja == "2":
        print("Nie był to najciekawszy dzień na tym wyjeździe")
    elif decyzja == "3":
        print("Najlepszy dzień jaki tu przeżyłeś.")
    time.sleep(1)

    print("Pani recepcjonistka zaproponawała ci przejazd do wesołego miasteczka")
    time.sleep(1)

    print("Zgadzasz się i wyruszasz w droge")
    time.sleep(1)

    print("Jesteś już na miejscu. Na którą atrakcje idziesz najpierw ?")
    print("1. Mega szybki rollercoaster")
    print("2. Huśtawki na wysokości 30 metrów")
    print("3. Dom strachów")

    decyzja2 = input("Twój wybór: ")
    if decyzja2 == "1":
        print("Bardzo fajna atrakcja, ale trochę zbyt szybka")
    elif decyzja2 == "2":
        print("Najlepsza atrakcja w twoim życiu!")
    elif decyzja2 == "3":
        print("Prawie dostałeś zawału serca. Wyszedłeś przerażony")