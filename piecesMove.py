def pawnMove(piece, row, col, boardState):
        two_row_after = -2 if piece == "P" else 2
        one_row_after = -1 if piece == "P" else 1
        starting_row = 6 if piece == "P" else 1
        possible_move = []

        if (col < 7 and boardState[row + one_row_after][col + 1] != ""):
            if col < 7 and boardState[row][col].isupper() ^ boardState[row + one_row_after][col + 1].isupper():
                possible_move.append([row + one_row_after, col + 1])
        if (col > 0 and boardState[row + one_row_after][col - 1] != ""):
            if col > 0 and boardState[row][col].isupper() ^ boardState[row + one_row_after][col - 1].isupper():
                possible_move.append([row + one_row_after, col - 1])

        if row == starting_row:

            if boardState[row + two_row_after][col] == "" and boardState[row + one_row_after][col] == "":
                possible_move.append([row + one_row_after, col])
                possible_move.append([row + two_row_after, col])
                return possible_move
            
            if boardState[row + one_row_after][col] != "":
                return possible_move
            
            if boardState[row + two_row_after][col] != "":
                possible_move.append([row + one_row_after, col])
                return possible_move
            
            else:
                return possible_move
            
        else:
            if boardState[row + one_row_after][col] == "":
                possible_move.append([row + one_row_after, col])
                return possible_move
            else:
                return possible_move
