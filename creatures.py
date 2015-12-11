import random

class Mob(object):
    def __init__(self, name, hostile, health, attack, accuracy, loot, xp):
        self.name = name
        self.hostile = hostile
        self.health = health
        self.attack = attack
        self.accuracy = accuracy
        self.loot = loot
        self.xp = xp

def build_goblin():
	return Mob("Goblin", 1, 120, 1, 1.2, 0.60, 25)
def build_skele():
	return Mob("Skeleton", 1, 100, 1, 1.4, 0.35, 20)
def build_rat():
	return Mob("Rat", 2, 25, 0.2, 1.0, 0.1, 5)
def build_troll():
	return Mob("Troll", 1, 250, 3, 0.8, 5.0, 200)

hostile_npcs = [
  build_goblin,
  build_goblin,
  build_skele,
  build_skele,
  build_skele,
  build_skele,
  build_skele,
  build_rat,
  build_rat,
  build_rat,
  build_troll,
  ]
  
def pick_enemy():
	return random.choice(hostile_npcs)()