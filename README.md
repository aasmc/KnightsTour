# Knights Tour

Medium level project from Jetbrains Academy. Python Core course. 

## Description

The knight's tour problem uses a chessboard and a knight.

A standard chess board is an 8x8 square on which the chess pieces are placed. For this project, 
we will use a coordinate system (x,y) to label each square on the chessboard, where (1,1) is the 
bottom left, and (8,8) is the top right.

![Chess Grid](https://github.com/aasmc/KnightsTour/blob/master/art/grid.png?raw=true)

The knight is a chess piece. It moves in an L-shape and can jump over other pieces. It has to 
move 2 squares horizontally and 1 square vertically, or 2 squares vertically and 1 square horizontally.

![Knight's moves](https://github.com/aasmc/KnightsTour/blob/master/art/knightmove.png?raw=true)

### The rules of the knight's tour are as follows:

- The knight can start at any square.
- The knight must visit every square by moving in the L-shape.
- The knight can visit each square only once.
- The knight can finish anywhere on the board. This is called an 'open' tour of the board.
- You win if you visit every square on the board.
- You lose if you fail to visit every square only once without revisiting it.

## Stage I:
### Objectives:

- Ask the user for the knight's starting position.
- If the user input contains non-integer numbers you should print "Invalid dimensions!".
- If the user input contains more than 2 numbers you should print "Invalid dimensions!".
- If the user input numbers out of bounds of the game field you should print "Invalid dimensions!".
- Display the 8x8 chessboard with the knight in this position. You should display a frame around the board and mark the column and row numbers. You should use an underscore _ for an empty cell with a space in between them, and an X for the knight's position.

## Stage II

### Description

The traditional version of the puzzle uses a standard chessboard, but you can use a board of any size.
You can try smaller boards like 5×5, rectangular boards like 4×8, or even non-rectangular boards with some squares 
missing! Here, we will only focus on rectangular boards. Note that the board is guaranteed to have a solution if the 
smallest dimension is at least 5. Smaller boards may not have a solution.

### Objectives

In this stage, you should modify your program to do the following:

- Ask the user for the board's dimensions using X for columns and Y for rows.
- If the board's dimensions contain non-integer numbers print Invalid dimensions!.
- If the board's dimensions contain more than 2 numbers print Invalid dimensions!.
- If the board's dimensions contain negative numbers print Invalid dimensions!.
- If invalid dimensions were provided by the user, ask them for valid dimensions again after outputting Invalid dimensions!
- Once the starting position is determined, check whether it is valid as in the previous stage.
- If not, you should show the Invalid position! error message and then prompt the user for another starting position.
- Draw the board.

Use an underscore symbol _ to mark empty board squares; the number of underscore symbols for each empty square should 
be chosen according to the total number of cells: there should be as many underscores for each cell as there are digits 
in the total number of cells. For example, a 10 × 10 board has 100 spaces, so your placeholder should be ___ for an 
empty cell. If your board dimension is 6 x 5, your placeholder will be __. This will be used in later stages.

Make sure that the column numbers are exactly under the placeholders for the given column. Also, make sure your column, 
row numbers, and the knight position are aligned to the right: for example, the knight positions should be marked 
as _X or __X (instead of X_ or _X_), depending on the number of underscores for each square.

The border's length also depends on the size of the field. Use the following formula to calculate the length of the 
required border: column_n * (cell_size + 1) + 3, where column_n is the number of columns, and cell_size is the length 
of a placeholder for one cell.

## Examples

The greater-than symbol followed by space (> ) represents the user input. Note that it's not part of the input.

### Example 1
```text
Enter your board dimensions: > 6 5
Enter the knight's starting position: > 4 2
 ---------------------
5| __ __ __ __ __ __ |
4| __ __ __ __ __ __ |
3| __ __ __ __ __ __ |
2| __ __ __  X __ __ |
1| __ __ __ __ __ __ |
 ---------------------
    1  2  3  4  5  6
```

### Example 2
```text
Enter your board dimensions: > 4 4
Enter the knight's starting position: > 8 8
Invalid position!
Enter the knight's starting position: > -1 2
Invalid position!
Enter the knight's starting position: > 2 2
 ---------------
4| __ __ __ __ |
3| __ __ __ __ |
2| __  X __ __ |
1| __ __ __ __ |
 ---------------
    1  2  3  4
```

### Example 3
```text
Enter your board dimensions: > 10 10
Enter the knight's starting position: > 5 5
  -------------------------------------------
10| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 9| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 8| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 7| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 6| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 5| ___ ___ ___ ___   X ___ ___ ___ ___ ___ |
 4| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 3| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 2| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
 1| ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ |
  -------------------------------------------
      1   2   3   4   5   6   7   8   9  10
```