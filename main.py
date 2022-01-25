# Write your code here
def print_row_with_knight(x, line_number):
    row = f"{line_number}| "
    s = ""
    for i in range(1, x):
        s += "_ "
    s += "X "
    for j in range(x + 1, 9):
        s += "_ "
    s += "|"
    row += s
    print(row)


def start_game():
    line = input("Enter the knight's starting position:")
    numbers = line.split()
    if len(numbers) > 2 or len(numbers) < 2:
        print("Invalid dimensions!")
        return
    try:
        x = int(numbers[0])
        y = int(numbers[1])
        if x < 1 or x > 8 or y < 1 or y > 8:
            print("Invalid dimensions!")
            return
    except ValueError:
        print("Invalid dimensions!")
    else:
        horizontal_border = "--------------------"
        row = "| _ _ _ _ _ _ _ _ |"
        bottom_legend = "   1 2 3 4 5 6 7 8  "
        print(horizontal_border)
        for xx in range(8, 0, -1):
            if y == xx:
                print_row_with_knight(x, xx)
            else:
                row_with_line_number = f"{xx}{row}"
                print(row_with_line_number)
        print(horizontal_border)
        print(bottom_legend)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
