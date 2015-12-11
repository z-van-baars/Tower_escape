


import random

class Floor(object):
    def __init__(self, name, size, danger, cleared, searched):
        self.name = name
        self.size = size
        self.danger = danger
        self.cleared = cleared
        self.searched = searched

class Mob(object):
    def __init__(self, name, hostile, health, attack, loot):
        self.name = name
        self.hostile = hostile
        self.health = health
        self.attack = attack
        self.loot = loot

skeleton = Mob("Skeleton", 1, 100, 0.5, 1)


inventory = {
    'Crooked Staff': 1,
    'Iron Dagger': 2,
    'White Cloak': 3
}

stats = {
    'Gold': 50,
    'Health': 100,  
    'Mana': 50, 
    'Stamina': 100,
    'Defense': 1.0,
    'Attack': 1.0,
    'R. Attack': 1.0,
    'Level': 1,
    'Experience': 0
}

def turnbump(numlines): 
    for line in range(numlines):
        print(" ")

def explore():
    if floors[floor].searched == 0:
        if random.randint(1, 100) < floors[floor].danger:
                    print("A WILD SKELETON APPEARED!!!")
                    input("hit enter when ready --->")
                    turnbump(3)
                    battle()
                    
    else:
        print("You've already searched this floor!")
        input("")
        input("hit enter when ready")

def battle():
    move = "none"
    enemy = skeleton
    while enemy.health > 0:
        turnbump(3)
        print("-------------------------------")
        print("Health : " + str(stats['Health']) + "/ Enemy Health : " + str(enemy.health))
        print("What kind of attack (Reckless // Normal // Cautious)")
        hit = 0
        move = input("?")
        if move == "reckless":
            hit = (random.randint(15, 40) * stats['Attack'])
        

        if move == "normal":
            hit = (random.randint(15, 40) * stats['Attack'])
        

        if move == "cautious":
            hit -= (random.randint(1, 40) * stats['Attack'])

        if hit > 0:
            turnbump(1)
            print("Hit for: " + str(hit) + " damage!")
            enemy.health -= hit
            input("")
        else:
            print("I don't recognize that command.")
            input("")
    print("You defeated your foe!")
    input("Press enter when ready --->")



#creating initial condition variables

floors = [

    Floor("1st Floor", 1, 100, 0, 0),
    Floor("2nd Floor", 2, 50, 0, 0),
    Floor("3rd Floor", 3, 50, 0, 0),
    Floor("4th Floor", 4, 20, 0, 0),
    Floor("5th Floor", 5, 0, 0, 0)
    ]

floor = 4
action = "none"
z = 0
gamerun = "y"


#main game loop
while gamerun == "y":
    turnbump(21)
    print(" +++ ESCAPE THE EVIL WIZARD'S TOWER!!! +++ ")
    print(" -----------------------------------------")
    while action != "escape" or stats["health"] >= 1:
        turnbump(3)
        print("You're on the " + floors[floor].name)
        print("------------------------------------")
        print("WHATDO?")
        action = input("?")

        ## Battle function tester
        if action == "battle":
            battle()


        elif action == "stats":
            for key in stats:
                print("{0}:{1}".format(key, stats[key]))
            input("hit enter when ready --->")
            turnbump(21)

        elif action == "floor":
            print(str(floors[floor].name))

        elif action == "attack":
            print(stats['Attack'])

        elif action == "explore":
            explore()

        #can't go below floor 1
        elif action == "down" and floor > 0:
            if floor > 0:
                if floors[floor].cleared == 0:

                    if random.randint(1, 100) < floors[floor].danger:
                        print("A WILD SKELETON APPEARED!!!")
                        input("hit enter when ready --->")
                        battle()

                    else:
                        print("you may pass")
                        input("hit enter when ready --->")
                        floors[floor].cleared = 1
                floor -= 1
            else:
                "You can't go any lower!"
                input("")
            turnbump(3)

        #can't go above floor 5
        elif action == "up":
            if floor != 4:
                floor += 1
            else:
                print("You can't go any higher!")
                input("")
            turnbump(3)

        else:
            print("I don't recognize that command maingame.")
            input("")
            turnbump(3)




    turnbump(1)

    if stats["health"] < 1:
        print("You succumb to your wounds")

    else:
        #win conditions
        print("++++++++++++++++++++++++++++")
        print("+                                  +")
        print("+++You Saved the Kingdom!+++")
        print("++++++++++++++++++++++++++++")


    gamerun = input("play again(y/n?")
    y = 0



