
class PartyAnimal:
    x=0

    def __init__(self): #Declaracion de un constructor, tipicamente se usa para prepara laa variales
        print('I am constructor')

    def party(self):
        self.x = self.x+1
        print('So far',self.x)

    def __del__(self):#Declaracion de destructr, se usa raramente
        print('I am destructor', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print(an)
