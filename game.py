import cell
import board_row
import game_board


def validate_input_length(numbers):
    return len(numbers) == 2


def validate_numbers_are_digits(numbers):
    x_str = numbers[0]
    y_str = numbers[1]
    return x_str.isdigit() and y_str.isdigit()


def prompt_user_for_dimensions(message, is_knight_position, board_x=-1, board_y=-1):
    """Prompts user for dimensions of the chess board or knight position depending on flag
    is_knight_position. Checks the input for correctness. If input is incorrect, repeats
    the prompt. Dimensions must be positive integers. Returns a tuple of (x, y) dimensions."""
    error_message = "Invalid position!" \
        if is_knight_position \
        else "Invalid dimensions!"
    while True:
        numbers = input(message).split()
        if not validate_input_length(numbers):
            print(error_message)
            continue
        if not validate_numbers_are_digits(numbers):
            print(error_message)
            continue
        try:
            x = int(numbers[0])
            y = int(numbers[1])
            if x < 1 or y < 1:
                print(error_message)
                continue
            else:
                if is_knight_position:
                    if x < 1 or y < 1 or x > board_x or y > board_y:
                        print(error_message)
                        continue
                    else:
                        return (x, y)
                return (x, y)
        except ValueError:
            print(error_message)
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


def get_cells(row_number, number_of_cols, cell_size, knight_pos):
    cells = []
    for i in range(1, number_of_cols + 1):
        empty = True
        symbol = ""
        if knight_pos == i:
            empty = False
            symbol = "X"
        c = cell.Cell(
            x=i,
            y=row_number,
            size=cell_size,
            empty=empty,
            visited=False,
            symbol=symbol)
        cells.append(c)
    return cells


def get_row(
        row_number,
        cell_size,
        number_of_columns,
        number_of_rows,
        knight_position=-1):
    leading_space = get_row_leading_space(number_of_rows, row_number)
    cells = get_cells(row_number, number_of_columns, cell_size, knight_position)
    r = board_row.Row(
        row_num=row_number,
        cells=cells,
        leading_space=leading_space
    )
    return r


def get_rows(number_of_rows, number_of_cols, cell_size, knight_x, knight_y):
    rows = []
    for i in range(number_of_rows, 0, -1):
        row = get_row(i, cell_size, number_of_cols, number_of_rows, knight_x) \
            if knight_y == i \
            else get_row(i, cell_size, number_of_cols, number_of_rows)
        rows.append(row)
    return rows


def get_board(board_x, board_y, knight_x, knight_y):
    cell_size = calculate_cell_size(board_x, board_y)
    border_width = calculate_border_width(cell_size, board_x)
    border = get_border(border_width, board_y)
    bottom_legend = get_bottom_legend(board_x, cell_size)

    rows = get_rows(board_y, board_x, cell_size, knight_x, knight_y)
    board = game_board.Board(
        rows=rows,
        border=border,
        legend=bottom_legend,
        num_rows=board_y,
        num_cols=board_x
    )
    return board


def print_board(board):
    print(board)


def prompt_user_for_moves(board):
    prompt_message = "Enter your next move:"
    move_result = board.move_result()
    while not move_result.game_over:
        next_moves = input(prompt_message).split()
        if not validate_input_length(next_moves):
            prompt_message = "Invalid move! Enter your next move:"
            continue
        if not validate_numbers_are_digits(next_moves):
            prompt_message = "Invalid move! Enter your next move:"
            continue
        next_x, next_y = map(int, next_moves)
        if not board.validate_next_moves(next_x, next_y):
            prompt_message = "Invalid move! Enter your next move:"
            continue
        board.process_next_move(next_x, next_y)
        move_result = board.move_result()
    if move_result.is_winner:
        print("What a great tour! Congratulations!")
    else:
        message = f"No more possible moves!\nYour knight visited {move_result.num_moves} squares!"
        print(message)


def prompt_user_for_puzzle():
    while True:
        decision = input("Do you want to try the puzzle? (y/n):")
        if decision == "y":
            return True
        elif decision == "n":
            return False
        else:
            print("Invalid input!")


def play_game():
    board_dimensions = prompt_user_for_dimensions("Enter your board dimensions:",
                                                  False)

    num_rows = board_dimensions[0]
    num_cols = board_dimensions[1]

    knight_pos = prompt_user_for_dimensions(
        "Enter the knight's starting position:",
        True,
        num_rows,
        num_cols)

    x = knight_pos[0]
    y = knight_pos[1]

    board = get_board(
        num_rows,
        num_cols,
        x,
        y)

    if prompt_user_for_puzzle():
        if board.has_solution(x, y):
            board.show_possible_moves(x, y, True)
            prompt_user_for_moves(board=board)
        else:
            print("No solution exists!")
    else:
        if board.solve_on_board(x, y, 1):
            print("\nHere's the solution!")
            board.show_solution()
        else:
            print("No solution exists!")
