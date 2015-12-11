##battles.py
import random
import player
import creatures
import utilities

def move_eval():
    hit = "none"
    while hit == "none":
        move = "none"
        print("What kind of attack (Reckless // Normal // Cautious)")
        move = input("?")
        if move == "reckless":
            if (player.stats['Accuracy'] - random.randint(0, 100)) > 30:
                hit = (random.randint(1, 80) * player.stats['Attack'])
            else:
                hit = 0

        elif move == "normal":
            if (player.stats['Accuracy'] - random.randint(0, 100)) > 10:
                hit = (random.randint(15, 40) * player.stats['Attack'])
            else:
                hit = 0

        elif move == "cautious":
            if (player.stats['Accuracy'] - random.randint(0, 100)) > 0:
                hit = (random.randint(1, 15) * player.stats['Attack'])
            else:

        else:
            print("I don't recognize that command.")
            input("")
        utilities.turnbump(1)
    return hit

def battle():
    enemy = creatures.pick_enemy()
    utilities.turnbump(3)
    print("A wild " + enemy.name + " attacks!")
    while enemy.health > 0 and player.stats['Health'] > 0:
        utilities.turnbump(3)
        print("-------------------------------")
        print("Health : " + str(player.stats['Health']) + "               " + enemy.name +" Health : " + str(enemy.health))
        hit = move_eval()
        if hit > 0:
            print("Hit for: " + str(hit) + " damage!")
            enemy.health -= hit

        else:
            print("You missed!")
        input("Press Enter when ready --->")
        utilities.turnbump(1)
        if enemy.health > 0:
            if (enemy.accuracy - random.randint(0, 100)) > 0:
                enemy_hit = enemy.attack
                enemy_hit += random.randint(1, 10)
                player.stats['Health'] -= enemy_hit
                print("The enemy hit for: " + str(enemy_hit) + " damage!")

            else:
                print("The enemy's attack missed!")
            input("Press Enter when ready --->")
        elif player.stats['Health'] > 0:


            print("You defeated your foe!")
    input("Press enter when ready --->")

