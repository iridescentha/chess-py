import pygame
from board import Board
from sys import exit

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

def pawnMove(piece, row, col, boardState):
        two_row_after = -2 if piece == "P" else 2
        one_row_after = -1 if piece == "P" else 1
        starting_row = 6 if piece == "P" else 1
        possible_move = []

        if (col > 0 and boardState[row + one_row_after][col - 1] != "") or (col < 7 and boardState[row + one_row_after][col + 1] != ""):
            if col < 7 and boardState[row][col].isupper() ^ boardState[row + one_row_after][col + 1].isupper():
                possible_move.append([row + one_row_after, col + 1])
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


def getLegalMoves(piece, row, col, boardState):
    if piece.lower() == "p":
        possible_move = pawnMove(piece, row, col, boardState)
        print(possible_move)
        return possible_move
    else:
        return []


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
                            selected_square = [clicked_row, clicked_col]
                            piece = board.boardState[clicked_row][clicked_col]
                            legal_moves = getLegalMoves(piece, clicked_row, clicked_col, board.boardState)

                        
                else:
                    start_row, start_col = selected_square[0], selected_square[1]
                    clicked_position = getClickedSquare()

                    if clicked_position != None: 
                        piece = board.boardState[start_row][start_col]
                        end_row, end_col = clicked_position[0], clicked_position[1]

                        if legal_moves == None: continue

                        if [end_row, end_col] in legal_moves:
                            board.movePiece(start_row, start_col, end_row, end_col, piece, board.boardState)
                            selected_square = None
                            
                        elif [end_row, end_col] not in legal_moves and board.boardState[end_row][end_col] == "":
                            selected_square = None

                        elif board.boardState[end_row][end_col] != "":
                            selected_square = [end_row, end_col]
                            piece = board.boardState[end_row][end_col]
                            legal_moves = getLegalMoves(piece, end_row, end_col, board.boardState)
                            print("INVALID MOVE")
                            continue
                    else: 
                        continue
                
                
        screen.fill("white")
        
        board.drawSquares(screen)
        if selected_square is not None:
            board.highlightSquare(screen, selected_square) 
        board.drawBoard(screen, screen_rect)
        board.drawPieces(screen)


        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    exit()


if __name__ == "__main__":
    main()