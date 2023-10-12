import time
import AskInputs
import Display
import Generate_Game


# return information of a tile
def get_tile(map_game, x, y):
    return map_game[y][x]


# test a coord to try if is out of bound
def try_coord(map_game, x, y):
    if len(map_game) > y and len(map_game[0]) > x:
        return True
    print("Your coordinate does not exist")
    return False


# test the tile if we can do action on it
def can_do_action(map_game, x, y):
    if map_game[y][x] == 1:
        return True, "Hide"
    elif map_game[y][x] == 2:
        return True, "Flag"
    elif map_game[y][x] == 0:
        return False, "0"
    else:
        return False, "0"


# count how many mines around a tile
def how_many_mine(map_game, x, y, coord_mine):
    mine_around = 0
    rows = len(map_game)
    cols = len(map_game[0])
    for i in range(max(0, x - 1), min(rows, x + 2)):
        for j in range(max(0, y - 1), min(cols, y + 2)):
            if (i, j) != (x, y):
                if (i, j) in coord_mine:
                    mine_around += 1
                map_game[y][x] = 3
    return mine_around


# call in recursive each tile to test if mine around
def undercover_recurs(map_game, x, y, coord_mine):
    if map_game[y][x] != 1:
        return 0
    mine_around = how_many_mine(map_game, x, y, coord_mine)
    rows = len(map_game)
    cols = len(map_game[0])
    if mine_around == 0:
        for i in range(max(0, x - 1), min(rows, x + 2)):
            for j in range(max(0, y - 1), min(cols, y + 2)):
                undercover_tile(map_game, i, j, coord_mine)
    map_game[y][x] = 3 + mine_around


# test it's a mine if not call recursive
def undercover_tile(map_game, x, y, coord_mine):
    if (x, y) in coord_mine:
        Display.lose()
        return -1
    undercover_recurs(map_game, x, y, coord_mine)


#
def action_on_map(map_game, x, y, coord_mine):
    """
       Perform an action on the game map at the specified coordinates (x, y).

       This function checks if the specified tile at (x, y) can be interacted with and
       carries out the appropriate action based on the tile's status (Hide, Flag, or error).

       Parameters:
       - map_game (list of lists): The game map where each tile is represented by an integer.
       - x (int): The x-coordinate (column) of the tile to interact with.
       - y (int): The y-coordinate (row) of the tile to interact with.
       - coord_mine (list of tuples): A list of tuples representing the coordinates of all mines in the game.

       Returns:
       - map_game (list of lists): The updated game map after performing the specified action.
       - -1 (int): Returns -1 if an error occurs during tile interaction, such as selecting a mine.

       Action Types:
       - 'Hide': Uncover or flag a tile.
       - 'Flag': Unflag a previously flagged tile or choose to uncover it.
       """
    can, option = can_do_action(map_game, x, y)
    if not can:
        print("Already play on this tile", '\n')
        return map_game
    if option == "Hide":
        if AskInputs.AskInputString("Do you want to undercover a tile (type : U) or flag a mine (F) ", "U", "F") == "F":
            map_game[y][x] = 2
        else:
            if undercover_tile(map_game, x, y, coord_mine) == -1:
                return -1
        return map_game
    elif option == "Flag":
        if AskInputs.AskInputString("Its a flag tile, do you want to unflagged it : Type Yes or No", "Yes",
                                    "No") == "Yes":
            map_game[y][x] = 1
            if AskInputs.AskInputString("Do you want to undercover it: Type Yes or No", "Yes", "No") == "Yes":
                if undercover_tile(map_game, x, y, coord_mine) == -1:
                    return -1
    else:
        print("error")
        return map_game


def print_time(start_t):
    """
        Calculate and print the elapsed time from the specified start time.

        This function calculates the elapsed time in minutes and seconds from the
        provided start time and prints a formatted string indicating the time taken.

        Parameters:
        - start_t (float): The start time in seconds since the epoch (usually obtained using time.time()).

        Example Usage:
        - start_time = time.time()
        - # Perform some time-consuming operation
        - print_time(start_time)  # Output: "You take 2:30 minutes" (example output)

        Note:
        - The function uses the time module to calculate the elapsed time.
        """
    end = time.time()
    elapsed_time = end - start_t
    minute, second = divmod(elapsed_time, 60)
    print(f"You take {minute:.0f}:{second:.0f} minutes")


def game():
    """Start and play a game of Minesweeper.

    This function initiates and plays a game of Minesweeper, interacting with the user
    to reveal tiles, flag mines, and determine the game's outcome.

    The game continues until the user either uncovers all safe tiles or uncovers a mine.

    Example Usage:
    - game()  # Start and play a game of Minesweeper interactively.

    Note:
    - The game is played by printing the game map, prompting the user for coordinates,
      and calling functions like `try_coord`, `action_on_map`, and `is_win` to
      manage the game state.
    - The game's duration is measured using the `print_time` function, and the outcome
      is displayed to the user using `Display.win()` when the game is won.
    """

    value_game = Generate_Game.init_game()
    coord_mine, map_game = Generate_Game.generate_game(value_game)
    game_finish = True
    start_t = time.time()
    while game_finish:
        print(coord_mine)
        Display.print_map(map_game)
        x = AskInputs.AskInputInt("choose a Coordinate : position X → : ")
        y = AskInputs.AskInputInt("choose a Coordinate : position Y ↑ : ")
        if AskInputs.AskInputString("you choose {}-{} ? (Type : Yes or No) ".format(x, y), "Yes", "No") == "Yes":
            if try_coord(map_game, x, y):
                if action_on_map(map_game, x, y, coord_mine) == -1:
                    game_finish = False
                if is_win(map_game, coord_mine):
                    Display.win()

                    game_finish = False

    print_time(start_t)


def is_win(map_game, coord_mine):
    """
        Check if the game has been won by the player.

        This function compares the number of uncovered and flagged tiles in the game map
        with the total number of mines to determine if the player has won the game.

        Parameters:
        - map_game (list of lists): The game map where each tile is represented by an integer.
        - coord_mine (list of tuples): A list of tuples representing the coordinates of all mines in the game.

        Returns:
        - bool: True if all mines are flagged and all other tiles are uncovered, indicating a win.
                False otherwise, indicating the game is still ongoing.

        Example Usage:
        - is_win(game_map, [(1, 1), (2, 3), (4, 4)])  # Example check for a win condition.
        """
    count_mine = len(coord_mine)
    count_tile = 0
    for row in map_game:
        for char in row:
            if char == 1 or char == 2:
                count_tile += 1
    if count_tile == count_mine:
        Display.print_map(map_game)
        return True
    else:
        return False


def restart():
    while True:
        string_input = AskInputs.AskInputString("Do you want to restart : (type 'Yes' or 'No')", "Yes", "No")
        if string_input == "Yes":
            game()
        else:
            quit()


if __name__ == "__main__":
    # Call the main function if the script is run directly
    game()
    restart()
