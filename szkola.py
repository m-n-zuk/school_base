class Uczen:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    def przedstawSie(self):
        return f"{self.imie} {self.nazwisko}"

class UczenController:
    def __init__(self):
        self.listaUczniow = []

    def dodajUcznia (self, imie, nazwisko):
        uczen = Uczen(imie, nazwisko)
        self.listaUczniow.append(uczen)
        print("Uczeń został pomyślnie dodany!")

    def pokazUczniow (self):

        for i in self.listaUczniow:
            print(i.przedstawSie())

    def sprawdzUcznia (self, nazwisko):
        index = -1
        for i, v in enumerate(self.listaUczniow):
            if (v.nazwisko == nazwisko):
                index = i
        return index

    def usunUcznia (self, index):
        self.listaUczniow.pop(index) # pop usuwa po indeksie, a remove po wartosci
        print("Uczeń został pomyślnie usunięty!")

    def edytujUcznia(self, index, noweImie, noweNazwisko):
        if (noweImie != ""):
            self.listaUczniow[index].imie = noweImie #listaUczniow[index]  to moj obiekt, ktory jest obiektem na liscie
        if (noweNazwisko != ""):
            self.listaUczniow[index].nazwisko = noweNazwisko
        print("Dane zostały zmienione!")

        # if (znaleziono == False):
        #     print("Znajomy nie został odnaleziony.")
        #     dec = input("Czy szukamy jeszcze raz ? t/n").upper()
        #     if (dec == "T"):
        #         continue
        #     else:
        #         break

class Szkola (UczenController):
    def __init__(self, nazwaSzkoly):
        super().__init__()
        self.nazwaSzkoly = nazwaSzkoly
        self.menu()

    def menu(self):
        while (True):
            print(f"\nWitaj w szkole {self.nazwaSzkoly}!")
            menu = int(input("1 - dodaj ucznia, 2 - pokaz uczniow, 3 - usun ucznia, 4 - edytuj ucznia, 5 - koniec\n"))

            if (menu == 1):
                imie = input("Podaj imię: ")
                nazwisko = input("Podaj nazwisko: ")
                self.dodajUcznia(imie, nazwisko)

            elif (menu == 2):
                print(f"Lista uczniów w {self.nazwaSzkoly}:")
                self.pokazUczniow()

            elif (menu == 3):
                nazwisko = input("Podaj nazwisko ucznia do usunięcia: ")
                index = self.sprawdzUcznia(nazwisko)
                if(index > -1):
                    self.usunUcznia(index)
                else:
                    print("Uczeń nie został odnaleziony.")

            elif (menu == 4):
                nazwisko = input("Podaj nazwisko ucznia do edycji: ")
                index = self.sprawdzUcznia(nazwisko)
                if (index > -1):
                    print("Uczeń został odnaleziony! Podaj jego nowe dane:")
                    noweImie = input("Podaj nowe imię: ")
                    noweNazwisko = input("Podaj nowe nazwisko: ")
                    self.edytujUcznia(index, noweImie, noweNazwisko)
                else:
                    print("Uczeń nie został odnaleziony.")

            elif (menu == 5):
                print("koniec")
                break

            else:
                print("Opcja nierozpoznana")

szkola = Szkola("Politechnika Wrocławska")