import random

def tabliczkaMnozenia():
    print("Lecisz samolotem i bardzo ci się nudzi, dlatego odpalasz krótki test mnożenia")

    def zadaj_pytanie():
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        dobra_odp = num1 * num2
        return num1, num2, dobra_odp

    def zadaj_pyt(pytanie):
        num1, num2, dobra_odp = pytanie
        zadawanie = input(f"Ile to jest {num1} * {num2}? ")

        try:
            zadawanie = int(zadawanie)
            if zadawanie == dobra_odp:
                print("Dobra odpowiedź")
                return True
            else:
                print(f"Zła odpowiedź. Poprawna odpowiedź to {dobra_odp}.")
                return False
        except ValueError:
            print("Podaj dobrą liczbę.")
            return False

    def main():
        print("Test mnożenia")
        ilosc_pytan = 5
        dobre_odp = 0

        for _ in range(ilosc_pytan):
            pytanie = zadaj_pytanie()
            dobre_odp += zadaj_pyt(pytanie)

        print(f"Twój wynik: {dobre_odp}/{ilosc_pytan} dobre odpowiedzi.")
    
    main()
