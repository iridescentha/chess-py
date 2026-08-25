from legalMoves import *

def chooseBestMove():
    pass

def applyMove(board, move):
    board_copy = board.copy()

def evaluate():
    pass

def getAllLegalMoves(boardState, move_turn):
    legal_pieces = "prnbqk" if move_turn == "black" else "PRNBQK"
    legal_moves = []

    for i in range(8):
        for j in range(8):

            if boardState[i][j] in legal_pieces:
                legal_moves.append(getLegalMoves(boardState[i][j], i, j, boardState))

    print(legal_moves)