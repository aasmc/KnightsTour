def print_error_message(message):
    print(message)


def prompt_user_for_dimensions(message, is_knight_position, board_x=-1, board_y=-1):
    """Prompts user for dimensions of the chess board or knight position depending on flag
    is_knight_position. Checks the input for correctness. If input is incorrect, repeats
    the prompt. Dimensions must be positive integers. Returns a tuple of (x, y) dimensions."""
    error_message = "Invalid position!" if is_knight_position else "Invalid dimensions!"
    while True:
        numbers = input(message).split()
        if len(numbers) > 2 or len(numbers) < 2:
            print_error_message(error_message)
            continue
        x_str = numbers[0]
        y_str = numbers[1]
        if not x_str.isdigit() or not y_str.isdigit():
            print_error_message(error_message)
            continue
        try:
            x = int(x_str)
            y = int(y_str)
            if x < 0 or y < 0:
                print_error_message(error_message)
                continue
            else:
                if is_knight_position:
                    if x < 1 or y < 1 or x > board_x or y > board_y:
                        print_error_message(error_message)
                        continue
                    else:
                        return (x, y)
                return (x, y)
        except ValueError:
            print_error_message(error_message)
            continue


def calculate_cell_size(board_x, board_y):
    total = board_x * board_y
    count = 1
    while total >= 10:
        total = total // 10
        count += 1
    return count


def calculate_border_width(cell_size, number_of_columns):
    return number_of_columns * (cell_size + 1) + 3


def get_border(border_width, max_row):
    border = str(" " * len(str(max_row)))
    for i in range(0, border_width):
        border = f"{border}-"
    return border


def get_bottom_legend(number_of_columns, cell_size):
    legend = "   "
    for i in range(1, number_of_columns + 1):
        space = cell_size - 1
        space_str = str(" " * space)
        legend = f"{legend}{space_str}{i} "
    legend = f"{legend} "
    return legend


def get_row_leading_space(number_of_rows, row_number):
    row_num_max_space = str(number_of_rows)
    row_num_str = str(row_number)
    diff = len(row_num_max_space) - len(row_num_str)
    return str(" " * diff)


def get_row(row_number, cell_size, number_of_columns, number_of_rows, knight_position=-1):
    leading_space = get_row_leading_space(number_of_rows, row_number)
    row = f"{leading_space}{row_number}| "
    for i in range(1, number_of_columns + 1):
        cell = str(" " * (cell_size - 1)) + "X " if i == knight_position else str("_" * cell_size) + " "
        row = f"{row}{cell}"
    row = f"{row}|"
    return row


def get_board(board_x, board_y, knight_x, knight_y):
    cell_size = calculate_cell_size(board_x, board_y)
    border_width = calculate_border_width(cell_size, board_x)
    border = get_border(border_width, board_y)
    bottom_legend = get_bottom_legend(board_x, cell_size)

    game_board = [border]
    for i in range(board_y, 0, -1):
        row = get_row(i, cell_size, board_x, board_y, knight_x)\
            if knight_y == i \
            else get_row(i, cell_size, board_x, board_y)
        game_board.append(row)
    game_board.append(border)
    game_board.append(bottom_legend)
    return game_board


def print_board(game_board):
    for row in game_board:
        print(row)


def play_game():
    board_dimensions = prompt_user_for_dimensions("Enter your board dimensions:", False)
    knight_pos = prompt_user_for_dimensions(
        "Enter the knight's starting position:",
        True,
        board_dimensions[0],
        board_dimensions[1])
    board = get_board(board_dimensions[0], board_dimensions[1], knight_pos[0], knight_pos[1])
    print_board(board)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    play_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
