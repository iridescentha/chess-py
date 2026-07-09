import pygame

piece_width = 80
piece_height = 80
white_pawn = pygame.transform.scale(pygame.image.load("assets/white_pawn.png"), (piece_width, piece_height))
white_rook = pygame.transform.scale(pygame.image.load("assets/white_rook.png"), (piece_width, piece_height))
white_knight = pygame.transform.scale(pygame.image.load("assets/white_knight.png"), (piece_width, piece_height))
white_bishop = pygame.transform.scale(pygame.image.load("assets/white_bishop.png"), (piece_width, piece_height))
white_queen = pygame.transform.scale(pygame.image.load("assets/white_queen.png"), (piece_width, piece_height))
white_king = pygame.transform.scale(pygame.image.load("assets/white_king.png"), (piece_width, piece_height))

black_pawn = pygame.transform.scale(pygame.image.load("assets/black_pawn.png"), (piece_width, piece_height))
black_rook = pygame.transform.scale(pygame.image.load("assets/black_rook.png"), (piece_width, piece_height))
black_knight = pygame.transform.scale(pygame.image.load("assets/black_knight.png"), (piece_width, piece_height))
black_bishop = pygame.transform.scale(pygame.image.load("assets/black_bishop.png"), (piece_width, piece_height))
black_queen = pygame.transform.scale(pygame.image.load("assets/black_queen.png"), (piece_width, piece_height))
black_king = pygame.transform.scale(pygame.image.load("assets/black_king.png"), (piece_width, piece_height))

class Board:
    boardState = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["",  "",  "",  "",  "",  "",  "",  ""],
    ["",  "",  "",  "",  "",  "",  "",  ""],
    ["",  "",  "",  "",  "",  "",  "",  ""],
    ["",  "",  "",  "",  "",  "",  "",  ""],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ]

    square_size = 80
    circle_size = 18

    board_left = 320
    board_top = 40
    board_size = 640

    piece_image = {
        "P": white_pawn,
        "R": white_rook,
        "N": white_knight,
        "B": white_bishop,
        "Q": white_queen,
        "K": white_king,

        "p": black_pawn,
        "r": black_rook,
        "n": black_knight,
        "b": black_bishop,
        "q": black_queen,
        "k": black_king,
    }

    def __init__(self):
        pass

    def drawBoard(self, screen, screen_rect):
        rect = pygame.Rect(0, 0, self.board_size, self.board_size)
        rect.center = screen_rect.center
        pygame.draw.rect(screen, "black", rect, 5)

    def drawSquares(self, screen,):
        for row in range(8):
            y_pos = self.board_top + (row * self.square_size)
            for column in range(8):
                    if row % 2 and column % 2:
                        x_pos2 = self.board_left + (column * self.square_size)
                        pygame.draw.rect(screen, "burlywood1", pygame.Rect(x_pos2, y_pos,self.square_size, self.square_size))
                    elif row % 2 or column % 2:
                        x_pos = self.board_left + (column * self.square_size)
                        pygame.draw.rect(screen, "brown4", pygame.Rect(x_pos, y_pos, self.square_size, self.square_size))
                    else:
                        x_pos2 = self.board_left + (column * self.square_size)
                        pygame.draw.rect(screen, "burlywood1", pygame.Rect(x_pos2, y_pos, self.square_size, self.square_size))

    def drawPieceCentered(self, image, row, col, screen):
        center_square_x = self.board_left + (row * self.square_size + (self.square_size // 2))
        center_square_y = self.board_top + (col * self.square_size + (self.square_size // 2))
        rect = image.get_rect()
        rect.center = (center_square_x, center_square_y)
        screen.blit(image, rect)
        

    def drawPieces(self, screen):
        for row in range(8):
            for col in range(8):
                piece = self.boardState[col][row]
                if piece != "":
                    image_piece = self.piece_image[piece]
                    self.drawPieceCentered(image_piece, row, col, screen)

    def movePiece(self, current_row, current_col, end_row, end_col, piece, boardState):
        boardState[current_row][current_col] = ""
        if piece.lower() == "p" and end_row == 0 or end_row == 7:
            boardState[end_row][end_col] = "Q" if piece == "P" else "q"
        else:
            boardState[end_row][end_col] = piece

    def highlightSquare(self, screen, rowAndCol: list[int]):

        y = self.board_top + (rowAndCol[0] * self.square_size)
        x = self.board_left + (rowAndCol[1] * self.square_size)
        pygame.draw.rect(screen, "darkolivegreen1", pygame.Rect(x, y, self.square_size, self.square_size))

    def highlightLegalMoves(self, screen, legal_moves):
        if legal_moves is None: return
        for square_pos in legal_moves:
            y = self.board_top + (square_pos[0] * self.square_size + (self.square_size // 2))
            x = self.board_left + (square_pos[1] * self.square_size + (self.square_size // 2))
            pygame.draw.circle(screen, "gray36", (x, y), self.circle_size)