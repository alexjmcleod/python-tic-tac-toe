print("\nWelcome to Tic-Tac-Toe\n")

available_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
used_spaces = []
valid_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

winning_combinations = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[1, 4, 7],
[2, 5, 8],
[3, 6, 9],
[1, 5, 9],
[3, 5, 7]]


player_1 = []
player_2 = []
winner = False
winning_player = ""

# Logic to check if player wins after each turn

def check_spaces(winning_combo, players_spaces):
	""" A helper function for is_win. This tests to see if each space in a particular winning_combo is present in the player's spaces. Returns False if any of the spaces are not present and True if they all are, signaling a winning set """
	for space in winning_combo:
		if space not in players_spaces:
			return False
	return True


def is_win(spaces):
	""" Tests whether the provided spaces can be combined to match one of the winning space combinations in winning_combinations """

	if len(spaces) < 3:
		return False
	for winning_combo in winning_combinations:
		global winner
		winner = check_spaces(winning_combo, spaces)	
		if winner == True:
			return spaces
	return False

def player_turns(player):
	""" Gets players choices for a tile and tests whether that choice creates a winning set """

	if player == "player_1":
		player_name = "Player 1"
	else:
		player_name = "Player 2"

	move = int(input(player_name + ", pick a tile: "))
	while move in used_spaces:
		print("That tile has already been claimed. Please choose another tile.")
		move = int(input(player_name + ", pick a tile: "))
	while move not in valid_moves:
		print("That is not a valid tile. Please choose another tile.")
		move = int(input(player_name + ", pick a tile: "))
	used_spaces.append(move)



	if player == "player_1":
		player_1.append(move)
		available_spaces[move-1] = "X" # Replace the space number with the players character	
		if is_win(player_1): # passing in player_1 list of tiles
			return True
		
	else:
		player_2.append(move) 
		available_spaces[move-1] = "O" # Replace the space number with the players character	
		if is_win(player_2): # passing in player_2 list of tiles
			return True
		

	




def draw_board(available_spaces):
	horizontal_bar = "-------------------"

	row_1 = "|  " + str(available_spaces[0]) + "  |  " + str(available_spaces[1]) + "  |  " +  str(available_spaces[2]) + "  |"
	row_2 = "|  " + str(available_spaces[3]) + "  |  " + str(available_spaces[4]) + "  |  " +  str(available_spaces[5]) + "  |"
	row_3 = "|  " + str(available_spaces[6]) + "  |  " + str(available_spaces[7]) + "  |  " +  str(available_spaces[8]) + "  |"


	print(horizontal_bar)
	print(row_1)
	print(horizontal_bar)
	print(row_2)
	print(horizontal_bar)
	print(row_3)
	print(horizontal_bar)

def celebrate_winner(winning_player):
	""" Prints a box with the winner's name inside """
	frame_x = "-----------------------------------------\n"
	frame_y = "|                                       |\n"
	frame_winner = "|            " + winning_player + "             |\n"
	return "\n" + frame_x + frame_y + frame_y + frame_winner + frame_y + frame_y + frame_x


def start_game():
	""" Starts a new game """
	print("Player 1 character: X")
	print("Player 2 character: O")
	while winner == False:
		print("\n")
		draw_board(available_spaces)
		if player_turns("player_1"):
			draw_board(available_spaces)
			return print(celebrate_winner("Player 1 Wins!"))
		if winner == False:
			print("\n")
			draw_board(available_spaces)
			if player_turns("player_2"):
				print(celebrate_winner("Player 2 Wins!"))
				draw_board(available_spaces)		
				return None	
				
	

start_game()

new_game = ""
while new_game != "y" and new_game != "n":
	new_game = input("New game? (y/n) ")


if new_game == "y":
	available_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	used_spaces = []
	player_1 = []
	player_2 = []
	new_game = ""
	winner = False
	print("\n" * 3)
	start_game()
