allowed_x_moves = [-1, -2, -2, -1, 1, 2, 2, 1]
allowed_y_moves = [2, 1, -1, -2, -2, -1, 1, 2]


def check_pos(move, limit):
    return 1 <= move <= limit


def get_row_index_knight_pos(index, knight_x, knight_y):
    new_x = knight_x + allowed_x_moves[index]
    new_y = knight_y + allowed_y_moves[index]
    return new_y, new_x


def get_possible_moves(initial_x, initial_y, max_rows, max_cols, check_cell, board=None):
    moves = []
    for i in range(8):
        (row_index, knight_pos) = get_row_index_knight_pos(i, initial_x, initial_y)
        if check_pos(knight_pos, max_cols) and check_pos(row_index, max_rows):
            should_add = True
            if check_cell:
                cell_to_check = board.rows[-row_index].cells[knight_pos - 1]
                should_add = not cell_to_check.visited
            if should_add:
                moves.append(i)
    return moves


class Board:
    num_moves = 1
    is_winner = False
    game_over = False
    knight_x = -1
    knight_y = -1
    knight_possible_moves = []

    def __init__(self, rows, border, legend, num_rows, num_cols):
        self.rows = rows
        self.header = border
        self.footer = border
        self.legend = legend
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.max_moves = num_rows * num_cols

    def __str__(self):
        s = f"{self.header}\n"
        for row in self.rows:
            s = f"{s}{str(row)}\n"
        s = f"{s}{self.footer}\n{self.legend}"
        return s

    def show_possible_moves(self, knight_x, knight_y, should_print):
        self.knight_y = knight_y
        self.knight_x = knight_x
        self.knight_possible_moves = get_possible_moves(knight_x, knight_y, self.num_rows, self.num_cols, False)
        for move in self.knight_possible_moves:
            cell, new_knight_pos, row_index = self.get_row_cell_for_move(knight_x, knight_y, move)
            if not cell.visited:
                symbol = get_possible_moves(
                    new_knight_pos,
                    row_index,
                    self.num_rows,
                    self.num_cols,
                    True,
                    self)
                symbol = len(symbol) - 1  # shouldn't include previous position, so subtract 1
                cell.symbol = str(symbol)
                cell.empty = False
        if should_print:
            print(self)

    def get_row_cell_for_move(self, knight_x, knight_y, move):
        row_index, new_knight_pos = get_row_index_knight_pos(move, knight_x, knight_y)
        row = self.rows[-row_index]
        cell = row.cells[new_knight_pos - 1]
        return cell, new_knight_pos, row_index

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
        for move in self.knight_possible_moves:
            cell, new_knight_pos, row_index = self.get_row_cell_for_move(self.knight_x, self.knight_y, move)
            if not cell.visited:
                cell.empty = True

    def move_knight_to_pos(self, x, y):
        self.move_knight_from_current_cell()
        new_row = self.rows[-y]
        new_cell = new_row.cells[x - 1]
        new_cell.symbol = "X"
        new_cell.empty = False
        self.show_possible_moves(x, y, True)

    def move_knight_from_current_cell(self):
        prev_row = self.rows[-self.knight_y]
        prev_cell = prev_row.cells[self.knight_x - 1]
        prev_cell.move_knight_from_cell()
        self.clear_prev_possible_moves()

    def process_next_move(self, next_x, next_y):
        self.num_moves += 1
        self.move_knight_to_pos(next_x, next_y)
        possible_moves = get_possible_moves(next_x, next_y, self.num_rows, self.num_cols, True, self)
        if len(possible_moves) == 0:
            self.game_over = True
            self.is_winner = self.num_moves == self.max_moves
            print(self)
            return

    def has_solution(self, knight_x, knight_y):
        board = [[-1 for i in range(self.num_cols)] for i in range(self.num_rows)]
        board[knight_y - 1][knight_x - 1] = 0
        return self.check_solution(knight_x - 1, knight_y - 1, self.num_moves, board)

    def check_solution(self, knight_x, knight_y, num_moves, board):
        if num_moves == self.max_moves:
            return True
        for i in range(8):
            next_x = knight_x + allowed_x_moves[i]
            next_y = knight_y + allowed_y_moves[i]
            if self.is_auto_move_allowed(next_x, next_y, board):
                board[next_y][next_x] = num_moves
                if self.check_solution(next_x, next_y, num_moves + 1, board):
                    return True
                else:
                    board[next_y][next_x] = -1
        return False

    def is_auto_move_allowed(self, next_x, next_y, board):
        return 0 <= next_x < self.num_cols \
               and 0 <= next_y < self.num_rows \
               and board[next_y][next_x] == -1

    def show_solution(self, knight_x, knight_y):
        self.solve_on_board(knight_x, knight_y, self.num_moves)
        print(self)

    def solve_on_board(self, knight_x, knight_y, num_moves):
        if num_moves == self.max_moves:
            self.make_auto_move(knight_x, knight_y, num_moves)
            return True
        for i in range(8):
            next_x = knight_x + allowed_x_moves[i]
            next_y = knight_y + allowed_y_moves[i]
            if self.check_auto_move_correct(next_x, next_y):
                self.make_auto_move(knight_x, knight_y, num_moves)
                if self.solve_on_board(next_x, next_y, num_moves + 1):
                    return True
                else:
                    self.backtrack(next_x, next_y)
        return False

    def backtrack(self, knight_x, knight_y):
        row = self.rows[-knight_y]
        cell = row.cells[knight_x - 1]
        cell.empty = True

    def make_auto_move(self, knight_x, knight_y, num_moves):
        row = self.rows[-knight_y]
        cell = row.cells[knight_x - 1]
        cell.empty = False
        cell.symbol = str(num_moves)

    def is_within_board(self, next_x, next_y):
        return 1 <= next_x <= self.num_cols and 1 <= next_y <= self.num_rows

    def check_auto_move_correct(self, next_x, next_y):
        within_board = self.is_within_board(next_x, next_y)
        if not within_board:
            return False
        row = self.rows[-next_y]
        cell = row.cells[next_x - 1]
        return cell.empty


class GameResult:

    def __init__(self, num_moves, is_winner, game_over):
        self.num_moves = num_moves
        self.is_winner = is_winner
        self.game_over = game_over
