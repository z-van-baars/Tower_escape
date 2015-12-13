import utilities

stats = {
    'Gold': 50,
    'Health': 100,
    'Max Health': 100,
    'Mana': 50,
    'Stamina': 100,
    'Defense': 1.0,
    'Attack': 1.0,
    'R. Attack': 1.0,
    'Accuracy': 1.0,
    'Level': 1,
    'Experience': 0,
    'Intelligence': 10,
    'Strength': 10,
    'Dexterity': 10
}

inventory = {
    'Crooked Staff': 1,
    'Iron Dagger': 2,
    'White Cloak': 3
}

spells = {}

spellbook = {
    '1': "Fireball",
    '2': "Shock",
    '3': "Heal"
}


def xp_check(xp, l):

    xp_gate = 100 + ((l * 10 - 10) * (l * 10 - 10))
    if xp > xp_gate:
        levelup()


def levelup():

    utilities.turnbump(3)
    skill = "none"
    stats['Level'] += 1
    stats['Max Health'] += 10
    stats['Health'] = stats['Max Health']
    print("You leveled up to level: " + str(stats['Level']) + "!")
    while skill == "none":
        print("+ + + + + + + + + + + + + + + + + + + + + + + + + +")
        for key in stats:
                print("{0} : {1}".format(key, stats[key]))
        utilities.turnbump(1)
        print("(S)trength // (D)exterity // (I)ntelligence")
        skill = input("Pick a skill to increase:")
        if skill == "s" or skill == "S":
            stats['Max Health'] += 5
            stats['Defense'] += 0.1
            stats['Attack'] += 0.1
            stats['Stamina'] += 5
            stats['Health'] = stats['Max Health']
            print("Increased Max Health to: " + str(stats['Max Health']))
            print("Increased Stamina to: " + str(stats["Stamina"]))
            print("Increased Attack to: " + str(stats["Attack"]))
            print("Increased Defense to: " + str(stats["Defense"]))

        elif skill == "d" or skill == "D":
            stats['R. Attack'] += 0.1
            stats['Accuracy'] += 0.1
            print("Increased Accuracy to: " + str(stats["Accuracy"]))
            print("Increased Ranged Attack to: " + str(stats["R. Attack"]))

        elif skill == "i" or skill == "I":
            stats['Mana'] += 10
            print("Increased Mana to: " + str(stats["Mana"]))

        else:
            print("I don't recognize that command.")
            input("")
            skill = "none"
    input("")
    input("Press Enter to continue --->")
