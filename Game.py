import AskInputs
import random


# Function to Init Game
# ask all information for the game, size / number of mines
def InitGame():
    print(""" __        __   _                            _          __  __ _            ____                                   
 \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   |  \/  (_)_ __   ___/ ___|_      _____  ___ _ __   ___ _ __ 
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | |\/| | | '_ \ / _ \___ \ \ /\ / / _ \/ _ \ '_ \ / _ \ '__|
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |  | | | | | |  __/___) \ V  V /  __/  __/ |_) |  __/ |   
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_|  |_|_|_| |_|\___|____/ \_/\_/ \___|\___| .__/ \___|_|   
                                                                                                  |_|              """)
    print(120 * "*")

    width = AskInputs.AskInputInt("Enter field width : ")
    height = AskInputs.AskInputInt("Enter field height : ")
    number_mines = AskInputs.AskInputInt("How many mines ? ")
    return {"width": width, "height": height, "number_mines": number_mines}


# generate all the coord of all mine and generate the map with the width, height
def GenerateGame(value):
    coord_mine = GenerateCoordMine(value)
    map_game = GenerateMap(value, coord_mine)
    return coord_mine, map_game


def GenerateCoordMine(value):
    coordinates = set()
    x, y = random.randint(0, value["width"] - 1), random.randint(0, value["height"] - 1)
    for nbr in range(value["number_mines"]):
        coordinates.add((x, y))
        x, y = random.randint(0, value["width"] - 1), random.randint(0, value["height"] - 1)
    return coordinates


def GenerateMap(value, coord_mine):
    map_game = []
    for map_h in range(value["height"]):
        line = []
        for map_w in range(value["width"]):
            line.append(1)
        map_game.append(line)
    return map_game


def PrintMap(map_game):
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


def TryCoord(map_game, x, y):
    if len(map_game) > y and len(map_game[0]) > x:
        return True
    print("Your coordinate does not exist")
    return False


def CanDoAction(map_game, x, y):
    if map_game[y][x] == 1:
        return True, "Hide"
    elif map_game[y][x] == 2:
        return True, "Flag"
    elif map_game[y][x] == 0:
        return False


def Undercover_Recurs(map_game, x, y, coord_mine):
    if map_game[y][x] != 1:
        return 0
    neighbors = []
    rows = len(map_game)
    cols = len(map_game[0])

    mine_arround = 0
    for i in range(max(0, x - 1), min(rows, x + 2)):
        for j in range(max(0, y - 1), min(cols, y + 2)):
            if (i, j) != (x, y):
                if (i,j) in coord_mine:
                    mine_arround += 1
                map_game[y][x] = 3

    if mine_arround == 0:
        for i in range(max(0, x - 1), min(rows, x + 2)):
            for j in range(max(0, y - 1), min(cols, y + 2)):
                Undercover_Tile(map_game, i,j ,coord_mine)
    map_game[y][x] = 3 + mine_arround
    return neighbors


def Undercover_Tile(map_game, x, y, coord_mine):
    if (x, y) in coord_mine:
        Loose()
    Undercover_Recurs(map_game, x, y, coord_mine)


def action_on_map(map_game, x, y, coord_mine):
    can, option = CanDoAction(map_game, x, y)
    if not can:
        return map_game
    if option == "Hide":
        if AskInputs.AskInputString("Do you want to undercover a tile (type : U) or flag a mine (F) ", "U", "F") == "F":
            map_game[y][x] = 2
        else:
            Undercover_Tile(map_game, x, y, coord_mine)
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


def Game():
    value_game = InitGame()
    coord_mine, map_game = GenerateGame(value_game)
    while True:
        print(coord_mine)
        PrintMap(map_game)
        x = AskInputs.AskInputInt("choose a Coordinate : First the position X → : ")
        y = AskInputs.AskInputInt("position Y ↑ : ")
        if AskInputs.AskInputString("you choose {}-{} ? (Type : Yes or No) ".format(x, y), "Yes", "No") == "Yes":
            if TryCoord(map_game, x, y):
                pass
                action_on_map(map_game, x, y, coord_mine)
        else:
            pass


def Loose():
    print(150 * "/")
    print("""█████ █████                        █████                                         
░░███ ░░███                        ░░███                                          
 ░░███ ███    ██████  █████ ████    ░███         ██████   ██████   █████   ██████ 
  ░░█████    ███░░███░░███ ░███     ░███        ███░░███ ███░░███ ███░░   ███░░███
   ░░███    ░███ ░███ ░███ ░███     ░███       ░███ ░███░███ ░███░░█████ ░███████ 
    ░███    ░███ ░███ ░███ ░███     ░███      █░███ ░███░███ ░███ ░░░░███░███░░░  
    █████   ░░██████  ░░████████    ███████████░░██████ ░░██████  ██████ ░░██████ 
   ░░░░░     ░░░░░░    ░░░░░░░░    ░░░░░░░░░░░  ░░░░░░   ░░░░░░  ░░░░░░   ░░░░░░  
                                                                                  """)
    quit()

def Win():
    print(150 * "/")
    print("""" █████ █████                        █████   ███   █████  ███            
░░███ ░░███                        ░░███   ░███  ░░███  ░░░             
 ░░███ ███    ██████  █████ ████    ░███   ░███   ░███  ████  ████████  
  ░░█████    ███░░███░░███ ░███     ░███   ░███   ░███ ░░███ ░░███░░███ 
   ░░███    ░███ ░███ ░███ ░███     ░░███  █████  ███   ░███  ░███ ░███ 
    ░███    ░███ ░███ ░███ ░███      ░░░█████░█████░    ░███  ░███ ░███ 
    █████   ░░██████  ░░████████       ░░███ ░░███      █████ ████ █████
   ░░░░░     ░░░░░░    ░░░░░░░░         ░░░   ░░░      ░░░░░ ░░░░ ░░░░░ 
                                                                        """)


Game()
