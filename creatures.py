import random

class Mob(object):
    def __init__(self, name, hostile, health, attack, accuracy, loot):
        self.name = name
        self.hostile = hostile
        self.health = health
        self.attack = attack
        self.accuracy = accuracy
        self.loot = loot


skeleton = Mob("Skeleton", 1, 100, 1, 40, 1)
rat = Mob("Rat", 2, 25, 0.2, 60, 1)
troll = Mob("Troll", 1, 250, 3, 40, 2)

hostiles = [
	skeleton,
	rat,
	troll
]

def creature_picker():
	a = random.choice(hostiles)
	instancecreature.Mob = Mob(hostiles[a].name, hostiles[a].hostile, hostiles[a].health, hostiles[a].attack, hostiles[a].accuracy, hostiles[a].loot)
	return instancecreature