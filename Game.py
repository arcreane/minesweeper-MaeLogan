import AskInputs
import difficulty
import random
import Display
import Generate_Game



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
        Display.lose()
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
    value_game = Generate_Game.init_game()
    coord_mine, map_game = Generate_Game.generate_game(value_game)
    game_finish = True
    while game_finish:
        print(coord_mine)
        Display.print_map(map_game)
        x = AskInputs.AskInputInt("choose a Coordinate : position X → : ")
        y = AskInputs.AskInputInt("choose a Coordinate : position Y ↑ : ")
        if AskInputs.AskInputString("you choose {}-{} ? (Type : Yes or No) ".format(x, y), "Yes", "No") == "Yes":
            if try_coord(map_game, x, y):
                action_on_map(map_game, x, y, coord_mine)
                if is_win(map_game, coord_mine):
                    Display.win()
                    game_finish = False


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

if __name__ == "__main__":
    # Call the main function if the script is run directly
    game()
