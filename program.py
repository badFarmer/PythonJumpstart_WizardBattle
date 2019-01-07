import random

from actors import Wizard, Creature, Description, Location, ConcatText


def main():
    print_header()
    game_loop()


def print_header():
    print('------------------------')
    print('------WIZARD BASH-------')
    print('------------------------')


def game_loop():
    descriptions = [
        Description('dark'),
        Description('creepy'),
        Description('foggy'),
        Description('burning'),
        Description('grim'),
        Description('moaning'),
        Description('rippling'),
        Description('hellish'),
    ]

    locations = [
        Location('forest'),
        Location('bog'),
        Location('marsh'),
        Location('ravine'),
        Location('slough'),
        Location('hallow'),
        Location('field'),
        Location('hut'),
        Location('river'),
        Location('hovel'),
    ]

    concats = [
        ConcatText(', '),
        ConcatText(' and ')
    ]

    creatures = [
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000)
    ]

    hero = Wizard('Gandolf', 75)

    while True:
        active_description1 = random.choice(descriptions)
        active_description2 = random.choice(descriptions)
        active_concat = random.choice(concats)
        if active_description1.adjective == active_description2.adjective:
            active_description2.adjective = ''
            active_concat.text = ''
        active_location = random.choice(locations)
        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a {}{}{} {}...'.format(
            active_creature.name,
            active_creature.level,
            active_description1.adjective,
            active_concat.text,
            active_description2.adjective,
            active_location.noun
            ))
        cmd = input('Do you attack, runaway, or look around?')
        if cmd == 'a':
            print('penis')
        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print('look around.')
        else:
            print('OK, exiting game... bye!')
            break


if __name__ == '__main__':
    main()
