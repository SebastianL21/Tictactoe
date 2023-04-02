"""
Tic Tac Toe Player
"""

import math
import copy

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
    x_counts = sum(row.count(X) for row in board)
    o_counts = sum(row.count(O) for row in board)
    if x_counts <= o_counts:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return [(i, j) for i, row in enumerate(board) for j, element in enumerate(row) if element is None]


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not a valid move")
    new_board = copy.deepcopy(board)
    i, j = action
    if player(board) == X:
        new_board[i][j] = X
    else:
        new_board[i][j] = O
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Checking for winner in rows
    for row in board:
        if len(set(row)) == 1:
            return row[0]

    # Checking for winner in diagonals
    if len(set([board[i][i] for i, _ in enumerate(board)])) == 1:
        return board[0][0]
    if len(set([board[2-i][i] for i, _ in enumerate(board)])) == 1:
        return board[2][0]

    # Checking for winner in columns. Board is transposed first
    for row in list(map(list, zip(*board))):
        if len(set(row)) == 1:
            return row[0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) is True:
        return None
    if player(board) == X:
        return maximize(board, -math.inf, math.inf)[0]
    else:
        return minimize(board, math.inf, -math.inf)[0]


def maximize(board, alpha, beta):
    if terminal(board) is True:
        return (None, utility(board))
    best_val = (None, -math.inf)
    moves = actions(board)
    for action in moves:
        new_board = result(board, action)
        score = (action, minimize(new_board, alpha, beta)[1])
        if best_val[1] < score[1]:
            best_val = score
        alpha = max(alpha, best_val[1])
        if beta <= alpha:
            break
    return best_val


def minimize(board, alpha, beta):
    if terminal(board) is True:
        return (None, utility(board))
    best_val = (None, math.inf)
    moves = actions(board)
    for action in moves:
        new_board = result(board, action)
        score = (action, maximize(new_board, alpha, beta)[1])
        if best_val[1] > score[1]:
            best_val = score
        beta = min(beta, best_val[1])
        if beta <= alpha:
            break
    return best_val
