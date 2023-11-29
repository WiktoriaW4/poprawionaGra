import random

def pogoda():
    def losuj_pogode():
        pogoda = ["upalnie", "gorąco", "słonecznie"]
        wylosowana_pogoda = random.choice(pogoda)
        return wylosowana_pogoda
    if __name__ == "__main__":
        wylosowana_pogoda = losuj_pogode()
        print("Jest", wylosowana_pogoda)