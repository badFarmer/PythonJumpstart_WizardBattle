def main():
    print_header()


def print_header():
    print('------------------------')
    print('------WIZARD BASH-------')
    print('------------------------')


def game_loop():
    while True:

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


