class Cell:
    def __init__(self, x, y, size, empty=True, visited=False, symbol=""):
        self.x = x
        self.y = y
        self.visited = visited
        self.size = size
        self.empty = empty
        self.symbol = symbol

    def move_knight_from_cell(self):
        self.visited = True
        self.symbol = "*"
        self.empty = False

    def __str__(self):
        if self.empty:
            return str("_" * self.size) + " "
        else:
            symbol_len = len(self.symbol)
            space = str(" " * (self.size - symbol_len))
            return f"{space}{self.symbol} "


