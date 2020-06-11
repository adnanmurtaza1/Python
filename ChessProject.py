"test to see if it works"
def give_all_locations(index, piece, board, allLoc): # gets all locations based on the piece at an index on the board
    if piece == "p":
        return locations_for_p(index, board)
    elif piece == "P":
        return locations_for_P(index, board)
    elif piece == "n":
        return locations_for_Knight(index, board, False)
    elif piece == "N":
        return locations_for_Knight(index, board, True)
    elif piece == "r":
        return locations_for_Rook(index, board, False)
    elif piece == "R":
        return locations_for_Rook(index, board, True)
    elif piece == "b":
        return locations_for_Bishop(index, board, False)
    elif piece == "B":
        return locations_for_Bishop(index, board, True)
    elif piece == "q":
        return locations_for_Queen(index, board, False)
    elif piece == "Q":
        return locations_for_Queen(index, board, True)
    elif piece == "k":
        return locations_for_k(index, board, allLoc)
    else:
        return locations_for_K(index, board, allLoc)


def isCapturable(piece, white): # Based on the turn checks if the piece is capturable
    if white == True:
        if piece in "rnbqp":
            return True
    else:
        if piece in "RNBQP":
            return True
    return False


def index_to_list(index): # makes a list of the row and column based on the index
    list = []
    row = int(index)//8 + 1
    col = int(index)%8 + 1
    list.append(row)
    list.append(col)
    return list

def rc_to_index(row, col): # returns the index on the board based on the row and col
    return (int(row) - 1) * 8 + (int(col) - 1)

def locations_for_p(index, board): # all possible locations for a black pawn
    locations = []
    col = index%8 + 1

    if index + 7 < 63 and col != 1 and isCapturable(board[index + 7], False): # if the space in bottom left of the black pawn can be captured
        locations.append(index_to_list(index + 7))

    if index + 9 < 63 and col != 8 and isCapturable(board[index + 9], False): # if the space in bottom right of the black pawn can be captured
        locations.append(index_to_list(index + 9))

    if index + 8 < 63 and board[index + 8] == "*": # if the space in front of the black pawn is open
        locations.append(index_to_list(index + 8))

    if index + 16 < 64 and index//8 == 1 and board[index + 8] == "*" and board[index + 16] == "*": #if the 2nd space in front of the black pawn is open and it is in the starting row
        locations.append(index_to_list(index + 16))

    return locations

def locations_for_P(index, board): # all possible locations for a white pawn
    locations = []
    col = index % 8 + 1

    if index - 7 > -1 and col != 8 and isCapturable(board[index - 7], True):  # if the space in front right of the white pawn can be captured
        locations.append(index_to_list(index - 7))

    if index - 9 > -1 and col != 1 and isCapturable(board[index - 9], True):  # if the space in front left of the white pawn can be captured
        locations.append(index_to_list(index - 9))

    if index - 8 > -1 and board[index - 8] == "*":  # if the space in front of the white pawn is open
        locations.append(index_to_list(index - 8))

    if index - 16 > -1 and index // 8 == 6 and board[index - 8] == "*" and board[index - 16] == "*":  # if the 2nd space in front of the white pawn is open and it is in the starting row
        locations.append(index_to_list(index - 16))

    return locations

def locations_for_Knight(index, board, turn): # Knight
    locations = []
    column = index%8 + 1 # due to column restrictions because the knight can't leave the board
    if index + 17 < 64 and (board[index + 17] == "*" or isCapturable(board[index + 17], turn)) and column != 8:  # tall bottom right
        locations.append(index_to_list(index + 17))
    if index + 15 < 64 and (board[index + 15] == "*" or isCapturable(board[index + 15], turn)) and column != 1:  # tall bottom left
        locations.append(index_to_list(index + 15))
    if index + 10 < 64 and (board[index + 10] == "*" or isCapturable(board[index + 10], turn)) and column != 7 and column != 8:  # short bottom right
        locations.append(index_to_list(index + 10))
    if index + 6 < 64 and (board[index + 6] == "*" or isCapturable(board[index + 6], turn)) and column != 1 and column != 2:  # short bottom left
        locations.append(index_to_list(index + 6))
    if index - 17 > -1 and (board[index - 17] == "*" or isCapturable(board[index - 17], turn)) and column != 1:  # tall top left
        locations.append(index_to_list(index - 17))
    if index - 15 > -1 and (board[index - 15] == "*" or isCapturable(board[index - 15], turn)) and column != 8:  # tall top right
        locations.append(index_to_list(index - 15))
    if index - 10 > -1 and (board[index - 10] == "*" or isCapturable(board[index - 10], turn)) and column != 1 and column != 2:  # short top left
        locations.append(index_to_list(index - 10))
    if index - 6 > -1 and (board[index - 6] == "*" or isCapturable(board[index - 6], turn)) and column != 7 and column != 8:  # short top right
        locations.append(index_to_list(index - 6))

    return locations


def locations_for_Rook(index, board, turn): # Rook
    locations = []
    temp = index - 8
    while temp > -1 and board[temp] == "*": # gets all the rook moves vertically above
        locations.append(index_to_list(temp))
        temp = temp - 8

    if temp > -1 and isCapturable(board[temp], turn): # if the while loop for vertically above got stopped by a piece
        locations.append(index_to_list(temp))

    temp = index + 8
    while temp < 64 and board[temp] == "*": # gets all the rook moves vertically below
        locations.append(index_to_list(temp))
        temp = temp + 8

    if temp < 64 and isCapturable(board[temp], turn): # if the while loop for vertically below got stopped by a piece
        locations.append(index_to_list(temp))

    temp = index + 1
    row = index//8
    if temp//8 == row: # makes sure the temp didn't just go to the next row because of the rook being on column 8
        while temp//8 == row and board[temp] == "*" and temp < 64: # gets all the rook moves to the right
            locations.append(index_to_list(temp))
            temp = temp + 1

    if temp//8 == row and temp < 64 and isCapturable(board[temp], turn): # if the while loop for to the right got stopped by a piece
        locations.append(index_to_list(temp))

    temp = index - 1
    row = index // 8
    if temp // 8 == row:  # makes sure the temp didn't just go to the previous row because of the rook being on column 1
        while temp // 8 == row and board[temp] == "*" and temp > -1: # gets all the rook moves to the left
            locations.append(index_to_list(temp))
            temp = temp - 1

    if temp // 8 == row and temp > -1 and isCapturable(board[temp], turn): # if the while loop for to the left got stopped by a piece
        locations.append(index_to_list(temp))

    return locations


def locations_for_Bishop(index, board, turn): #Bishop
    locations = []
    col = index%8 + 1
    tempcol = col #holds the temporary value of the column

    tempcol = col + 1
    tempind = index - 7
    while tempcol < 9 and tempind > -1 and board[tempind] == "*": #top right
        locations.append(index_to_list(tempind))
        tempind = tempind - 7
        tempcol = tempcol + 1
    if tempcol < 9 and tempind > -1 and isCapturable(board[tempind], turn): # blocked by piece
        locations.append(index_to_list(tempind))

    tempcol = col + 1
    tempind = index + 9
    while tempcol < 9 and tempind < 64 and board[tempind] == "*": #bottom right
        locations.append(index_to_list(tempind))
        tempind = tempind + 9
        tempcol = tempcol + 1
    if tempcol < 9 and tempind < 64 and isCapturable(board[tempind], turn): # blocked by piece
        locations.append(index_to_list(tempind))

    tempcol = col - 1
    tempind = index - 9
    while tempcol > 0 and tempind > -1 and board[tempind] == "*": # top left
        locations.append(index_to_list(tempind))
        tempind = tempind - 9
        tempcol = tempcol - 1
    if tempcol > 0 and tempind > -1 and isCapturable(board[tempind], turn): # blocked by piece
        locations.append(index_to_list(tempind))

    tempcol = col - 1
    tempind = index + 7
    while tempcol > 0 and tempind < 64 and board[tempind] == "*": # bottom left
        locations.append(index_to_list(tempind))
        tempind = tempind + 7
        tempcol = tempcol - 1
    if tempcol > 0 and tempind < 64 and isCapturable(board[tempind], turn): # blocked by piece
        locations.append(index_to_list(tempind))

    return locations


def locations_for_Queen(index, board, turn): # returns all possible locations of a queen based on the color(turn)
    locations = []
    temp = index - 8
    while temp > -1 and board[temp] == "*": # gets all the Queen moves vertically above
        locations.append(index_to_list(temp))
        temp = temp - 8
    if temp > -1 and isCapturable(board[temp], turn): # if the while loop for vertically above got stopped by a piece
        locations.append(index_to_list(temp))

    temp = index + 8
    while temp < 64 and board[temp] == "*": # gets all the Queen moves vertically below
        locations.append(index_to_list(temp))
        temp = temp + 8
    if temp < 64 and isCapturable(board[temp], turn): # if the while loop for vertically below got stopped by a piece
        locations.append(index_to_list(temp))

    temp = index + 1
    row = index//8
    if temp//8 == row: # makes sure the temp didn't just go to the next row because of the Queen being on column 8 # gets all the Queen moves to the right
        while temp//8 == row and board[temp] == "*":
            locations.append(index_to_list(temp))
            temp = temp + 1
    if temp//8 == row and temp < 64 and isCapturable(board[temp], turn): # if the while loop for to the right got stopped by a piece
        locations.append(index_to_list(temp))

    temp = index - 1
    row = index // 8
    if temp // 8 == row:  # makes sure the temp didn't just go to the previous row because of the rook being on column 1
        while temp // 8 == row and board[temp] == "*":
            locations.append(index_to_list(temp))
            temp = temp - 1
    if temp // 8 == row and temp > -1 and isCapturable(board[temp], turn): # if the while loop for to the left got stopped by a piece
        locations.append(index_to_list(temp))


    col = index % 8 + 1
    tempcol = col  # holds the temporary value of the column

    tempcol = col + 1
    tempind = index - 7
    while tempcol < 9 and tempind > -1 and board[tempind] == "*":  # top right
        locations.append(index_to_list(tempind))
        tempind = tempind - 7
        tempcol = tempcol + 1
    if tempcol < 9 and tempind > -1 and isCapturable(board[tempind], turn): # blocked by piece
        locations.append(index_to_list(tempind))

    tempcol = col + 1
    tempind = index + 9
    while tempcol < 9 and tempind < 64 and board[tempind] == "*":  # bottom right
        locations.append(index_to_list(tempind))
        tempind = tempind + 9
        tempcol = tempcol + 1
    if tempcol < 9 and tempind < 64 and isCapturable(board[tempind], turn): # blocked by piece
        locations.append(index_to_list(tempind))

    tempcol = col - 1
    tempind = index - 9
    while tempcol > 0 and tempind > -1 and board[tempind] == "*":  # top left
        locations.append(index_to_list(tempind))
        tempind = tempind - 9
        tempcol = tempcol - 1
    if tempcol > 0 and tempind > -1 and isCapturable(board[tempind], turn): # blocked by piece
        locations.append(index_to_list(tempind))

    tempcol = col - 1
    tempind = index + 7
    while tempcol > 0 and tempind < 64 and board[tempind] == "*":  # bottom left
        locations.append(index_to_list(tempind))
        tempind = tempind + 7
        tempcol = tempcol - 1
    if tempcol > 0 and tempind < 64 and isCapturable(board[tempind], turn): # blocked by piece
        locations.append(index_to_list(tempind))

    return locations


def locations_for_k(index, board, allLoc): # returns all possible locations for a black king
    locations = []
    col = index % 8 + 1
    king_list = []

    king_list = index_to_list(index + 8)
    if index + 8 < 64 and (board[index + 8] == "*" or isCapturable(board[index + 8], True)) and (not (king_list in allLoc)):  # down
        locations.append(index_to_list(index + 8))
    king_list = index_to_list(index - 8)
    if index - 8 > -1 and (board[index - 8] == "*" or isCapturable(board[index - 8], True)) and (not (king_list in allLoc)):  # up
        locations.append(index_to_list(index - 8))
    king_list = index_to_list(index + 1)
    if index + 1 < 64 and col < 8 and (board[index + 1] == "*" or isCapturable(board[index + 1], True)) and (not (king_list in allLoc)):  # right
        locations.append(index_to_list(index + 1))
    king_list = index_to_list(index - 1)
    if index - 1 > -1 and col > 1 and (board[index - 1] == "*" or isCapturable(board[index - 1], True)) and (not (king_list in allLoc)):  # left
        locations.append(index_to_list(index - 1))
    king_list = index_to_list(index - 7)
    if index - 7 > -1 and col < 8 and (board[index - 7] == "*" or isCapturable(board[index - 7], True)) and (not (king_list in allLoc)):  # top right
        locations.append(index_to_list(index - 7))
    king_list = index_to_list(index - 9)
    if index - 9 > -1 and col > 1 and (board[index - 9] == "*" or isCapturable(board[index - 9], True)) and (not (king_list in allLoc)):  # top left
        locations.append(index_to_list(index - 9))
    king_list = index_to_list(index + 9)
    if index + 9 < 64 and col < 8 and (board[index + 9] == "*" or isCapturable(board[index + 9], True)) and (not (king_list in allLoc)):  # bottom right
        locations.append(index_to_list(index + 9))
    king_list = index_to_list(index + 7)
    if index + 7 < 64 and col > 1 and (board[index + 7] == "*" or isCapturable(board[index + 7], True)) and (not (king_list in allLoc)):  # bottom left
        locations.append(index_to_list(index + 7))

    return locations

def locations_for_K(index, board, allLoc): # returns a list of all possible locations for a white king
    locations = []
    col = index%8 + 1
    king_list = []

    king_list = index_to_list(index + 8)
    if index + 8 < 64 and (board[index + 8] == "*" or isCapturable(board[index + 8], True)) and (not (king_list in allLoc)): # down
        locations.append(index_to_list(index + 8))
    king_list = index_to_list(index - 8)
    if index - 8 > -1 and (board[index - 8] == "*" or isCapturable(board[index - 8], True)) and (not (king_list in allLoc)): # up
        locations.append(index_to_list(index-8))
    king_list = index_to_list(index + 1)
    if index + 1 < 64 and col < 8 and (board[index + 1] == "*" or isCapturable(board[index + 1], True)) and (not (king_list in allLoc)): # right
        locations.append(index_to_list(index + 1))
    king_list = index_to_list(index - 1)
    if index - 1 > -1 and col > 1 and (board[index - 1] == "*" or isCapturable(board[index - 1], True)) and (not (king_list in allLoc)): # left
        locations.append(index_to_list(index - 1))
    king_list = index_to_list(index - 7)
    if index - 7 > -1 and col < 8 and (board[index - 7] == "*" or isCapturable(board[index - 7], True)) and (not (king_list in allLoc)): # top right
        locations.append(index_to_list(index - 7))
    king_list = index_to_list(index - 9)
    if index - 9 > -1 and col > 1 and (board[index - 9] == "*" or isCapturable(board[index - 9], True)) and (not (king_list in allLoc)): # top left
        locations.append(index_to_list(index - 9))
    king_list = index_to_list(index + 9)
    if index + 9 < 64 and col < 8 and (board[index + 9] == "*" or isCapturable(board[index + 9], True)) and (not (king_list in allLoc)): # bottom right
        locations.append(index_to_list(index + 9))
    king_list = index_to_list(index + 7)
    if index + 7 < 64 and col > 1 and (board[index + 7] == "*" or isCapturable(board[index + 7], True)) and (not (king_list in allLoc)): # bottom left
        locations.append(index_to_list(index + 7))

    return locations

def alternate_king(index, board, turn):
    locations = []
    col = index % 8 + 1

    if index + 8 < 64 and (board[index + 8] == "*" or isCapturable(board[index + 8], turn)):  # down
        locations.append(index_to_list(index + 8))
    if index - 8 > -1 and (board[index - 8] == "*" or isCapturable(board[index - 8], turn)):  # up
        locations.append(index_to_list(index - 8))
    if index + 1 < 64 and col < 8 and (board[index + 1] == "*" or isCapturable(board[index + 1], turn)):  # right
        locations.append(index_to_list(index + 1))
    if index - 1 > -1 and col > 1 and (board[index - 1] == "*" or isCapturable(board[index - 1], turn)):  # left
        locations.append(index_to_list(index - 1))
    if index - 7 > -1 and col < 8 and (board[index - 7] == "*" or isCapturable(board[index - 7], turn)):  # top right
        locations.append(index_to_list(index - 7))
    if index - 9 > -1 and col > 1 and (board[index - 9] == "*" or isCapturable(board[index - 9], turn)):  # top left
        locations.append(index_to_list(index - 9))
    if index + 9 < 64 and col < 8 and (board[index + 9] == "*" or isCapturable(board[index + 9], turn)):  # bottom right
        locations.append(index_to_list(index + 9))
    if index + 7 < 64 and col > 1 and (board[index + 7] == "*" or isCapturable(board[index + 7], turn)):  # bottom left
        locations.append(index_to_list(index + 7))

    return locations

def alternate_p(index, board): # method for getting all the places a black pawn can capture for allLoc
    locations = []
    col = index%8 + 1

    if index + 7 < 63 and col != 1 and isCapturable(board[index + 7], False): # if the space in bottom left of the black pawn can be captured
        locations.append(index_to_list(index + 7))

    if index + 9 < 63 and col != 8 and isCapturable(board[index + 9], False): # if the space in bottom right of the black pawn can be captured
        locations.append(index_to_list(index + 9))

    return locations

def alternate_P(index, board): # method for getting all the places a white pawn can capture for allLoc
    locations = []
    col = index % 8 + 1

    if index - 7 > -1 and col != 8 and isCapturable(board[index - 7], True):  # if the space in front right of the white pawn can be captured
        locations.append(index_to_list(index - 7))

    if index - 9 > -1 and col != 1 and isCapturable(board[index - 9], True):  # if the space in front left of the white pawn can be captured
        locations.append(index_to_list(index - 9))

    return locations


def inspect_for_check(white, board, temp_board): # returns whether the king is in check and the list of all moves any of the piece in the opposite side can make #### Uses both the board and temp_board because the board allows the method to find where the king is, and the temp_board allows for the TRUE allLoc
    allLoc = [] # for all moves
    cords_king = [] # for the cords of the king
    check = False
    oppside = False # color of opposite side
    waste_storage = []

    if white: # gets the board needed for the pawn because a pawn needs to know that the kings location is capturable
        pawn_board = board.replace("K", "P")
    else:
        pawn_board = board.replace("k", "p")

    if white: # gets the cords for color of king and gets the color of opposite side
        king = "K"
        index_king = board.find("K")
        cords_king = index_to_list(index_king)
        oppside = False
    else:
        king = "k"
        index_king = board.find("k")
        cords_king = index_to_list(index_king)
        oppside = True

    for x in range(0, 64): # iterate through the board(temp board because if the king is there, allLoc will be blocked by the king and won't be able to get the TRUE allLoc
        piece = temp_board[x]
        if belongs(oppside, piece): # if the piece belongs to the opposite side
            if piece in "Kk": # The king is a separate case because if the original one is used, then it will worry about the spaces it can't go through because of being checked, and it will run in a forever loop
                allLoc = allLoc + alternate_king(x, temp_board, white)
            elif piece == "P":
                allLoc = allLoc + alternate_P(x, pawn_board) # pawn_board for white pawn
            elif piece == "p":
                allLoc = allLoc + alternate_p(x, pawn_board)# pawn_board for black pawn
            else:
                allLoc = allLoc + give_all_locations(x, piece, temp_board, waste_storage) # otherwise, any piece can follow this guideline

    if cords_king in allLoc: # if the king is in check
        check = True

    return check, allLoc, index_king, king


def display(boards): # displays the board
    print("Chess board:")
    print("   1  2  3  4  5  6  7  8")
    for x in range(0, 64, 8):
        temp = "" + str(int(( x /8 + 1))) + "  "
        for y in range(x, x + 8):
         temp = temp + boards[y] + "  "
        print(temp)
    print("   1  2  3  4  5  6  7  8")

def is_right_piece(white, row, col, board): # checks if the piece belongs to the turn using a helper mthod
    index = (int(row) - 1) * 8 + (int(col) - 1) # gets index of the piece on the board

    return belongs(white, board[index])

def belongs(white, piece): # checks if the piece belong to the turn
    if white == True:  # If it's white's turn
        if piece in "PKQBNR":
            return True
        else:
            return False

    else:  # If it's black's turn
        if piece in "pkqbnr":
            return True
        else:
            return False

def print_options(locations): # prints all the possible moves in a visually pleasing way
    for x in range(0, len(locations)):
        print(str(x + 1), locations[x], " ", end=" ")
    print()

def list_to_index(newlocation): # turns a list(of a coordinate) to an index using the helper method
    return rc_to_index(newlocation[0], newlocation[1])

def make_the_move(index, newindex, board): # makes the move from the old index to the new index
    temp = board
    tboard = "" # not "board" just to ensure the original doesn't get tampered with
    piece = temp[index]
    for x in range(0, 64):
        if x == index:
            tboard = tboard + "*"
        elif x == newindex:
            tboard = tboard + piece
        else:
            tboard = tboard + temp[x]

    return tboard



# Variables needed
board = "rnbqkbnrpppppppp********************************PPPPPPPPRNBQKBNR"  # Chess board
white = True  # Keeps track of player's turn
check = False # the boolean variable for check
allLoc = [] # keeps track of all the locations


while True:  # Lasting forever

    display(board) # displays the board

    if white:  # gets to king of the current color that it's in
        indexking_for_allLoc = board.find("K")
    else:
        indexking_for_allLoc = board.find("k")

    temp_board = make_the_move(indexking_for_allLoc, 100, board) # gets the board without the king so then allLoc gets the true allLoc


    check, allLoc, index_king, king = inspect_for_check(white, board, temp_board) # gets if the king is in check and all the locations # also gets index_king and king to make the king_locations easier

    if check: # checks for checkmate and the game is over
        king_locations = give_all_locations(index_king, king, board, allLoc)
        if len(king_locations) == 0: # if king has nowhere to go either
            if white:
                print("CHECKMATE! WHITE WINS!")
                break
            else:
                print("CHECKMATE! BLACK WINS!")
                break
        else:
            print("You're in check!")



    if white == True: # prints the player's turn
        print("White's turn to move a piece")
    else:
        print("Black's turn to move a piece")

    while True: # To ensure that if they move a piece, their king won't be in check, otherwise loop through this while loop

        while True: # just in case they choose a valid piece on their side, but they cannot move it

            while True:  # Gets row and column of piece

                while True:  # Gets the row of the piece
                    row = input("Type the row of your piece or type end to end the game ")

                    if row == "end":
                        print("Game is over, thanks for playing!")
                        break  # leaves the while loop of getting the row loop
                    elif row in "12345678":  # row in string of 1 through 8
                        break
                    else:
                        print("Sorry that is not a valid response, try again")


                if row == "end": # ends the game
                    break  # leaves the while loop of getting the row&col loop


                while True:  # Gets the column of the piece
                    col = input("Type the column of the piece ")

                    if col in "12345678":
                        break
                    else:
                        print("Sorry that is not a valid response, try again")

                if is_right_piece(white, row, col, board):  # if the piece on the board belongs to the color's turn
                    break
                else:
                    print("Sorry, you do not have a piece at that location, try again")

            if row == "end":  # leaves the while loop of running the choosing of a piece
                break


            index = rc_to_index(row, col) #gets index of the piece on the board (INT)
            piece = board[index] #gets the piece at the board (STRING)

            locations = give_all_locations(index, piece, board, allLoc) # gets a list of all possible locations for the piece at that location to go to

            if len(locations) == 0: # if the piece cannot be moved
                print("Sorry, you can't move this piece, choose another one")
            else:
                break


        if row == "end": # leaves the while loop of ensuring their move doesn't leave them in a check
            break

        print("Choose a move:")
        print_options(locations)

        while True:  # to ensure they choose a valid option
            option = input()
            if option.isdigit() == False:
                print("Not a valid option, try again")
            elif int(option) < 1 or int(option) > len(locations):
                print("Not a valid option, try again")
            else:
                break

        newlocation = locations[int(option) - 1] # which location
        newindex = list_to_index(newlocation) # index of the new location
        backup_board = board # for the backup board
        board = make_the_move(index, newindex, board) # makes the official move to be further judged

        if white:  # gets to king of the current color that it's in # it has to get the indexking again because the old one won't apply if they move the king
            indexking_for_allLoc = board.find("K")
        else:
            indexking_for_allLoc = board.find("k")

        temp_board = make_the_move(indexking_for_allLoc, 100, board)  # gets the board without the king so then it gives the true "check" verdict # the old temp_board can't be used because we just made a move that is now being judged

        check, random, irrelevant, useless = inspect_for_check(white, board, temp_board)
        if check: # if their king happens to be in check after making the move, they can't make the move
            print("Sorry, you can't move there or else you will be in check")
            board = backup_board # the original board is set to the back_up
        else:
            break

    if row == "end": # leaves the entire game
        break

    if white == True:
        white = False
    else:
        white = True