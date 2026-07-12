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


    for top_row in range(row-1, -1, -1):
        if boardState[top_row][col] != "" and boardState[top_row][col].isupper() ^ piece.isupper():
            rook_possible_move.append([top_row, col])

        if boardState[top_row][col] != "":
            break
        
        if boardState[top_row][col] == "":
            rook_possible_move.append([top_row, col])

    for bottom_row in range(row+1, 8, 1):
        if boardState[bottom_row][col] != "" and boardState[bottom_row][col].isupper() ^ piece.isupper():
            rook_possible_move.append([bottom_row, col])

        if boardState[bottom_row][col] != "":
            break
        
        if boardState[bottom_row][col] == "":
            rook_possible_move.append([bottom_row, col])
    
    return rook_possible_move

def rookAttackingMove(row, col, boardState, move_turn):
    rook_attack_move = []
    king = "K" if move_turn == "white" else "k"

    for left_col in range(col-1, -1, -1):
        if boardState[row][left_col] == king:
            rook_attack_move.append([row, left_col])
            continue

        if boardState[row][left_col] != "" and boardState[row][left_col] != king:
            rook_attack_move.append([row, left_col])
            break

        if boardState[row][left_col] == "":
            rook_attack_move.append([row, left_col])

    for right_col in range(col+1, 8, 1):
        if boardState[row][right_col] == king:
            rook_attack_move.append([row, right_col])
            continue

        if boardState[row][right_col] != "" and boardState[row][right_col] != king:
            rook_attack_move.append([row, right_col])
            break

        if boardState[row][right_col] == "":
            rook_attack_move.append([row, right_col])

    for top_row in range(row-1, -1, -1):
        if boardState[top_row][col] == king:
            rook_attack_move.append([top_row, col])
            continue

        if boardState[top_row][col] != "" and boardState[top_row][col] != king:
            rook_attack_move.append([top_row, col])
            break

        if boardState[top_row][col] == "":
            rook_attack_move.append([top_row, col])

    for bottom_row in range(row+1, 8, 1):
        if boardState[bottom_row][col] == king:
            rook_attack_move.append([bottom_row, col])
            continue

        if boardState[bottom_row][col] != "" and boardState[bottom_row][col] != king:
            rook_attack_move.append([bottom_row, col])
            break

        if boardState[bottom_row][col] == "":
            rook_attack_move.append([bottom_row, col])
    return rook_attack_move
    

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

def bishopAttackingMove(row, col, boardState, move_turn):
    bishop_attack_move = []
    king = "K" if move_turn == "white" else "k"
    top_left_diagonal_row = row
    top_left_diagonal_col = col
    while top_left_diagonal_row > 0 or top_left_diagonal_col > 0:
        if top_left_diagonal_row == 0 or top_left_diagonal_col == 0: break
        top_left_diagonal_row -=1
        top_left_diagonal_col -=1
        if boardState[top_left_diagonal_row][top_left_diagonal_col] == king:
            bishop_attack_move.append([top_left_diagonal_row, top_left_diagonal_col])
            continue

        if boardState[top_left_diagonal_row][top_left_diagonal_col] != "" and boardState[top_left_diagonal_row][top_left_diagonal_col] != king:
            bishop_attack_move.append([top_left_diagonal_row, top_left_diagonal_col])

        if boardState[top_left_diagonal_row][top_left_diagonal_col] != "": 
            bishop_attack_move.append([top_left_diagonal_row, top_left_diagonal_col])
            break

        bishop_attack_move.append([top_left_diagonal_row, top_left_diagonal_col])

    
    top_right_diagonal_row = row
    top_right_diagonal_col = col
    while top_right_diagonal_row > 0 or top_right_diagonal_col < 7:
        if top_right_diagonal_row == 0 or top_right_diagonal_col == 7: break
        top_right_diagonal_row -=1
        top_right_diagonal_col +=1
        if boardState[top_right_diagonal_row][top_right_diagonal_col] == king:
            bishop_attack_move.append([top_right_diagonal_row, top_right_diagonal_col])
            continue

        if boardState[top_right_diagonal_row][top_right_diagonal_col] != "" and boardState[top_right_diagonal_row][top_right_diagonal_col] != king:
            bishop_attack_move.append([top_right_diagonal_row, top_right_diagonal_col])

        if boardState[top_right_diagonal_row][top_right_diagonal_col] != "": 
            bishop_attack_move.append([top_right_diagonal_row, top_right_diagonal_col])
            break

        bishop_attack_move.append([top_right_diagonal_row, top_right_diagonal_col])


    bottom_left_diagonal_row = row
    bottom_left_diagonal_col = col
    while bottom_left_diagonal_row < 7 or bottom_left_diagonal_col > 0:
        if bottom_left_diagonal_row == 7 or bottom_left_diagonal_col == 0: break
        bottom_left_diagonal_row +=1
        bottom_left_diagonal_col -=1
        if boardState[bottom_left_diagonal_row][bottom_left_diagonal_col] == king:
            bishop_attack_move.append([bottom_left_diagonal_row, bottom_left_diagonal_col])
            continue

        if boardState[bottom_left_diagonal_row][bottom_left_diagonal_col] != "" and boardState[bottom_left_diagonal_row][bottom_left_diagonal_col] != king:
            bishop_attack_move.append([bottom_left_diagonal_row, bottom_left_diagonal_col])

        if boardState[bottom_left_diagonal_row][bottom_left_diagonal_col] != "": 
            bishop_attack_move.append([bottom_left_diagonal_row, bottom_left_diagonal_col])
            break

        bishop_attack_move.append([bottom_left_diagonal_row, bottom_left_diagonal_col])


    bottom_right_diagonal_row = row
    bottom_right_diagonal_col = col
    while bottom_right_diagonal_row < 7 or bottom_right_diagonal_col < 7:
        if bottom_right_diagonal_row == 7 or bottom_right_diagonal_col == 7: break
        bottom_right_diagonal_row +=1
        bottom_right_diagonal_col +=1
        if boardState[bottom_right_diagonal_row][bottom_right_diagonal_col] == king:
            bishop_attack_move.append([bottom_right_diagonal_row, bottom_right_diagonal_col])
            continue

        if boardState[bottom_right_diagonal_row][bottom_right_diagonal_col] != "" and boardState[bottom_right_diagonal_row][bottom_right_diagonal_col] != king:
            bishop_attack_move.append([bottom_right_diagonal_row, bottom_right_diagonal_col])

        if boardState[bottom_right_diagonal_row][bottom_right_diagonal_col] != "": 
            bishop_attack_move.append([bottom_right_diagonal_row, bottom_right_diagonal_col])
            break

        bishop_attack_move.append([bottom_right_diagonal_row, bottom_right_diagonal_col])


    return bishop_attack_move


def queenMove(piece, row, col, boardState):
    queen_possible_move = []
    line_move = rookMove(piece, row, col, boardState)
    for line in line_move: queen_possible_move.append(line)

    diagonal_move = bishopMove(piece, row, col, boardState)
    for diagonal in diagonal_move: queen_possible_move.append(diagonal)
    
    return queen_possible_move

def queenAttackingMove(row, col, boardState, move_turn):
    queen_attacking_move = []
    line_attacking_move = rookAttackingMove(row, col, boardState, move_turn)
    for attacking_line in line_attacking_move: queen_attacking_move.append(attacking_line)

    diagonal_attacking_move = bishopAttackingMove(row, col, boardState, move_turn)
    for attacking_diagonal in diagonal_attacking_move: queen_attacking_move.append(attacking_diagonal)

    return queen_attacking_move


def kingMove(piece, row, col, boardState):
    king_possible_move = []

    if col > 0 and (boardState[row][col-1] == "" or boardState[row][col-1].isupper() ^ piece.isupper()):
        king_possible_move.append([row, col-1])

    if col < 7 and (boardState[row][col+1] == "" or boardState[row][col+1].isupper() ^ piece.isupper()):
        king_possible_move.append([row, col+1])

    if row > 0:
        if (boardState[row-1][col] == "" or boardState[row-1][col].isupper() ^ piece.isupper()):
            king_possible_move.append([row-1, col])

        if col > 0 and (boardState[row-1][col-1] == "" or boardState[row-1][col-1].isupper() ^ piece.isupper()):
            king_possible_move.append([row-1, col-1])

        if col < 7 and (boardState[row-1][col+1] == "" or boardState[row-1][col+1].isupper() ^ piece.isupper()):
            king_possible_move.append([row-1, col+1])

    if row < 7:
        if (boardState[row+1][col] == "" or boardState[row+1][col].isupper() ^ piece.isupper()):
            king_possible_move.append([row+1, col])

        if col > 0 and (boardState[row+1][col-1] == "" or boardState[row+1][col-1].isupper() ^ piece.isupper()):
            king_possible_move.append([row+1, col-1])

        if col < 7 and (boardState[row+1][col+1] == "" or boardState[row+1][col+1].isupper() ^ piece.isupper()):
            king_possible_move.append([row+1, col+1])

    return king_possible_move

def kingAttackingMove(row, col, boardState, move_turn):
    king_attack_move = []

    king_attack_move.append([row-1, col-1])
    king_attack_move.append([row-1, col])
    king_attack_move.append([row-1, col+1])
    king_attack_move.append([row, col-1])
    king_attack_move.append([row, col+1])
    king_attack_move.append([row+1, col-1])
    king_attack_move.append([row+1, col])
    king_attack_move.append([row+1, col+1])

    return king_attack_move


def getAttackedSquares(boardState, move_turn):
    attacked_squares = []
    if move_turn == "white":
        for row in range(8):
            for col in range(8):
                if boardState[row][col] == "": continue

                if boardState[row][col] == "r":
                    attacked_squares += rookAttackingMove(row, col, boardState, move_turn)
                
                if boardState[row][col] == "n":
                    attacked_squares += knightMove(boardState[row][col], row, col, boardState)

                if boardState[row][col] == "b":
                    attacked_squares += bishopAttackingMove(row, col, boardState, move_turn)
                
                if boardState[row][col] == "q":
                    attacked_squares += queenAttackingMove(row, col, boardState, move_turn)

                if boardState[row][col] == "k":
                    attacked_squares += kingAttackingMove(row, col, boardState, move_turn)

                if boardState[row][col] == "p":
                    if col > 0:
                        attacked_squares.append([row+1, col-1])
                    if col < 7:
                        attacked_squares.append([row+1, col+1])

    elif move_turn == "black":
        for row in range(8):
            for col in range(8):
                if boardState[row][col] == "": continue

                if boardState[row][col] == "R":
                    attacked_squares += rookAttackingMove(row, col, boardState, move_turn)
                
                if boardState[row][col] == "N":
                    attacked_squares += knightMove(boardState[row][col], row, col, boardState)

                if boardState[row][col] == "B":
                    attacked_squares += bishopAttackingMove(row, col, boardState, move_turn)
                
                if boardState[row][col] == "Q":
                    attacked_squares += queenAttackingMove(row, col, boardState, move_turn)

                if boardState[row][col] == "K":
                    attacked_squares += kingAttackingMove(row, col, boardState, move_turn)

                if boardState[row][col] == "P":
                    if col > 0:
                        attacked_squares.append([row-1, col-1])
                    if col < 7:
                        attacked_squares.append([row-1, col+1])
    return attacked_squares