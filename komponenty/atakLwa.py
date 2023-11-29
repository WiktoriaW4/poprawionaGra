import time


def atakLwa():
  
    print("Już ostatni dzień i jutro o 6:30 wylot ")
    time.sleep(1)
    print("Idziesz surfować i przejść się po safari")
    time.sleep(1)

    print("Surfowanie bardzo ci się spodobało i liczysz, na nastepny raz.")
    time.sleep(1)

    print("Idziesz sam na safari")
    time.sleep(1)

    print("Lew patrzy na ciebie i chce cię zaatakować. Co robisz ?")
    time.sleep(1)

    print("1. Uciekasz licząc, że cię nie dogoni")
    print("2. Stoisz w miejscu aby nie zwracać na niego niepotrzebnej uwagi")
    print("3. Rzucasz się do walki licząc, że jesteś silniejszy")

    decyzja5 = input("Twój wybór: ") 
    if decyzja5 == "1":
        print("Lew cię dogonił. Nie masz obu rąk.")
    elif decyzja5 == "2":
        print("Lew podszedł do ciebie, ale nic ci nie zrobił i po chwili odszedł")
    elif decyzja5 == "3":
        print("Lew cię pokonał i nie żyjesz. Zacznij od nowa")
        exit()