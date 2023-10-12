import AskInputs
import difficulty
import random

# Function to Init game
# ask all information for the game, size / number of mines
def init_game():
    """
       Initialize a Minesweeper game by gathering information about the game size and number of mines.

       This function prompts the user to choose a difficulty level (Easy, Medium, Hard, or Custom) and
       collects information about the game size and the number of mines based on the selected difficulty.
       If the Custom option is chosen, the user is prompted for custom field width, height, and number of mines.

       Returns:
       dict: A dictionary containing game information including width, height, and number of mines.

       Example Usage:
       - game_info = init_game()  # Example initialization of a Minesweeper game.
       - width = game_info["width"]
       - height = game_info["height"]
       - number_mines = game_info["number_mines"]
       """
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
    """
        Generate a Minesweeper game based on the provided game information.

        This function generates the coordinates of mines and creates the initial game map
        using the given game information (field size and number of mines).

        Parameters:
        - value (dict): A dictionary containing game information including width, height, and number of mines.

        Returns:
        tuple: A tuple containing two elements:
            1. coord_mine (list of tuples): A list of tuples representing the coordinates of all mines in the game.
            2. map_game (list of lists): The initial game map where each tile is represented by an integer.

        Example Usage:
        - game_info = {"width": 8, "height": 8, "number_mines": 10}
        - coord_mine, map_game = generate_game(game_info)  # Example generation of a Minesweeper game.
        """
    coord_mine = generate_coord_mine(value)
    map_game = generate_map(value)
    return coord_mine, map_game


def generate_coord_mine(value):
    """
        Generate random coordinates for mines based on the provided game information.

        This function generates a set of unique coordinates representing the positions of mines
        within the game field. Mines are randomly placed within the specified width and height
        according to the given number of mines.

        Parameters:
        - value (dict): A dictionary containing game information including width, height, and number of mines.

        Returns:
        set: A set of tuples representing unique coordinates of mines within the game field.

        Example Usage:
        - game_info = {"width": 8, "height": 8, "number_mines": 10}
        - mine_coordinates = generate_coord_mine(game_info)  # Example generation of mine coordinates.
        """
    coordinates = set()
    x, y = random.randint(0, value["width"] - 1), random.randint(0, value["height"] - 1)
    for nbr in range(value["number_mines"]):
        coordinates.add((x, y))
        x, y = random.randint(0, value["width"] - 1), random.randint(0, value["height"] - 1)
    return coordinates


def generate_map(value):
    """
    Generate an initial game map with hidden tiles based on the provided game information.

    This function creates a two-dimensional list representing the initial game map
    with all tiles initially hidden (represented by the integer 1). The dimensions of
    the map are determined by the width and height values provided in the game information.

    Parameters:
    - value (dict): A dictionary containing game information including width, height, and number of mines.

    Returns:
    list of lists: The initial game map where each tile is represented by an integer (1 for hidden tiles).

    Example Usage:
    - game_info = {"width": 8, "height": 8, "number_mines": 10}
    - initial_map = generate_map(game_info)  # Example generation of the initial game map.
    """
    map_game = []
    for map_h in range(value["height"]):
        line = []
        for map_w in range(value["width"]):
            line.append(1)
        map_game.append(line)
    return map_game
