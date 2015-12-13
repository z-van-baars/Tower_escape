import utilities

stats = {
    'Gold': 50,
    'Health': 100,
    'Mana': 50,
    'Stamina': 100,
    'Defense': 1.0,
    'Attack': 1.0,
    'R. Attack': 1.0,
    'Accuracy': 1.0,
    'Level': 1,
    'Experience': 0
}

inventory = {
    'Crooked Staff': 1,
    'Iron Dagger': 2,
    'White Cloak': 3
}


def xp_check(xp, l):

    xp_gate = 100 + ((l * 10 - 10) * (l * 10 - 10))
    if xp > xp_gate:
        levelup()


def levelup():

    utilities.turnbump(3)
    skill = "none"
    stats['Level'] += 1
    print("You leveled up to level: " + str(stats['Level']) + "!")
    print("+ + + + + + + + + + + + + + + + + + + + + + + + + +")
    for key in stats:
                print("{0} : {1}".format(key, stats[key]))
    utilities.turnbump(1)
    print("(H)ealth - (M)ana - (S)tamina - (D)efense - (A)ttack - (R)anged Attack - Accurac(Y)")
    skill = input("Pick a skill to increase:")
    print(str(skill))
    while skill == "none":

        if skill == "h" or skill == "H":
            stats['Health'] += 10
            print("Increased Health to: " + str(stats["Health"]))

        elif skill == "m" or skill == "M":
            stats['Mana'] += 5
            print("Increased Mana to: " + str(stats["Mana"]))

        elif skill == "s" or skill == "S":
            stats['Stamina'] += 5
            print("Increased Stamina to: " + str(stats["Stamina"]))

        elif skill == "d" or skill == "D":
            stats['Defense'] += 0.1
            print("Increased Defense to: " + str(stats["Defense"]))

        elif skill == "a" or skill == "A":
            stats['Attack'] += 0.1
            print("Increased Attack to: " + str(stats["Attack"]))

        elif skill == "r" or skill == "R":
            stats['R. Attack'] += 0.1
            print("Increased Ranged Attack to: " + str(stats["R. Attack"]))

        elif skill == "y" or skill == "Y":
            stats['Accuracy'] += 0.1
            print("Increased Accuracy to: " + str(stats["Accuracy"]))

        else:
            print("I don't recognize that command.")
            input("")
            skill = "none"
    input("")
    input("Press Enter to continue --->")
