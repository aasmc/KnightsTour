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

## Functionality of the app
The app acts according to the following algorithm:

- Asks the player for board dimensions (must be two integers greater than 0 separated by a space). In case of incorrect input, prints "Invalid input!"
- Asks the player for initial knight position (must be two integers greater than 0 separated by a space and within bounds of the board). In case of incorrect input, prints "Invalid position!"
- Asks the player whether they want to try the puzzle or see the solution with a line Do you want to try the puzzle? (y/n):. If the user enters y, proceeds to step 4. If the user enters n, proceeds to step 5. In the case of any other input prints Invalid input! and asks the same question.
- If the player wants to try the puzzle, checks whether the board has a solution. If not, prints No solution exists! and ends the game. Otherwise, lets the player give the puzzle a try like.
- If they want to see the solution, checks whether the board has one. Prints No solution exists! in case there is none. If a solution exists, labels the starting point as 1, then labels each move with the next number until all the squares are visited.

The most intuitive method for the solution finder is to use recursion and backtracking. The recursive function checks the best possible move based on Warnsdorff's rule. The function calls itself from the new position, and continue to call itself until there are no more possible moves. If you've visited all the squares, then it is the solution you're looking for. If not, it means you've reached a dead end and need to go back to the previous square and check the next best possible move. Obviously, bigger boards take much longer to solve.
## Examples

The greater-than symbol followed by space (> ) represents the user input. Note that it's not part of the input.

### Example 1
```text
Enter your board dimensions: > 4 4
Enter the knight's starting position: > 2 2
Do you want to try the puzzle? (y/n): > n
No solution exists!
```

### Example 2
```text
Enter your board dimensions: > 4 4
Enter your knight's starting position: > 2 2
Do you want to try the puzzle? (y/n): > y
No solution exists!
```

### Example 3
```text
Enter your board dimensions: > 5 4
Enter knight's starting position: > 1 4
Do you want to try the puzzle? (y/n): > y
 ------------------
4|  X __ __ __ __ |
3| __ __  5 __ __ |
2| __  3 __ __ __ |
1| __ __ __ __ __ |
 ------------------
    1  2  3  4  5
....

Enter your next move: > 2 4
 ------------------
4|  *  X  *  *  * |
3|  *  *  *  *  * |
2|  *  *  *  *  * |
1|  *  *  *  *  * |
 ------------------
    1  2  3  4  5

What a great tour! Congratulations!
```

### Example 4
```text
Enter your board dimensions: > 4 3
Enter the knight's starting position: > 1 3
Do you want to try the puzzle? (y/n): > n

Here's the solution!
 ---------------
3|  1  4  7 10 |
2| 12  9  2  5 |
1|  3  6 11  8 |
 ---------------
    1  2  3  4
```

### Example 5
```text
Enter your board's dimensions: > 6 6
Enter the knight's starting position: > 1 6
Do you want to try the puzzle? (y/n): > n

Here's the solution!
 ---------------------
6|  1 30 27 12 15 36 |
5| 28 11  2  5 26 13 |
4| 31  4 29 14 35 16 |
3| 10 21 18  3  6 25 |
2| 19 32 23  8 17 34 |
1| 22  9 20 33 24  7 |
 ---------------------
    1  2  3  4  5  6
```