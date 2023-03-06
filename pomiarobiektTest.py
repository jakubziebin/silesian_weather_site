class Pomiar:
    #touple pomiarów ( [temperatura], [co2], [hałas])
    def __init__(self, wartosci):
        self._wartosci = wartosci

    def __str__(self):
        return f"Temperatura = {self._wartosci[0]}\nCO2 = {self._wartosci[1]}\nhałas = {self._wartosci[2]}"

    def get_pomiar(self):
        #getter tuple z danym setem pomiarów
        return self._wartosci

    def set_pomiar(self, wartosci):
        self._wartosci = wartosci

def main():
    pomiar = get_pomiarInput()
    print(pomiar)


def get_pomiarInput():
    wartosci = []
    print("Podaj kolejno temp, co2, halas: ")
    for i in range(3):
        wartosci.append(input())
    wartosci = tuple(wartosci)    
    return Pomiar(wartosci)

if __name__ == "__main__":
    main()