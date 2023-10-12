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
