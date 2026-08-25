import pygame
from board import Board
from sys import exit
from legalMoves import *
from pawnPromotion import *
from aiEngine import *

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
                        res = promotePawnFunction(board, clicked_position, pawn_promote_pos, isKingInCheck, checkGameStatus)
                        if res:
                            promote_time = res[0]
                            game_over = res[1]
                            king_in_check = res[2]
                        continue

                    start_row, start_col = selected_square[0], selected_square[1]
                    clicked_position = getClickedSquare()

                    if clicked_position != None: 
                        piece = board.boardState[start_row][start_col]
                        end_row, end_col = clicked_position[0], clicked_position[1]

                        if legal_moves == None: continue

                        if [end_row, end_col] in legal_moves:

                            if board.movePiece(start_row, start_col, end_row, end_col, piece, board.boardState) == "promote_time":
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