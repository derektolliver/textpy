import random

class Hero:

    # instance variables
    # title - name of hero/character
    # health - amount of life as an int
    # level

    def createHero(name):
        self.title = name
        self.health = random.random()

    def levelup():
        self.level += 1
        self.health += random.random()
