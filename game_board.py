POSSIBLE_DIRECTIONS = [
    "FORWARD_LEFT",
    "LEFT_FORWARD",
    "LEFT_BACK",
    "BACK_LEFT",
    "BACK_RIGHT",
    "RIGHT_BACK",
    "RIGHT_FORWARD",
    "FORWARD_RIGHT"
]


def check_pos(move, limit):
    return 1 <= move <= limit


def get_row_index_knight_pos(move, knight_x, knight_y):
    row_index = -1
    new_knight_pos = -1
    if move == "FORWARD_LEFT":
        row_index = knight_y + 2
        new_knight_pos = knight_x - 1
    elif move == "LEFT_FORWARD":
        row_index = knight_y + 1
        new_knight_pos = knight_x - 2
    elif move == "LEFT_BACK":
        row_index = knight_y - 1
        new_knight_pos = knight_x - 2
    elif move == "BACK_LEFT":
        row_index = knight_y - 2
        new_knight_pos = knight_x - 1
    elif move == "BACK_RIGHT":
        row_index = knight_y - 2
        new_knight_pos = knight_x + 1
    elif move == "RIGHT_BACK":
        row_index = knight_y - 1
        new_knight_pos = knight_x + 2
    elif move == "RIGHT_FORWARD":
        row_index = knight_y + 1
        new_knight_pos = knight_x + 2
    elif move == "FORWARD_RIGHT":
        row_index = knight_y + 2
        new_knight_pos = knight_x + 1
    return row_index, new_knight_pos


def get_possible_moves(initial_x, initial_y, max_rows, max_cols, check_cell, board=None):
    moves = []
    for direction in POSSIBLE_DIRECTIONS:
        (row_index, knight_pos) = get_row_index_knight_pos(direction, initial_x, initial_y)
        if check_pos(knight_pos, max_cols) and check_pos(row_index, max_rows):
            should_add = True
            if check_cell:
                cell_to_check = board.rows[-row_index].cells[knight_pos - 1]
                should_add = not cell_to_check.visited
            if should_add:
                moves.append(direction)
    return moves


class Board:
    num_moves = 1
    is_winner = False
    game_over = False
    knight_x = -1
    knight_y = -1

    def __init__(self, rows, border, legend, num_rows, num_cols):
        self.rows = rows
        self.header = border
        self.footer = border
        self.legend = legend
        self.num_rows = num_rows
        self.num_cols = num_cols

    def __str__(self):
        s = f"{self.header}\n"
        for row in self.rows:
            s = f"{s}{str(row)}\n"
        s = f"{s}{self.footer}\n{self.legend}"
        return s

    def show_possible_moves(self, knight_x, knight_y, should_print, should_clear):
        self.knight_y = knight_y
        self.knight_x = knight_x
        moves = get_possible_moves(knight_x, knight_y, self.num_rows, self.num_cols, False)
        for move in moves:
            row_index, new_knight_pos = get_row_index_knight_pos(move, knight_x, knight_y)
            row = self.rows[-row_index]
            cell = row.cells[new_knight_pos - 1]
            if not should_clear and not cell.visited:
                symbol = get_possible_moves(
                    new_knight_pos,
                    row_index,
                    self.num_rows,
                    self.num_cols,
                    True,
                    self)
                symbol = len(symbol) - 1  # shouldn't include previous position, so subtract 1
                cell.symbol = symbol
                cell.empty = False
            elif not cell.visited:
                cell.empty = True
        if should_print:
            print(self)

    def move_result(self):
        return GameResult(
            num_moves=self.num_moves,
            is_winner=self.is_winner,
            game_over=self.game_over
        )

    def check_move_direction(self, next_x, next_y):
        current_x = self.knight_x
        current_y = self.knight_y
        diff_x = abs(next_x - current_x)
        diff_y = abs(next_y - current_y)
        if diff_y == 1 and diff_x == 2:
            return True
        elif diff_y == 2 and diff_x == 1:
            return True
        else:
            return False

    def validate_next_moves(self, next_x, next_y):
        if not check_pos(next_x, self.num_cols):
            return False
        if not check_pos(next_y, self.num_rows):
            return False
        if not self.check_move_direction(next_x, next_y):
            return False
        row = self.rows[-next_y]
        cell = row.cells[next_x - 1]
        if cell.visited:
            return False
        if cell.symbol == "X":
            return False
        return True

    def clear_prev_possible_moves(self):
        self.show_possible_moves(self.knight_x, self.knight_y, False, True)

    def move_knight_to_pos(self, x, y):
        prev_row = self.rows[-self.knight_y]
        prev_cell = prev_row.cells[self.knight_x - 1]
        prev_cell.move_knight_from_cell()
        self.clear_prev_possible_moves()
        new_row = self.rows[-y]
        new_cell = new_row.cells[x - 1]
        new_cell.symbol = "X"
        new_cell.empty = False
        self.show_possible_moves(x, y, True, False)

    def process_next_move(self, next_x, next_y):
        self.num_moves += 1
        self.move_knight_to_pos(next_x, next_y)
        possible_moves = get_possible_moves(next_x, next_y, self.num_rows, self.num_cols, True, self)
        if len(possible_moves) == 0:
            self.game_over = True
            self.is_winner = self.num_moves == (self.num_cols * self.num_rows)
            print(self)
            return


class GameResult:

    def __init__(self, num_moves, is_winner, game_over):
        self.num_moves = num_moves
        self.is_winner = is_winner
        self.game_over = game_over
