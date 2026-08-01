def promotePawnFunction(board, clicked_position, pawn_promote_pos, isKingInCheck, checkGameStatus):
    pawn_row = 0 if board.move_turn == "white" else 7
    promotion_row = pawn_row
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

        return [promote_time, game_over, king_in_check]
    
    elif end_row == (pawn_row + operation1) and end_col == pawn_promote_pos[1]:
        board.boardState[promotion_row][end_col] = "N" if board.move_turn == "white" else "n"
        promote_time = False
        if board.move_turn == "white": board.move_turn = "black"
        else: board.move_turn = "white"
        king_in_check = isKingInCheck(board.boardState, board.move_turn)
        game_over = checkGameStatus(board, king_in_check)

        return [promote_time, game_over, king_in_check]
    
    if end_row == (pawn_row + operation2) and end_col == pawn_promote_pos[1]:
        board.boardState[promotion_row][end_col] = "R" if board.move_turn == "white" else "r"
        promote_time = False
        if board.move_turn == "white": board.move_turn = "black"
        else: board.move_turn = "white"
        king_in_check = isKingInCheck(board.boardState, board.move_turn)
        game_over = checkGameStatus(board, king_in_check)

        return [promote_time, game_over, king_in_check]
        
    if end_row == (pawn_row + operation3) and end_col == pawn_promote_pos[1]:
        board.boardState[promotion_row][end_col] = "B" if board.move_turn == "white" else "b"
        promote_time = False
        if board.move_turn == "white": board.move_turn = "black"
        else: board.move_turn = "white"
        king_in_check = isKingInCheck(board.boardState, board.move_turn)
        game_over = checkGameStatus(board, king_in_check)

        return [promote_time, game_over, king_in_check]