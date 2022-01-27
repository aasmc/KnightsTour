class Row:

    def __init__(self, row_num, cells, leading_space):
        self.row_num = row_num
        self.cells = cells
        self.leading_space = leading_space

    def __str__(self):
        s = f"{self.leading_space}{self.row_num}| "
        for cell in self.cells:
            s = f"{s}{str(cell)}"
        s = f"{s}|"
        return s

