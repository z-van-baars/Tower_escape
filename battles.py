

import random
import player
import creatures
import utilities

enemy = "none"
dmg = 0


def attack_type():

    atk_type = "none"
    while atk_type == "none":
        print("Attack type: [P]hysical // [R]anged // [M]agic")
        atk_type = input("?")
        if atk_type == "p" or atk_type == "P":
            hit = phys_move_eval()
        elif atk_type == "r" or atk_type == "R":
            hit = ranged_move_eval()
        elif atk_type == "m" or atk_type == "M":
            hit = magic_move_eval()
        else:
            "I don't recognize that command."
            input("")
            atk_type = "none"
    return hit


def phys_move_eval():

    hit = "none"
    utilities.turnbump(1)
    while hit == "none":
        move = "none"
        print("What kind of attack ([R]eckless // [N]ormal // [C]autious)")
        move = input("?")
        utilities.turnbump(1)
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
            move = "none"
            utilities.turnbump(1)

    if hit > 0:
        print("Hit for: " + str(hit) + " damage!")

    else:
        print("You missed!")
    return hit


def ranged_move_eval():

    hit = "none"
    utilities.turnbump(1)
    while hit == "none":
        move = "none"
        print("Aim at: ([H]ead // [B]ody)")
        move = input("?")
        utilities.turnbump(1)
        if move == "h" or move == "H":
            if (random.randint(0, 100) * player.stats['Accuracy']) > 70:
                hit = round(random.randint(40, 80) * player.stats['R. Attack'])
            else:
                hit = 0

        elif move == "m" or move == "M":
            if (random.randint(0, 100) * player.stats['Accuracy']) > 45:
                hit = round(random.randint(5, 20) * player.stats['R. Attack'])
            else:
                hit = 0

        else:
            print("I don't recognize that command.")
            input("")
            utilities.turnbump(1)
    if hit > 0:
        print("Hit for: " + str(hit) + " damage!") 

    else:
        print("You missed!")
    return hit


def magic_move_eval():

    hit = "none"
    utilities.turnbump(1)
    while hit == "none":
        move = "none"
        print("What spell ? (1) " + player.spellbook['1'] + " // (2) " + player.spellbook['2'] + " // (3) " + player.spellbook['3'])
        move = input("?")
        utilities.turnbump(1)
        if move == "1":
            if random.randint(0, 100) > 50:
                hit = round(random.randint(20, 30) * (player.stats['Intelligence'] / 10))
            else:
                print("You missed!")
                hit = 0

        elif move == "2":
            if random.randint(0, 100) > 40:
                hit = round(random.randint(20, 25) * (player.stats['Intelligence'] / 10))
            else:
                print("You missed!")
                hit = 0

        elif move == "3":
            if player.stats['Health'] < player.stats['Max Health']:
                heal = 10
                if (player.stats['Health'] + heal) > player.stats['Max Health']:
                    heal = player.stats['Max Health'] - player.stats['Health']
                player.stats['Health'] += heal
                print("Healed " + str(heal) + " Health")
                print("Health : " + str(player.stats['Health']) + "/" + str(player.stats['Max Health']))
                hit = 0
            else:
                print("Oak: You can't use that here!")
                input("You are already at full health!")
                utilities.turnbump(1)
                move = "none"

        else:
            input("I don't recognize that command.")
            utilities.turnbump(1)
            move = "none"
    if hit > 0:
        print("Hit for: " + str(hit) + " damage!")
    return hit


def battle():

    enemy = creatures.pick_enemy()
    utilities.turnbump(3)
    print("A wild " + enemy.name + " attacks!")
    input("")
    while enemy.health > 0 and player.stats['Health'] > 0:
        utilities.turnbump(3)
        print("Health : " + str(player.stats['Health']) + "/" + str(player.stats['Max Health']) + " - - - - - - - - - " + enemy.name +" Health : " + str(enemy.health))
        print("__________________________________________________________")
        dmg = attack_type()
        enemy.health -= dmg
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
