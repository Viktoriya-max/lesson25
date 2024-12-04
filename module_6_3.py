import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DENGER = 0
    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        self._cords[0] = dx.__mul__(self.speed)
        self._cords[1] = dy.__mul__(self.speed)
        self._cords[2] = dz.__mul__(self.speed)
        if self._cords[2].__lt__(0):
            print("It's too deep, i can't dive :(")
            self._cords = 0

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DENGER.__lt__(5):
            print("Sorry, i'm peaceful")
        elif self._DEGREE_OF_DENGER.__gt__(5):
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(f'{self.sound}')


class Bird(Animal):
    beak = True
    def lay_eggs(self):
        print(f'Here are(is) {random.randint(1,4)} egg(s) for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DENGER = 3
    def dive_in(self,dz):
        self._cords[2] = self._cords[2].__sub__(abs(dz).__mul__(self.speed.__floordiv__(2)))

class PoisonousAnimal(Animal):
    _DEGREE_OF_DENGER = 8

class Duckbill(PoisonousAnimal,AquaticAnimal, Bird):
    sound = "Click-Click-Click"


db = Duckbill(10)
print(db.live)
print(db.beak)

db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()

