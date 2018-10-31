class Critter(object):
    """Wirtualny pupil"""
    def __init__(self, name):
        print("Urodził się nowy zwierzak!")
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Pusty łańcuch znaków nie może być imieniem zwierzaka.")
        else:
            self.__name = new_name
            print("Zmiana imienia powiodła się.")

    def talk(self):
        print("\nCześć! Jestem", self.name)


crit = Critter("Reksio")
crit.talk()

print("\nImię mojego zwierzaka to:", end=" ")
print(crit.name)

print("\nPróbuję zmienić imię zwierzaka na Pucek...")
crit.name = "Pucek"

print("\nImię mojego zwierzaka to:", end=" ")
print(crit.name)

print("\nPróbuję zmienić imię zwierzaka na pusty łańcuch znaków...")
crit.name = ""

print("\nImię mojego zwierzaka to:", end=" ")
print(crit.name)
