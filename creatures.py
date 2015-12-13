import random


class Mob(object):

    def __init__(self, name, hostile, health, attack, accuracy, pierce, resistance, loot, xp):
        self.name = name
        self.hostile = hostile
        self.health = health
        self.attack = attack
        self.accuracy = accuracy
        self.pierce = pierce
        self.resistance = resistance
        self.loot = loot
        self.xp = xp

enemy = Mob("Name", 3, 0, 0, 0, 0, 0, 0, 0)


def build_goblin():
    return Mob("Goblin", 1, 120, 1, 1.2, 1, 1, 0.60, 25)


def build_skele():
    return Mob("Skeleton", 1, 100, 1, 1.4, 1, 1, 0.35, 20)


def build_rat():
    return Mob("Rat", 2, 25, 0.2, 1.0, 1, 1, 0.1, 5)


def build_troll():
    return Mob("Troll", 1, 250, 3, 0.8, 1, 1, 5.0, 200)

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
  build_troll,
  build_troll,
  build_troll,
  build_troll,
  build_troll,
  build_troll,
  build_troll,
  build_troll
  ]


def pick_enemy():

    a = random.choice(hostile_npcs)
    return a()
