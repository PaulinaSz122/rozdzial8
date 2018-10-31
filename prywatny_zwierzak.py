class Critter(object):
    """Wirtualny pupil"""
    def __init__(self, name, mood):
        print("Urodził się nowy zwierzak!")
        self.name = name
        self.__mood = mood

    def talk(self):
        print("\nJestem", self.name)
        print("W tej chwili czuję się", self.__mood, "\n")

    def __private_method(self):
        print("To jest metoda prywatna.")

    def public_method(self):
        print("To jest metoda publiczna.")
        self.__private_method()


crit = Critter(name="Reksio", mood="szczęśliwy")
crit.talk()
crit.public_method()
