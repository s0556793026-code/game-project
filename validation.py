
def is_digits(choice):
    if choice.isdigit():
        return True
    print("Choice must be a positive integer")
    return False

def is_in_range_and_digits(choice):
    check_choice = is_digits(choice)
    if check_choice:
        if int(choice) in range(1, 10):
                return True
        print("Choice must be 1-9")
        return False
    return check_choice
    

def is_cell_available(board, choice):
    if board[choice - 1] == ' ':
        return True
    print("cell is not available try again")
    return False


