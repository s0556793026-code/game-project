from validation import  is_in_range_and_digits

board = []
for i in range(9):
        board.append(' ')


def show_board(board):
    return f"""
[1]{board[0]}  | [2]{board[1]}  | [3]{board[2]}
------+-------+----
[4]{board[3]}  | [5]{board[4]}  | [6]{board[5]}
------+-------+----
[7]{board[6]}  | [8]{board[7]}  | [9]{board[8]}

    """

def update_board(board, player, choice=None ):
    board[int(choice) - 1] = player

def check_victory(board, player):
    WINNING_LINES = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
    ]
    for t in WINNING_LINES:
        if board[t[0]] == player and board[t[0]] == board[t[1]] and board[t[0]] == board[t[2]]:
            return True
    return False







