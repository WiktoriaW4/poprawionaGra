def wyboryPierwszegoDnia():
    
    print("Wybierz co chcesz teraz robić")

    print("1. Idziesz na plaże")
    print("2. Zwiedzasz zabytki")
    print("3. Rozmawiasz z nowymi ludźmi")
    print("4. Zostajesz w pokoju")

    wybor3 = input("Twój wybór: ")

    if wybor3 == "1":
        print("Jesteś na plaży, wybierz zajęcie")
        print("A. Pływanie z rybami i płaszczkami")
        print("B. Opalanie się")
        print("C. przejażdżka skuterem wodnym")
    
        wybordwa = input("twój wybor: ")

    elif wybor3 == "2":
        print("Jesteś w centrum, gdzie idziesz")
        print("A. Do kawiarni")
        print("B. Do muzeum")
        print("C. Do najlepszej restauracji")

        wybortrzy = input("twój wybór: ")

    elif wybor3 == "3":
        print("Poznajesz nowe osoby, kolejne pytanie jakie im zadasz to: ")
        print("A. Skąd są")
        print("B. Czy mają jakieś zwierzęta")
        print("C. Jakie są ich zainteresowania")

        wyborcztery = input("twój wybor: ")

    elif wybor3 == "4":
        print("Zostajesz w pokoju, co będziesz robić")
        print("A. Oglądać telewizje")
        print("B. Uczyć się słów w regionalnym języku")
        print("C. Odpoczywać lub spać")

        wyborpiec = input("twój wybor: ")
    else:
        print ("Zły wybór. zacznij od nowa.")