

import random
import player
import creatures
import utilities


def move_eval():
    hit = "none"
    while hit == "none":
        move = "none"
        print("What kind of attack ([R]eckless // [N]ormal // [C]autious)")
        move = input("?")
        if move == "r" or move == "R":
            if (random.randint(0, 100) * player.stats['Accuracy']) > 50:
                hit = round(random.randint(40, 80) * player.stats['Attack'])
            else:
                hit = 0

        elif move == "n" or move == "N":
            if (random.randint(0, 100) * player.stats['Accuracy']) > 15:
                hit = round(random.randint(15, 40) * player.stats['Attack'])
            else:
                hit = 0

        elif move == "c" or move == "C":
            if (random.randint(0, 100) * player.stats['Accuracy']) > 5:
                hit = round(random.randint(2, 15) * player.stats['Attack'])
            else:
                hit = 0

        else:
            print("I don't recognize that command.")
            input("")
        utilities.turnbump(1)
    return hit


def battle():
    enemy = creatures.pick_enemy()
    utilities.turnbump(3)
    print("A wild " + enemy.name + " attacks!")
    input("")
    while enemy.health > 0 and player.stats['Health'] > 0:
        utilities.turnbump(3)
        print("Health : " + str(player.stats['Health']) + " - - - - - - - - - - - - " + enemy.name +" Health : " + str(enemy.health))
        print("__________________________________________________________")
        hit = move_eval()
        if hit > 0:
            print("Hit for: " + str(hit) + " damage!")
            enemy.health -= hit

        else:
            print("You missed!")
        input("Press Enter when ready --->")
        utilities.turnbump(1)
        if enemy.health > 0:
            if (random.randint(0, 100) * enemy.accuracy) > 25:
                enemy_hit = enemy.attack
                enemy_hit *= random.randint(1, 10)
                enemy_hit = round(enemy_hit)
                player.stats['Health'] -= enemy_hit
                print("The enemy hit for: " + str(enemy_hit) + " damage!")

            else:
                print("The enemy's attack missed!")
            input("Press Enter when ready --->")
        else:
            print("You defeated your foe!")
            input("")
            xp_range = round(enemy.xp * 1.1)
            exp = enemy.xp + random.randint(0, xp_range)
            gold_drop = round(enemy.loot * random.randint(0, 100))
            print(enemy.name + " dropped " + str(gold_drop) + " gold coin(s)!")
            player.stats['Gold'] += gold_drop
            player.stats['Experience'] += exp
            input(" ")
            print("Gained " + str(exp) + " XP!")
            input("")
    input("Press Enter when ready --->")
