
def get_input_and_validate(msg, validation):
    is_valid_choice = False
    while not is_valid_choice:
        choice = input(msg)
        is_valid_choice = validation(choice)

    return choice