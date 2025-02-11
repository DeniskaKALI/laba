from random import randint
import itertools


class Person:
    count = itertools.count()

    def __init__(self, team=randint(1, 2)):
        self.id = next(Person.count)
        self.team = team


class Hero(Person):
    pass


class Soldier(Person):
    pass


h1 = Hero(1)
h2 = Hero(2)
army1 = []
army2 = []

for i in range(20):
    soldier = Soldier()
    if soldier.team == 1:
        army1.append(soldier)
    else:
        army2.append(soldier)

print("Army 1 size:", len(army1))
print("Army 2 size:", len(army2))
