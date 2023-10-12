import AskInputs
import difficulty
import random

# Function to Init game
# ask all information for the game, size / number of mines
def init_game():
    print(""" __        __   _                            _          __  __ _            ____                                   
 \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   |  \/  (_)_ __   ___/ ___|_      _____  ___ _ __   ___ _ __ 
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | |\/| | | '_ \ / _ \___ \ \ /\ / / _ \/ _ \ '_ \ / _ \ '__|
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |  | | | | | |  __/___) \ V  V /  __/  __/ |_) |  __/ |   
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_|  |_|_|_| |_|\___|____/ \_/\_/ \___|\___| .__/ \___|_|   
                                                                                                  |_|              """)
    print(120 * "*")

    input_difficulty = AskInputs.AskInputString("Choose a difficulty : \n\t -Easy \n\t -Medium \n\t -Hard \n\t -Custom", "Easy", "Medium", "Hard", "Custom")

    if(input_difficulty == "Easy"):
        width, height, number_mines = difficulty.initEasy()
    elif(input_difficulty == "Medium"):
        width, height, number_mines = difficulty.initMedium()
    elif(input_difficulty == "Hard"):
        width, height, number_mines = difficulty.initHard()
    else:
        width = AskInputs.AskInputInt("Enter field width : ")
        height = AskInputs.AskInputInt("Enter field height : ")
        number_mines = AskInputs.AskInputInt("How many mines ? ")
    return {"width": width, "height": height, "number_mines": number_mines}


# generate all the coord of all mine and generate the map with the width, height
def generate_game(value):
    coord_mine = generate_coord_mine(value)
    map_game = generate_map(value, coord_mine)
    return coord_mine, map_game


def generate_coord_mine(value):
    coordinates = set()
    x, y = random.randint(0, value["width"] - 1), random.randint(0, value["height"] - 1)
    for nbr in range(value["number_mines"]):
        coordinates.add((x, y))
        x, y = random.randint(0, value["width"] - 1), random.randint(0, value["height"] - 1)
    return coordinates


def generate_map(value, coord_mine):
    map_game = []
    for map_h in range(value["height"]):
        line = []
        for map_w in range(value["width"]):
            line.append(1)
        map_game.append(line)
    return map_game


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


def get_tile(map_game, x, y):
    return map_game[y][x]


def try_coord(map_game, x, y):
    if len(map_game) > y and len(map_game[0]) > x:
        return True
    print("Your coordinate does not exist")
    return False


def can_do_action(map_game, x, y):

    if map_game[y][x] == 1:
        return True, "Hide"
    elif map_game[y][x] == 2:
        return True, "Flag"
    elif map_game[y][x] == 0:
        return False,"0"
    else :
        return False,"0"


def how_many_mine(map_game,x,y, coord_mine):
    mine_arround = 0
    rows = len(map_game)
    cols = len(map_game[0])
    for i in range(max(0, x - 1), min(rows, x + 2)):
        for j in range(max(0, y - 1), min(cols, y + 2)):
            if (i, j) != (x, y):
                if (i, j) in coord_mine:
                    mine_arround += 1
                map_game[y][x] = 3
    return mine_arround

def undercover_recurs(map_game, x, y, coord_mine):
    if map_game[y][x] != 1:
        "test"
        return "test"
    mine_arround = how_many_mine(map_game,x,y,coord_mine)
    rows = len(map_game)
    cols = len(map_game[0])
    if mine_arround == 0:
        for i in range(max(0, x - 1), min(rows, x + 2)):
            for j in range(max(0, y - 1), min(cols, y + 2)):
                undercover_tile(map_game, i, j, coord_mine)
    map_game[y][x] = 3 + mine_arround


def undercover_tile(map_game, x, y, coord_mine):
    if (x, y) in coord_mine:
        loose()
    undercover_recurs(map_game, x, y, coord_mine)


def action_on_map(map_game, x, y, coord_mine):
    can, option = can_do_action(map_game, x, y)
    if not can:
        print("Already play on this tile", '\n')
        return map_game
    if option == "Hide":
        if AskInputs.AskInputString("Do you want to undercover a tile (type : U) or flag a mine (F) ", "U", "F") == "F":
            map_game[y][x] = 2
        else:
            undercover_tile(map_game, x, y, coord_mine)
        return map_game
    elif option == "Flag":
        if AskInputs.AskInputString("Its a flag tile, do you want to unflagged it : Type Yes or No", "Yes",
                                    "No") == "Yes":
            map_game[y][x] = 1
            if AskInputs.AskInputString("Do you want to undercover it: Type Yes or No", "Yes", "No") == "Yes":
                pass
    else:
        print("erreur")
        return map_game


def game():
    value_game = init_game()
    coord_mine, map_game = generate_game(value_game)
    game_finish = True
    while game_finish:
        print(coord_mine)
        print_map(map_game)
        x = AskInputs.AskInputInt("choose a Coordinate : position X → : ")
        y = AskInputs.AskInputInt("choose a Coordinate : position Y ↑ : ")
        if AskInputs.AskInputString("you choose {}-{} ? (Type : Yes or No) ".format(x, y), "Yes", "No") == "Yes":
            if try_coord(map_game, x, y):
                # pass
                action_on_map(map_game, x, y, coord_mine)
                if is_win(map_game, coord_mine):
                    win()
                    game_finish = False
        else:
            pass


def is_win(map_game, coord_mine):
    count_mine = len(coord_mine)
    count_tile = 0
    for row in map_game:
        for char in row:
            if char == 1 or char == 2:
                count_tile += 1

    if count_tile == count_mine:
        return True
    else:
        return False


def loose():
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


game()
