class Critter(object):
    """Wirtualny pupil"""
    def __init__(self):
        print("Urodził się nowy zwierzak!")

    def talk(self):
        print("\nCześć! Jestem egzemplarzem klasy Critter.")


crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()
