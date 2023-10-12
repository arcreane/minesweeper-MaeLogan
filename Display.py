def lose():
    print("\n\n")
    print(""" ___ ___                    __                             
|   |   |.-----..--.--.    |  |.-----..-----..-----..-----.
 \     / |  _  ||  |  |    |  ||  _  ||  _  ||__ --||  -__|
  |___|  |_____||_____|    |__||_____||_____||_____||_____|
                                                           """)
    quit()


def win():
    print("\n\n")
    print(""" ___ ___                    ________  __        
|   |   |.-----..--.--.    |  |  |  ||__|.-----.
 \     / |  _  ||  |  |    |  |  |  ||  ||     |
  |___|  |_____||_____|    |________||__||__|__|


""")

def print_map(map_game):
    compt_x = 0
    for line in map_game:
        print(compt_x, end="\t")
        compt_x = compt_x + 1
        for tile in line:
            if tile == 1:
                print("⬛  ", end="")
            elif tile == 2:
                print("⚑  ", end="")
            elif tile == 3:
                print("⬜  ", end="")
            elif tile > 3:
                print(tile - 3, " ", end="")

        print()

    print("\t", end="")
    for i in range(0, len(map_game[1])):
        print("{}  ".format(i) if i < 9 else "{} ".format(i), end="")
    print()
