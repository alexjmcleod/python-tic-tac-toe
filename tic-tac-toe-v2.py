print("\nWelcome to Tic-Tac-Toe")

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

# Create players
player_1 = Player("Player 1", "X")
player_2 = Player("Player 2", "O")

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
    if len(player._tiles) < 3:
        return False # Not a win if the player doesn't have at least 3 tiles
    for combo in winning_combinations:
        for tile in combo:
            if tile not in player._tiles:
                return False # Not a win if the player doesn't have all 3 of the tiles in this combo

        # It's a win if the player has all 3 of the tiles from this combo in their tiles
        # Print winning player box
        frame_x = "-----------------------------------------\n"
        frame_y = "|                                       |\n"
        frame_winner = "|            " + player._name + " Wins!             |\n"
        print(frame_x + frame_y + frame_y + frame_winner + frame_y + frame_y + frame_x)

        global winner
        winner = True # To stop while loop in player_turns
        return True

    return False # Not a win if the player doesn't have any of the winning combos

def player_turn(player):
    """ Starts a turn for the provided player """
    draw_board()
    move = int(input(player._name + ", pick a tile: "))
    if move not in current_board:
        print("Please choose a valid tile.")
        move = int(input(player._name + ", pick a tile: "))
    player._tiles.append(move) # Add move to the current players tiles
    current_board[move-1] = player._character # Mark the board with the current players character
    print("\n")
    return is_win(player)


def run_game():
    """ Starts a game of tic-tac-toe """
    print("\nPlayer 1's character: X")
    print("Player 2's character: O\n")
    while winner == False:
        if player_turn(player_1):
            return None
        else:
            if player_turn(player_2):
                return None

run_game()

# At the end of the game, start a new game if the user would like
new_game = input("New game? (y/n) ")
while new_game != "y" and new_game != "n":
    new_game = input("New game? (y/n) ")

if new_game == "y":
    current_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player_1._tiles = []
    player_2._tiles = []
    new_game = ""
    winner = False
    print("\n" * 3)
    run_game()