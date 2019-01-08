import random
import time

from actors import Wizard, Creature, SmallAnimal, Dragon

def main():
    print_header()
    game_loop()


def print_header():
    print('------------------------')
    print('------WIZARD BASH-------')
    print('------------------------')


def location_generator():
    adjectives = [
        'dark',
        'creepy',
        'foggy',
        'grim',
        'moaning',
        'rippling',
        'hellish',
        'sleepy',
        'foul',
        'unclean',
        'grimy',
        'stanky',
        'wretched',
        'astral',
        'squeeling'
    ]
    terrains = [
        'forest',
        'bog',
        'marsh',
        'ravine',
        'slough',
        'hallow',
        'field',
        'hut',
        'river',
        'hovel',
        'plane',
        'portal'
    ]
    adjective1 = random.choice(adjectives)
    adjective2 = random.choice(adjectives)
    terrain = random.choice(terrains)
    descriptions = [
        " a {} and {} {}.".format(adjective1, adjective2, terrain),
        " a {}, {} {}".format(adjective1, adjective2, terrain),
        " a {} {}".format(adjective1, terrain)
    ]

    if adjective1 == adjective2:
        description = descriptions[3]
    else:
        description = random.choice(descriptions)

    return description


def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 50, True),
        Wizard('Evil Wizard', 1000)
    ]

    hero = Wizard('Gandolf', 75)

    while True:
        location = location_generator()
        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from{}...'.format(
            active_creature.name,
            active_creature.level,
            location
        ))
        cmd = input('Do you attack, runaway, or look around?')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides to recover strength.")
                time.sleep(5)
                print("The wizard returns revitalized.")
        elif cmd == 'r':
            print('The wizard doubts his power and runs away.')
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:'.format(hero.name))
            for c in creatures:
                print('* A {} of level {}'.format(
                    c.name, c.level
                ))
        else:
            print('OK, exiting game... bye!')
            break

        if not creatures:
            print("You've defeated all the creatures.")
            break

if __name__ == '__main__':
    main()
