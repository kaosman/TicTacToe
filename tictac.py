# Write a program to graphically implement a tic tac toe program

# 1.) We need to print a 3 x 3 board on screen. We need a function that will print a board
# 2.) Take player input and store it in a list called board. When player inputs a position on board where he wants to place his marker it will correspond to a value in the list

def print_board(*board):
	'''
	#Input: list of player markers
	#Output: Printed board
	'''
	
	print "   |   |   "
	print " "+board[1]+" | "+board[2]+" | "+board[3]+"  "
	print "   |   |   "
	print "-----------"
	print "   |   |   "
	print " "+board[4]+" | "+board[5]+" | "+board[6]+"  "
	print "   |   |   "
	print "-----------"
	print "   |   |   "
	print " "+board[7]+" | "+board[8]+" | "+board[9]+"  "
	print "   |   |   "

def chooseMarker():
	#Allow Player 1 to select marker
	while True:
		p1_marker = raw_input("Player 1 choose your marker x or o : ")
		if (p1_marker not in ['x', 'X', 'o', 'O']):
			print "Invalid input, select marker again \n"
		else:
			if (p1_marker not in ['x', 'X']):
				print "Player 1 is assigned o \n"
				print "Player 2 is assigned x \n"
				p2_marker = 'x'
				break
			else:
				print "Player 1 is assigned x \n"
				print "Player 2 is assigned o \n"
				p2_marker = 'o'
				break
	return [p1_marker,p2_marker]

def winConditions(player_marker,*board):
	# In tic tac toe, a player wins when three of their markers line up horizontally, vertically or diagonally.
	# In this case we have the markers stored in a list called board
	
	# Horizontal conditions
	if (board[1] == board[2] == board[3] == player_marker or board[4] == board[5] == board[6] == player_marker or board[7] == board[8] == board[9] == player_marker):
		result = "Win"
	elif (board[1] == board[4] == board[7] == player_marker or board[2] == board[5] == board[8] == player_marker or board[3] == board[6] == board[9] == player_marker): #Vertical conditions
		result = "Win"
	elif (board[1] == board[5] == board[9] == player_marker or board[3] == board[5] == board[7] == player_marker): #Diagonal conditions
		result = "Win"
	else:
		result = "Draw"
	return result

def game():

	board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
	print "Welcome to the game of Tic Tac Toe \n"
	print "Player 1 goes first \n"
	current_player_flag = "p1"
	marker_counter = 0
	
	markers = chooseMarker()
	print "Here are the markers \n"
	print "Player 1: %s \n" %(markers[0])
	print "Player 2: %s \n" %(markers[1])
	
	while (marker_counter<=9): #We need to let the loop run until a winning condition or stale mate is achieved. We need to alternate between players.	
		if (current_player_flag == "p1"):
			print_board(*board)
			p1_input = input("Player 1, enter a position between 1 and 9 to place your marker: ")
			board[p1_input]=markers[0]
			marker_counter = marker_counter + 1
			if (winConditions(markers[0],*board) == "Win"):
				print_board(*board)
				print "Player 1 wins \n"
				break
			else:
				current_player_flag = "p2"
		else:
			print_board(*board)
			p2_input = input("Player 2, enter a position between 1 and 9 to place your marker: ")
			marker_counter = marker_counter + 1
			board[p2_input]=markers[1]
			if (winConditions(markers[1],*board) == "Win"):
				print_board(*board)
				print "Player 2 wins \n"
				break
			else:
				current_player_flag = "p1"
	if (marker_counter>9):
		print_board(*board)
		print "The game is a draw!!!"
		
game ()
