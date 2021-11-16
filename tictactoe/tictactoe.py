"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # raise NotImplementedError
    initial_state = True
    x_count = 0
    o_count = 0
    for row in board:
        if not all(list((map(lambda i : i == None, row )))):
            initial_state = False
            
        for played in row:
            if played == X:
                x_count += 1
            elif played == O:
                o_count += 1
    if initial_state:
        print('initial')
        return X
    elif terminal(board):
        return None
    
    return O if o_count < x_count else X
    



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_actions = []
    for i in range(len(board)):
        row = board[i]
        for j in range(len(row)):
            if board[i][j] is EMPTY:
                available_actions.append((i, j))
    
    if terminal(board):
        return None
    return available_actions
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    play = player(board)
    import copy
    
    row = action[0]
    col = action[1]
    try:
        if board[row][col] == EMPTY:
            new_board = copy.deepcopy(board)
            new_board[row][col] = play
            return new_board
        elif board[row][col] == X or board[row][col] == O:
            raise Exception("Cell already occupied")
    except:
        raise Exception("Invalid cell")
        
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    def determinant(board):
        for row in board:
            first_player = row[0] or None
            
            if first_player is not None:
                won = all(list(map(lambda player: first_player == player, row)))
                if won:
                    
                    return first_player
        
        return None
    
    def row_winner():
        return determinant(board)
    
    def col_winner():
        row = board[0]
        all_cols = []
        for row_idx in range(len(row)):
            col = []
            for row_data in board:
                col.append(row_data[row_idx])
            all_cols.append(col)
            
        return determinant(all_cols)
    
    def diagonal_winner():
        diags = []
        diag_0_first = board[0][0]
        center = board[1][1]
        diagonal_0_last = board[2][2]
        first_diagonal = [diag_0_first, center, diagonal_0_last]
        diags.append(first_diagonal)
        
        diag_0_first = board[0][2]
        center = board[1][1]
        diagonal_0_last = board[2][0]
        first_diagonal = [diag_0_first, center, diagonal_0_last]
        diags.append(first_diagonal)
        
        return determinant(diags)
        
            

    return row_winner() or col_winner() or diagonal_winner()
    
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    
    board_filled = True
    for row in board:
        for col in row:
            if col is EMPTY:
                board_filled = False
    
    if board_filled:
        return True

    return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # raise NotImplementedError
    if terminal(board):
        won_by = winner(board)
        if won_by == X:
            return 1
        elif won_by == O:
            return -1
        return 0
    return None
            


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # raise NotImplementedError
    if terminal(board):
        return None
    
    def max_value(board):
        v = float('-inf')

        if terminal(board):
            return utility(board)
        
        for action in actions(board):
            print(result(board, action))
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        v = float("inf")

        if terminal(board):
            return utility(board)
        for action in actions(board):
            print(result(board, action))
            
            v = min(v, max_value(result(board, action)))
        return v
    
    all_actions = actions(board)
    actions_and_utility = []
    if player(board) == X:
        for action in all_actions:
            # new_board = result(board, action, player(board))
            resulting_utility = max_value(board)
            actions_and_utility.append([action, resulting_utility])
        
        print(actions_and_utility)
        for move in actions_and_utility:
            if move[1] == 1:
                return move[0], actions_and_utility
        for move in actions_and_utility:
            if move[1] == 0:
                return move[0], actions_and_utility
        for move in actions_and_utility:
            if move[1] == -1:
                return move[0], actions_and_utility
    elif player(board) == O:
        for action in all_actions:
            # new_board = result(board, action, player(board))
            resulting_utility = min_value(board)
            actions_and_utility.append([action, resulting_utility])
        for move in actions_and_utility:
            if move[1] == -1:
                return move[0]
        for move in actions_and_utility:
            if move[1] == 0:
                return move[0]
        for move in actions_and_utility:
            if move[1] == 1:
                return move[0]
            
        
