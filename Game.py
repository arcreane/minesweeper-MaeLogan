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


def GenerateGame(value):
    coord_mine = GenerateCoordMine(value)
    map_game = GenerateMap(value, coord_mine)
    PrintMap(map_game)


def GenerateCoordMine(value):
    coordinates = set()
    x, y = random.randint(0, value["width"] - 1), random.randint(0, value["height"] - 1)
    for nbr in range(value["number_mines"]):
        coordinates.add((x, y))
        x, y = random.randint(0, value["width"] - 1), random.randint(0, value["height"] - 1)
    return coordinates


def GenerateMap(value, coord_mine):
    map_game = []
    for map_w in range(value["width"]):
        line = []
        for map_h in range(value["height"]):
            if (map_w, map_h) in coord_mine:
                line.append("1")
            else:
                line.append("0")
        map_game.append(line)
    return map_game


def PrintMap(map_game):
    for line in map_game:
        for tile in line:
            print(tile, end="")
        print()


def Game():
    value_game = InitGame()
    GenerateGame(value_game)


Game()
