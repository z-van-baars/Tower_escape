import random

class Mob(object):
    def __init__(self, name, hostile, health, attack, accuracy, loot):
        self.name = name
        self.hostile = hostile
        self.health = health
        self.attack = attack
        self.accuracy = accuracy
        self.loot = loot

def build_skele():
	return Mob("Skeleton", 1, 100, 1, 40, 1)
def build_rat():
	return Mob("Rat", 2, 25, 0.2, 60, 1)
def build_troll():
	return Mob("Troll", 1, 250, 3, 40, 2)
