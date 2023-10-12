
def lose():
    """
       Print a message indicating the player has lost the Minesweeper game.
    """

    print("\n\n")
    print(""" ___ ___                    __                      
|   |   |.-----..--.--.    |  |.-----..-----..-----.
 \     / |  _  ||  |  |    |  ||  _  ||__ --||  -__|
  |___|  |_____||_____|    |__||_____||_____||_____|
                                                    """)


def win():
    """
          Print a message indicating the player has won the Minesweeper game.
       """
    print("\n\n")
    print(""" ___ ___                    ________  __        
|   |   |.-----..--.--.    |  |  |  ||__|.-----.
 \     / |  _  ||  |  |    |  |  |  ||  ||     |
  |___|  |_____||_____|    |________||__||__|__|


""")

def print_map(map_game):
    """
       Print the Minesweeper game map to the console.

       This function displays the game map provided as input. Each tile on the map is represented
       by an integer, and the function prints stylized symbols representing different tile states:
       - Hidden tile: ⬛
       - Flagged tile: ⚑
       - Revealed tile: ⬜
       - Numbered tile (indicating adjacent mines): 1, 2, 3, ...

       Parameters:
       - map_game (list of lists): The game map where each tile is represented by an integer.

       Example Usage:
       - game_map = [[1, 2, 3], [3, 2, 1], [2, 1, 1]]
       - print_map(game_map)  # Example usage to print the Minesweeper game map.
       """
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

