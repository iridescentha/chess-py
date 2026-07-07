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

def getLegalMoves(piece, row, col, boardState):
    if piece.lower() == "p":
        # print(row, col)
        # print(boardState)
        pass

def main():
    running = True
    board = Board()
    selected_square = None
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
                            getLegalMoves(piece, clicked_row, clicked_col, board.boardState)

                        
                else:
                    start_row, start_col = selected_square[0], selected_square[1]
                    clicked_position = getClickedSquare()

                    if clicked_position != None: 
                        end_row, end_col = clicked_position[0], clicked_position[1]
                    else: 
                        continue

                    piece = board.boardState[start_row][start_col]
                    board.movePiece(start_row, start_col, end_row, end_col, piece, board.boardState)
                    selected_square = None
                
                
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