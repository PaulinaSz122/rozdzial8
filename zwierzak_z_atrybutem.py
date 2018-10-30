class Critter(object):
    """Wirtualny pupil"""
    def __init__(self, name):
        print("Urodził się nowy zwierzak!")
        self.name = name

    def __str__(self):
        rep = "Obiekt klasy Critter\n"
        rep += "name: " + self.name + "\n"
        return rep

    def talk(self):
        print("Cześć! Jestem", self.name, "\n")


crit1 = Critter("Reksio")
crit2 = Critter("Pucek")

crit1.talk()
crit2.talk()

print("Wyświetlenie obiektu crit1:")
print(crit1)

print("Bezpośrednie wyświetlanie wartości atrybutu crit1.name:")
print(crit1.name)
