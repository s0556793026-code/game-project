from logic import board, show_board, update_board, check_victory, is_tied
from validation import  is_cell_available ,is_digits, is_in_range_and_digits
from i_o import get_input_and_validate


def main():
    player = 'x'
    is_victory = False
    while not is_victory:
        print(show_board(board))
        choice = get_input_and_validate(f"Player {player}, choose a cell (1-9): ", is_in_range_and_digits)
        is_available = is_cell_available(board, int(choice))
        if is_available:
            update_board(board, player, choice)
            is_victory = check_victory(board, player)
            if is_victory:
                print(show_board(board))
                print(f"{player} von the game")
            elif is_tied(board):
                print(show_board(board))
                print("The game ended in a draw.")
                is_victory = True
            elif player == 'x':
                player = 'o'
            else:
                player = 'x'
    
                
if __name__=="__main__":
    main()