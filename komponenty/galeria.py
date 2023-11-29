def galeria(pieniadze):
    wybor2 = input("Jesteś w galerii. Czy chcesz kupić sobie nowe ubrania i akcesoria ? (tak/nie):")
    if wybor2 == "tak":
        print ("kapelusz - 50 ")
        print ("okulary - 40 ")
        print ("krem - 90 ")
        print ("koszulka - 80 ")
        zakupy = float(input("Ile wydajesz ? : "))
        pieniadze = pieniadze - zakupy
        print("zostało ci", pieniadze)
    else:
        print("zostało ci", pieniadze)
    return pieniadze