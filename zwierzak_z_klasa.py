class Critter(object):
    """Wirtualny pupil"""
    total = 0

    @staticmethod
    def status():
        print("\nOgólna liczba zwierzaków wynosi", Critter.total)


    def __init__(self, name):
        self.name = name
        print("Urodził się nowy zwierzak!")
        Critter.total += 1


print("Uzyskanie dostępu do atrybutu klasy Critter.total:", end=" ")
print(Critter.total)

print("\nUtworzenie zwierzaków.")
crit1 = Critter("zwierzak 1")
crit2 = Critter("zwierzak 2")
crit3 = Critter("zwierzak 3")

Critter.status()

print("\nUzyskanie dostępu do atrybutu klasy poprzez obiekt:", end=" ")
print(crit1.total)
