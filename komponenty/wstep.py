def wstepGry():
  
    print ("W tej grze będziesz wybierać opcje, które będą mieć swoje skutki w przyszłości")

    imie = input("podaj imie: ")

    print("Lecisz na wakacje, masz 10000 złotych. Wybierz miejsce: ")
    print("1. Grecja")
    print("2. Wietnam")
    print("3. Hiszpania")
    print("4. Malediwy")

    wybor = input("Twój wybór: ")

    if wybor == "1":
        pieniadze = 8000
    elif wybor == "2":
        pieniadze = 5000
    elif wybor == "3":
        pieniadze = 7000
    elif wybor == "4":
        pieniadze = 6000
    else:
        print ("Zły wybór. Zacznij od nowa")

    print (imie, "zostało ci:", pieniadze)
    return imie, pieniadze