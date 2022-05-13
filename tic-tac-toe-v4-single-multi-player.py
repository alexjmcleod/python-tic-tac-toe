import random
print("\nWelcome to Tic-Tac-Toe\n")

class Player:
    """ Represents a player with tiles and a generic name """

    def __init__(self, name, character):
        """ Creates a new pet with a name and empty set of tiles """
        self._name = name
        self._tiles = []
        self._character = character

    def add_tile(self, tile):
        """ Adds the tile from a players turn to the players list of tiles """
        self._tiles.append(tile)

    def get_tiles(self):
        """ Returns the players current set of tiles """
        return self._tiles

    def clear_tiles(self):
        """ Clears the players tiles at the start of a new game """
        self._tiles = []

# Create players
player_1 = Player("Player 1", "X")
player_2 = Player("Player 2", "O")
computer = Player("Computer", "O")

# Globals
winning_combinations = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[1, 4, 7],
[2, 5, 8],
[3, 6, 9],
[1, 5, 9],
[3, 5, 7]]

current_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

winner = False

# Function definitions
def draw_board():
    """ Draws the current board """
    horizontal_bar = "-" * 19

    row_1 = "|  " + str(current_board[0]) + "  |  " + str(current_board[1]) + "  |  " + str(current_board[2]) + "  |"
    row_2 = "|  " + str(current_board[3]) + "  |  " + str(current_board[4]) + "  |  " + str(current_board[5]) + "  |"
    row_3 = "|  " + str(current_board[6]) + "  |  " + str(current_board[7]) + "  |  " + str(current_board[8]) + "  |"

    print(horizontal_bar)
    print(row_1)
    print(horizontal_bar)
    print(row_2)
    print(horizontal_bar)
    print(row_3)
    print(horizontal_bar)

def is_win(player):
    """ Checks whether a players current tiles match any of the winning combinations """

    player_tiles = player.get_tiles()
    if len(player_tiles) < 3:
        return False # Not a win if the player doesn't have at least 3 tiles
    for combo in winning_combinations:
        if all(tile in player_tiles for tile in combo):

            draw_board()

            # It's a win if the player has all 3 of the tiles from this combo in their tiles
            # Print winning player box
            frame_x = "-----------------------------------------\n"
            frame_y = "|                                       |\n"
            frame_winner = "|            " + player._name + " Wins!             |\n"
            print(frame_x + frame_y + frame_y + frame_winner + frame_y + frame_y + frame_x)

            global winner
            winner = True # To stop while loop in player_turns
            return True # To signal the end of the game has been reached

    if is_draw():
        winner = True # To stop while loop in player_turns
        draw_board()
        frame_x = "-----------------------------------------\n"
        frame_y = "|                                       |\n"
        frame_draw = "|             It's a draw!              |\n"
        print(frame_x + frame_y + frame_y + frame_draw + frame_y + frame_y + frame_x)
        return True # To signal the end of the game has been reached

    return False # Not a win if the player doesn't have any of the winning combos

def player_turn(player):
    """ Starts a turn for the provided player """

    draw_board()

    while True:
        move = input(player._name + ", pick a tile: ")
        code = check_valid_input(move)
        if code == 0:
            break
        elif code == 1:
            print("Please enter a valid integer.")
        elif code == 2:
            print("Please enter an integer 1-9.")
        elif code == 3:
            print("That tile is already taken. Please choose another tile.")

    move = int(move)
    player.add_tile(move) # Add move to the current players tiles
    current_board[move-1] = player._character # Mark the board with the current players character
    print("\n")
    return is_win(player)

def computer_turn(computer):
    """ Starts a turn for the computer in single player games """

    while True:
        move = random.choice(current_board)
        if isinstance(move, int):
            break

    computer.add_tile(move) # Add move to the current players (computer) tiles
    current_board[move-1] = computer._character # Mark the board with the current players (computer) character

    return is_win(computer)


def check_valid_input(move):
    """ Checks that the input from the user is valid """
    if not str.isnumeric(move):
        return 1
    elif not 0 < int(move) < 10:
        return 2
    elif int(move) not in current_board:
        return 3
    else:
        return 0

def is_draw():
    for tile in current_board:
        if type(tile) == int:
            return False
    return True

def run_game():
    """ Starts a game of tic-tac-toe """

    while True:
        game_mode = input('Enter "S" for single player mode or "M" for multiplayer mode: ').upper()
        if game_mode == "S" or game_mode == "M":
            break
        print("Invalid input.")

    print("\nPlayer 1's character: X")
    if game_mode == "S":
        print("Computer's character: O\n")
    elif game_mode == "M":
        print("Player 2's character: O\n")

    while winner == False:
        if player_turn(player_1):
            return new_game()
        else:
            if game_mode == "S": # single player
                if computer_turn(computer):
                    return new_game()
            elif game_mode == "M": # multi player
                if player_turn(player_2):
                    return new_game()

def new_game():
    # At the end of the game, start a new game if the user would like
    new_game = input("New game? (y/n) ")
    while new_game != "y" and new_game != "n":
        new_game = input("New game? (y/n) ")

    if new_game == "y":
        global current_board
        current_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        player_1.clear_tiles()
        player_2.clear_tiles()
        global winner
        winner = False
        print("\n" * 3)
        return run_game()


run_game()