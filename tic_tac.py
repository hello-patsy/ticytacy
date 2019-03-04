## babby first py script
def display_board(board):
	print('\n'*100)
	print(board[7]+'|'+board[8]+'|'+board[9])
	print('-|-|-')
	print(board[4]+'|'+board[5]+'|'+board[6])
	print('-|-|-')
	print(board[1]+'|'+board[2]+'|'+board[3])
## did it work?
#test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
#display_board(test_board)
## ask p1 to choose x or o
def player_input():
	marker = ''
	while marker != 'X' and marker != 'O':
		marker = input('Player 1, choose X or O: ').upper()
	if marker == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')
player1_marker , player2_marker = player_input()
## display p1 + p2 to see who is X and who is O
#player1_marker
#player2_marker
def place_marker(board, marker, position):
	board[position] = marker
## test to see if this is working correctly
#place_marker(test_board, '$', 8)
#display_board(test_board)
## define how to win
def win_check(board, mark):
	## row checks for matches
	return((board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    ## column checks for matches
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    ## diagonal checks for matches
    (board[1] == board[5] == board[9] == mark) or
    (board[3] == board[5] == board[7] == mark))
## code check
#win_check(test_board, 'X')
## create a coin toss to determine who goes first
import random
def choose_first():
	flip = random.randint(0,1)
	if flip == 0:
		return 'Player 1'
	else:
		return 'Player 2'
## define when spaces are available
def space_check(board, position):
	return board[position] == ' '
## create a check to see if board is full (=True or if not = False)
def full_board_check(board):
	for i in range(1,10):
		if space_check(board,i):
			return False
	return True
## ask players to enter Xs and Os til board is full
def player_choice(board):
	position = 0
	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
		position = int(input('Choose a position: (1 - 9) '))
	return position
## when game is over, ask players if they'd like to go again
def replay():
	choice = input('Play again? Enter Yes or No').lower()
	return choice == 'Yes'
## build out gameplay and add in the above
print('Welcome to Tic Tac Toe')
while True:
	print('\n'*100)
	the_board = [' ']*10
	player1_marker, player2_marker = player_input()
	turn = choose_first()
	print(turn + ' will go first')
	play_game = input('Ready to play? Enter y or n ')
	if play_game == 'y':
		game_on = True
	else:
		game_on = False
	while game_on:
		if turn == 'Player 1':
			display_board(the_board)
			position = player_choice(the_board)
			place_marker(the_board,player1_marker,position)
			if win_check(the_board,player1_marker):
				display_board(the_board)
				print('Player 1 has won the game.')
				game_on = False
			else:
				if full_board_check(the_board):
					display_board(the_board)
					print('Game is tied; no winner.')
					game_on = False
				else:
					turn = 'Player 2'
		else:
			display_board(the_board)
			position = player_choice(the_board)
			place_marker(the_board,player2_marker,position)
			if win_check(the_board,player2_marker):
				display_board(the_board)
				print('Player 2 has won the game.')
				game_on = False
			else:
				if full_board_check(the_board):
					display_board(the_board)
					print('Game is tied; no winner.')
					game_on = False
				else:
					turn = 'Player 1'
	if not replay():
		break
