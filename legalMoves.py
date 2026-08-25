from piecesMove import *

def getLegalMoves(piece, start_row, start_col, board):
    attacked_squares = getAttackedSquares(board.boardState, board.move_turn)
    if piece.lower() == "p":
        pawn_possible_move = pawnMove(piece, start_row, start_col, board.boardState)
        if [start_row, start_col] in board.en_passant:
            pawn_possible_move.append(board.en_passant[-1])
        return filterSafeMoves(start_row, start_col, pawn_possible_move, piece, board.boardState, board.move_turn)
    
    elif piece.lower() == "r":
        rook_possible_move = rookMove(piece, start_row, start_col, board.boardState)
        return filterSafeMoves(start_row, start_col, rook_possible_move, piece, board.boardState, board.move_turn)
    
    elif piece.lower() == "n":
        knight_possible_move = knightMove(piece, start_row, start_col, board.boardState)
        return filterSafeMoves(start_row, start_col, knight_possible_move, piece, board.boardState, board.move_turn)
    
    elif piece.lower() == "b":
        bishop_possible_move = bishopMove(piece, start_row, start_col, board.boardState)
        return filterSafeMoves(start_row, start_col, bishop_possible_move, piece, board.boardState, board.move_turn)
    
    elif piece.lower() == "q":
        queen_possible_move = queenMove(piece, start_row, start_col, board.boardState)
        return filterSafeMoves(start_row, start_col, queen_possible_move, piece, board.boardState, board.move_turn)
    
    elif piece.lower() == "k":
        left_rook_has_moved = board.white_left_rook_has_moved if board.move_turn == "white" else board.black_left_rook_has_moved
        right_rook_has_moved = board.white_right_rook_has_moved if board.move_turn == "white" else board.black_right_rook_has_moved
        king_has_moved = board.white_king_has_moved if board.move_turn == "white" else board.black_king_has_moved

        king_possible_move = kingMove(piece, start_row, start_col, board.boardState)

        rook_depending = "r" if board.move_turn == "black" else "R"
        
        filtered_king_possible_move = []
        for move in king_possible_move:
            if move not in attacked_squares:
                filtered_king_possible_move.append(move)
            else:
                continue
        
        king_possible_castling = []
        king_in_check = isKingInCheck(board.boardState, board.move_turn)
        if king_has_moved == False and right_rook_has_moved == False and king_in_check == False and[start_row, start_col+1] not in attacked_squares and board.boardState[start_row][7] == rook_depending:
            if board.boardState[start_row][start_col+1] == "" and board.boardState[start_row][start_col+2] == "":
                if board.move_turn == "white":
                    king_possible_castling.append([7, 6])
                else:
                    king_possible_castling.append([0, 6])
            
        if king_has_moved == False and left_rook_has_moved == False and king_in_check == False and [start_row, start_col-1] not in attacked_squares and board.boardState[start_row][0] == rook_depending:
            if board.boardState[start_row][start_col-1] == "" and board.boardState[start_row][start_col-2] == "" and board.boardState[start_row][start_col-3] == "":
                if board.move_turn == "white":
                    king_possible_castling.append([7, 2])
                else:
                    king_possible_castling.append([0, 2])
        
        for move in king_possible_castling:
            if move not in attacked_squares:
                filtered_king_possible_move.append(move)
            else:
                continue
        
        return filtered_king_possible_move
    
def hasAnyLegalMoves(board):
    piece_name = "RNBQKP" if board.move_turn == "white" else "rnbqkp"
    remaining_legal_moves = []

    for row in range(8):
        for col in range(8):
            if board.boardState[row][col] != "" and board.boardState[row][col] in piece_name:
                for legal_list in getLegalMoves(board.boardState[row][col], row, col, board):
                    remaining_legal_moves.append(legal_list)
    
    if remaining_legal_moves: return True
    else: return False

def checkGameStatus(board, king_in_check):
    if not hasAnyLegalMoves(board) and king_in_check:
        return "checkmate"
    elif not hasAnyLegalMoves(board) and not king_in_check:
        return "stalemate"
