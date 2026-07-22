import pygame
from board import Board
from sys import exit
from piecesMove import *

pygame.init()
pygame.display.set_caption("Chess")
screen = pygame.display.set_mode((1280, 720))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()

def getClickedSquare():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    local_x, local_y = mouse_x - 320, mouse_y - 40
    if local_x >= 0 and local_y >= 0 and local_x < 640 and local_y < 640:
        square_x = local_x // 80
        square_y = local_y // 80
        return [square_y, square_x]
    return None

def getLegalMoves(piece, start_row, start_col, board):
    attacked_squares = getAttackedSquares(board.boardState, board.move_turn)
    if piece.lower() == "p":
        pawn_possible_move = pawnMove(piece, start_row, start_col, board.boardState)
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
                      
def main():
    running = True
    board = Board()

    selected_square = None
    legal_moves = []
    king_in_check = False

    game_over = None

    promote_time = False
    pawn_promote_pos = []
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked_position = getClickedSquare()
                if not clicked_position: continue

                if selected_square is None and game_over is None and promote_time is False:
                        if clicked_position != None:
                            clicked_row, clicked_col = clicked_position[0], clicked_position[1]

                        if board.boardState[clicked_row][clicked_col] != "":
                            piece = board.boardState[clicked_row][clicked_col]
                            if piece.islower() and board.move_turn == "black" or piece.isupper() and board.move_turn == "white":
                                selected_square = [clicked_row, clicked_col]
                                legal_moves = getLegalMoves(piece, clicked_row, clicked_col, board)
                            else: print("Not your Move!"); 

                        
                else:
                    if game_over is not None or promote_time is True: 
                        clicked_position = getClickedSquare()
                        pawn_row = 0 if board.move_turn == "white" else 7
                        promotion_row = 0 if board.move_turn == "white" else 7
                        operation1 = 1 if board.move_turn == "white" else -1
                        operation2 = 2 if board.move_turn == "white" else -2
                        operation3 = 3 if board.move_turn == "white" else -3
                        end_row, end_col = clicked_position[0], clicked_position[1]
                        if end_row == pawn_row and end_col == pawn_promote_pos[1]:
                            board.boardState[pawn_row][end_col] = "Q" if board.move_turn == "white" else "q"
                            promote_time = False
                            if board.move_turn == "white": board.move_turn = "black"
                            else: board.move_turn = "white"
                            king_in_check = isKingInCheck(board.boardState, board.move_turn)
                            game_over = checkGameStatus(board, king_in_check)

                        elif end_row == (pawn_row + operation1) and end_col == pawn_promote_pos[1]:
                            board.boardState[promotion_row][end_col] = "N" if board.move_turn == "white" else "n"
                            promote_time = False
                            if board.move_turn == "white": board.move_turn = "black"
                            else: board.move_turn = "white"
                            king_in_check = isKingInCheck(board.boardState, board.move_turn)
                            game_over = checkGameStatus(board, king_in_check)

                        if end_row == (pawn_row + operation2) and end_col == pawn_promote_pos[1]:
                            board.boardState[promotion_row][end_col] = "R" if board.move_turn == "white" else "r"
                            promote_time = False
                            if board.move_turn == "white": board.move_turn = "black"
                            else: board.move_turn = "white"
                            king_in_check = isKingInCheck(board.boardState, board.move_turn)
                            game_over = checkGameStatus(board, king_in_check)

    
                        if end_row == (pawn_row + operation3) and end_col == pawn_promote_pos[1]:
                            board.boardState[promotion_row][end_col] = "B" if board.move_turn == "white" else "b"
                            promote_time = False
                            if board.move_turn == "white": board.move_turn = "black"
                            else: board.move_turn = "white"
                            king_in_check = isKingInCheck(board.boardState, board.move_turn)
                            game_over = checkGameStatus(board, king_in_check)
                            
                        continue

                    start_row, start_col = selected_square[0], selected_square[1]
                    clicked_position = getClickedSquare()

                    if clicked_position != None: 
                        piece = board.boardState[start_row][start_col]
                        end_row, end_col = clicked_position[0], clicked_position[1]

                        if legal_moves == None: continue

                        if [end_row, end_col] in legal_moves:

                            if board.movePiece(start_row, start_col, end_row, end_col, piece, board.boardState, screen) == "promote_time":
                                promote_time = True
                                pawn_promote_pos = [end_row, end_col]

                            if piece.isupper() and promote_time is False: board.move_turn = "black"
                            elif piece.islower() and promote_time is False: board.move_turn = "white"
                            king_in_check = isKingInCheck(board.boardState, board.move_turn)
                            game_over = checkGameStatus(board, king_in_check)
                            
                            selected_square = None
                            
                        elif [end_row, end_col] not in legal_moves and board.boardState[end_row][end_col] == "":
                            selected_square = None

                        elif board.boardState[end_row][end_col] != "":
                            if board.boardState[end_row][end_col].islower() and board.move_turn == "black" or board.boardState[end_row][end_col].isupper() and board.move_turn == "white":
                                selected_square = [end_row, end_col]
                                piece = board.boardState[end_row][end_col]
                                legal_moves = getLegalMoves(piece, end_row, end_col, board)
                            continue
                    else: 
                        continue
                
                
        screen.fill("#312e2b")
        board.drawSquares(screen)
        if king_in_check:
            board.highlightKingCheck(screen, findKingPosition(board.boardState, board.move_turn))
        if selected_square is not None:
            board.highlightSquare(screen, selected_square)
        board.drawBoard(screen, screen_rect)
        board.drawPieces(screen)
        if selected_square is not None:
            board.highlightLegalMoves(screen, legal_moves)
        if promote_time == True:
            board.promotePawn(screen, pawn_promote_pos, board.move_turn)
        if game_over is not None:
            board.drawGameOver(screen, game_over, pygame.font.SysFont("Arial", 30))


        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    exit()


if __name__ == "__main__":
    main()