from random import choice


class Warrior:
    def __init__(self, health=100):
        self.health = health

    def attack(self, opponent):
        opponent.health -= 20


fighter1 = Warrior()
fighter2 = Warrior()

while fighter1.health > 0 and fighter2.health > 0:
    attacker, defender = choice([(fighter1, fighter2), (fighter2, fighter1)])
    attacker.attack(defender)

    print(f"{'First' if attacker == fighter1 else 'Second'} strikes!")
    print(f"The {'second' if defender == fighter2 else 'first'} has {defender.health} health left")

if fighter1.health > 0:
    print("FIRST WINS")
else:
    print("SECOND WINS")
