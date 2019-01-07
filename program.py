import random

from actors import Wizard, Creature, Description, Location, ConcatText


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
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000)
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
            print('attack')
        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print('look around.')
        else:
            print('OK, exiting game... bye!')
            break


if __name__ == '__main__':
    main()
