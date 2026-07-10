def pawnMove(piece, row, col, boardState):
        two_row_after = -2 if piece == "P" else 2
        one_row_after = -1 if piece == "P" else 1
        starting_row = 6 if piece == "P" else 1
        pawn_possible_move = []

        if (col < 7 and boardState[row + one_row_after][col + 1] != ""):
            if col < 7 and boardState[row][col].isupper() ^ boardState[row + one_row_after][col + 1].isupper():
                pawn_possible_move.append([row + one_row_after, col + 1])
        if (col > 0 and boardState[row + one_row_after][col - 1] != ""):
            if col > 0 and boardState[row][col].isupper() ^ boardState[row + one_row_after][col - 1].isupper():
                pawn_possible_move.append([row + one_row_after, col - 1])

        if row == starting_row:

            if boardState[row + two_row_after][col] == "" and boardState[row + one_row_after][col] == "":
                pawn_possible_move.append([row + one_row_after, col])
                pawn_possible_move.append([row + two_row_after, col])
                return pawn_possible_move
            
            if boardState[row + one_row_after][col] != "":
                return pawn_possible_move
            
            if boardState[row + two_row_after][col] != "":
                pawn_possible_move.append([row + one_row_after, col])
                return pawn_possible_move
            
            else:
                return pawn_possible_move
            
        else:
            if boardState[row + one_row_after][col] == "":
                pawn_possible_move.append([row + one_row_after, col])
                return pawn_possible_move
            else:
                return pawn_possible_move


def rookMove(piece, row, col, boardState):
    rook_possible_move = []

    for left_col in range(col-1, -1, -1):
        if boardState[row][left_col] != "" and boardState[row][left_col].isupper() ^ piece.isupper():
            rook_possible_move.append([row, left_col])

        if boardState[row][left_col] != "":
            break

        if boardState[row][left_col] == "":
            rook_possible_move.append([row, left_col])
        
    for right_col in range(col+1, 8, 1):
        if boardState[row][right_col] != "" and boardState[row][right_col].isupper() ^ piece.isupper():
            rook_possible_move.append([row, right_col])

        if boardState[row][right_col] != "":
            break
        
        if boardState[row][right_col] == "":
            rook_possible_move.append([row, right_col])


    for left_row in range(row-1, -1, -1):
        if boardState[left_row][col] != "" and boardState[left_row][col].isupper() ^ piece.isupper():
            rook_possible_move.append([left_row, col])

        if boardState[left_row][col] != "":
            break
        
        if boardState[left_row][col] == "":
            rook_possible_move.append([left_row, col])

    for right_row in range(row+1, 8, 1):
        if boardState[right_row][col] != "" and boardState[right_row][col].isupper() ^ piece.isupper():
            rook_possible_move.append([right_row, col])

        if boardState[right_row][col] != "":
            break
        
        if boardState[right_row][col] == "":
            rook_possible_move.append([right_row, col])
    
    return rook_possible_move
    

def knightMove(piece, row, col, boardState):
    knight_possible_move = []
    if row > 1:
        if col > 0 and (boardState[row-2][col-1] == "" or boardState[row-2][col-1].isupper() ^ piece.isupper()):
            knight_possible_move.append([row-2, col-1])

        if col < 7 and (boardState[row-2][col+1] == "" or boardState[row-2][col+1].isupper() ^ piece.isupper()):
            knight_possible_move.append([row-2, col+1])

    if row > 1 or row == 1:
        if col > 1 and (boardState[row-1][col-2] == "" or boardState[row-1][col-2].isupper() ^ piece.isupper()):
            knight_possible_move.append([row-1, col-2])

        if col < 6 and (boardState[row-1][col+2] == "" or boardState[row-1][col+2].isupper() ^ piece.isupper()):
            knight_possible_move.append([row-1, col+2])

    if row < 6:
        if col > 0 and (boardState[row+2][col-1] == "" or boardState[row+2][col-1].isupper() ^ piece.isupper()):
            knight_possible_move.append([row+2, col-1])

        if col < 7 and (boardState[row+2][col+1] == "" or boardState[row+2][col+1].isupper() ^ piece.isupper()):
            knight_possible_move.append([row+2, col+1])

    if row < 6 or row == 6:
        if col > 1 and (boardState[row+1][col-2] == "" or boardState[row+1][col-2].isupper() ^ piece.isupper()):
            knight_possible_move.append([row+1, col-2])

        if col < 6 and (boardState[row+1][col+2] == "" or boardState[row+1][col+2].isupper() ^ piece.isupper()): 
            knight_possible_move.append([row+1, col+2])
    return knight_possible_move

def bishopMove(piece, row, col, boardState):
    bishop_possible_move = []
    top_left_diagonal_row = row
    top_left_diagonal_col = col
    while top_left_diagonal_row > 0 or top_left_diagonal_col > 0:
        if top_left_diagonal_row == 0 or top_left_diagonal_col == 0: break
        top_left_diagonal_row -=1
        top_left_diagonal_col -=1
        if boardState[top_left_diagonal_row][top_left_diagonal_col] != "" and boardState[top_left_diagonal_row][top_left_diagonal_col].isupper() ^ piece.isupper():
            bishop_possible_move.append([top_left_diagonal_row, top_left_diagonal_col])

        if boardState[top_left_diagonal_row][top_left_diagonal_col] != "": break

        bishop_possible_move.append([top_left_diagonal_row, top_left_diagonal_col])

    top_right_diagonal_row = row
    top_right_diagonal_col = col
    while top_right_diagonal_row > 0 or top_right_diagonal_col < 7:
        if top_right_diagonal_row == 0 or top_right_diagonal_col == 7: break
        top_right_diagonal_row -=1
        top_right_diagonal_col +=1
        if boardState[top_right_diagonal_row][top_right_diagonal_col] != "" and boardState[top_right_diagonal_row][top_right_diagonal_col].isupper() ^ piece.isupper():
            bishop_possible_move.append([top_right_diagonal_row, top_right_diagonal_col])

        if boardState[top_right_diagonal_row][top_right_diagonal_col] != "": break

        bishop_possible_move.append([top_right_diagonal_row, top_right_diagonal_col])

    bottom_left_diagonal_row = row
    bottom_left_diagonal_col = col
    while bottom_left_diagonal_row < 7 or bottom_left_diagonal_col > 0:
        if bottom_left_diagonal_row == 7 or bottom_left_diagonal_col == 0: break
        bottom_left_diagonal_row +=1
        bottom_left_diagonal_col -=1
        if boardState[bottom_left_diagonal_row][bottom_left_diagonal_col] != "" and boardState[bottom_left_diagonal_row][bottom_left_diagonal_col].isupper() ^ piece.isupper():
            bishop_possible_move.append([bottom_left_diagonal_row, bottom_left_diagonal_col])

        if boardState[bottom_left_diagonal_row][bottom_left_diagonal_col] != "": break

        bishop_possible_move.append([bottom_left_diagonal_row, bottom_left_diagonal_col])

    bottom_right_diagonal_row = row
    bottom_right_diagonal_col = col
    while bottom_right_diagonal_row < 7 or bottom_right_diagonal_col < 7:
        if bottom_right_diagonal_row == 7 or bottom_right_diagonal_col == 7: break
        bottom_right_diagonal_row +=1
        bottom_right_diagonal_col +=1
        if boardState[bottom_right_diagonal_row][bottom_right_diagonal_col] != "" and boardState[bottom_right_diagonal_row][bottom_right_diagonal_col].isupper() ^ piece.isupper():
            bishop_possible_move.append([bottom_right_diagonal_row, bottom_right_diagonal_col])

        if boardState[bottom_right_diagonal_row][bottom_right_diagonal_col] != "": break

        bishop_possible_move.append([bottom_right_diagonal_row, bottom_right_diagonal_col])
    
    return bishop_possible_move
