import time

def bagaz():
    print("Jesteś już spakowany i gotowy do wyjścia. Sprawdź ostatnią rzecz.")
    waga = float(input("Ile kilogramów waży twoja walizka ? : "))
    if waga < 25:
        print("Prawidłowa masa")
    else:
        print("Wypakuj trochę rzeczy")
        time.sleep(1)