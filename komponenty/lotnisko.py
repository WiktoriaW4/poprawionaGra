import random
import time

def lotnisko():
    print("Jedziesz już na lotnisko")
    def losujMiejsce():
        miejsca = ["przy oknie", "po środku", "przy przejściu", "w biznes klasie"]
        wylosowane_miejsce = random.choice(miejsca)
        return wylosowane_miejsce
    if __name__ == "_main_":
        wylosowane_miejsce = losujMiejsce()
        print("Masz miejsce", wylosowane_miejsce)
    time.sleep(1)
    print ("Doleciałeś już do zamierzonego kraju")
    time.sleep(1)