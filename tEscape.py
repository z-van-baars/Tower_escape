


import random
import battles
import player
import creatures
import utilities

class Floor(object):
    def __init__(self, name, size, danger, cleared, searched):
        self.name = name
        self.size = size
        self.danger = danger
        self.cleared = cleared
        self.searched = searched


def explore():
    if floors[floor].searched == 0:
        if random.randint(1, 100) < floors[floor].danger:
                    print("A WILD SKELETON APPEARED!!!")
                    input("hit enter when ready --->")
                    utilities.turnbump(3)
                    battles.battle()
                    
    else:
        print("You've already searched this floor!")
        input("")
        input("hit enter when ready")

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
    utilities.turnbump(21)
    print(" +++ ESCAPE THE EVIL WIZARD'S TOWER!!! +++ ")
    print(" -----------------------------------------")
    while action != "escape" or player.stats["health"] >= 1:
        utilities.turnbump(3)
        print("You're on the " + floors[floor].name)
        print("------------------------------------")
        print("WHATDO?")
        action = input("?")

        ## Battle function tester
        if action == "battle":
            battles.battle()


        elif action == "stats":
            for key in player.stats:
                print("{0}:{1}".format(key, player.stats[key]))
            input("hit enter when ready --->")
            utilities.turnbump(21)

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
                        battles.battle()

                    else:
                        print("you may pass")
                        input("hit enter when ready --->")
                        floors[floor].cleared = 1
                floor -= 1
            else:
                "You can't go any lower!"
                input("")
            utilities.turnbump(3)

        #can't go above floor 5
        elif action == "up":
            if floor != 4:
                floor += 1
            else:
                print("You can't go any higher!")
                input("")
            utilities.turnbump(3)

        else:
            print("I don't recognize that command maingame.")
            input("")
            utilities.turnbump(3)




    utilities.turnbump(1)

    if stats["health"] < 1:
        print("You succumb to your wounds")

    else:
        #win conditions
        print("++++++++++++++++++++++++++++")
        print("+                          +")
        print("+++You Saved the Kingdom!+++")
        print("++++++++++++++++++++++++++++")


    gamerun = input("play again(y/n?")
    y = 0



