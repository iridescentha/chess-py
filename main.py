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

def getLegalMoves(piece, start_row, start_col, boardState, move_turn):
    attacked_squares = getAttackedSquares(boardState, move_turn)
    if piece.lower() == "p":
        pawn_possible_move = pawnMove(piece, start_row, start_col, boardState)
        return filterSafeMoves(start_row, start_col, pawn_possible_move, piece, boardState, move_turn)
    
    elif piece.lower() == "r":
        rook_possible_move = rookMove(piece, start_row, start_col, boardState)
        return filterSafeMoves(start_row, start_col, rook_possible_move, piece, boardState, move_turn)
    
    elif piece.lower() == "n":
        knight_possible_move = knightMove(piece, start_row, start_col, boardState)
        return filterSafeMoves(start_row, start_col, knight_possible_move, piece, boardState, move_turn)
    
    elif piece.lower() == "b":
        bishop_possible_move = bishopMove(piece, start_row, start_col, boardState)
        return filterSafeMoves(start_row, start_col, bishop_possible_move, piece, boardState, move_turn)
    
    elif piece.lower() == "q":
        queen_possible_move = queenMove(piece, start_row, start_col, boardState)
        return filterSafeMoves(start_row, start_col, queen_possible_move, piece, boardState, move_turn)
    
    elif piece.lower() == "k":
        king_possible_move = kingMove(piece, start_row, start_col, boardState)
        filtered_king_possible_move = []
        for move in king_possible_move:
            if move not in attacked_squares:
                filtered_king_possible_move.append(move)
            else:
                continue
        return filtered_king_possible_move

def main():
    running = True
    board = Board()
    selected_square = None
    legal_moves = []
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked_position = getClickedSquare()
                if not clicked_position: continue

                if selected_square is None:
                        if clicked_position != None:
                            clicked_row, clicked_col = clicked_position[0], clicked_position[1]

                        if board.boardState[clicked_row][clicked_col] != "":
                            piece = board.boardState[clicked_row][clicked_col]
                            if piece.islower() and board.move_turn == "black" or piece.isupper() and board.move_turn == "white":
                                selected_square = [clicked_row, clicked_col]
                                legal_moves = getLegalMoves(piece, clicked_row, clicked_col, board.boardState, board.move_turn)
                            else: print("Not your Move!"); 

                        
                else:
                    start_row, start_col = selected_square[0], selected_square[1]
                    clicked_position = getClickedSquare()

                    if clicked_position != None: 
                        piece = board.boardState[start_row][start_col]
                        end_row, end_col = clicked_position[0], clicked_position[1]

                        if legal_moves == None: continue

                        if [end_row, end_col] in legal_moves:
                            board.movePiece(start_row, start_col, end_row, end_col, piece, board.boardState)
                            if piece.isupper(): board.move_turn = "black"
                            else: board.move_turn = "white"
                            
                            selected_square = None
                            
                        elif [end_row, end_col] not in legal_moves and board.boardState[end_row][end_col] == "":
                            selected_square = None

                        elif board.boardState[end_row][end_col] != "":
                            if board.boardState[end_row][end_col].islower() and board.move_turn == "black" or board.boardState[end_row][end_col].isupper() and board.move_turn == "white":
                                selected_square = [end_row, end_col]
                                piece = board.boardState[end_row][end_col]
                                legal_moves = getLegalMoves(piece, end_row, end_col, board.boardState, board.move_turn)
                            continue
                    else: 
                        continue
                
                
        screen.fill("white")
        
        board.drawSquares(screen)
        if selected_square is not None:
            board.highlightSquare(screen, selected_square)
        board.drawBoard(screen, screen_rect)
        board.drawPieces(screen)
        if selected_square is not None:
            board.highlightLegalMoves(screen, legal_moves)


        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    exit()


if __name__ == "__main__":
    main()