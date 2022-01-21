# Knights Tour

Medium level project from Jetbrains Academy. Python Core course. 

## Description

The knight's tour problem uses a chessboard and a knight.

A standard chess board is an 8x8 square on which the chess pieces are placed. For this project, 
we will use a coordinate system (x,y) to label each square on the chessboard, where (1,1) is the 
bottom left, and (8,8) is the top right.

The knight is a chess piece. It moves in an L-shape and can jump over other pieces. It has to 
move 2 squares horizontally and 1 square vertically, or 2 squares vertically and 1 square horizontally.

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

