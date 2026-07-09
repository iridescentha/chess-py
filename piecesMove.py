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
    
