# SUDOKU - BACK TRACKING - Python3


SUDOKU is a logic-based, combinatorial number-placement puzzle. 

The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") 
contain all of the digits from 1 to 9. 

The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution.

You can search more about the rules on the internet, even you can try a little at game online website.

The link below will help you to generate the valid board and give you its answer.

[Play SODUKU Now!](https://www.sudoku-solutions.com/)


#### Clone my repository
```python3
git clone https://github.com/dinhnhu1401/SUDOKU-BACKTRACKING.git
cd SUDOKU-BACKTRACKING
python3 sudoku.py
```

#### A quick View on the Online Python Compiler
Visit [![Run on Repl.it](https://repl.it/badge/github/dinhnhu1401/SUDOKU-BACKTRACKING)](https://repl.it/github/dinhnhu1401/SUDOKU-BACKTRACKING) and enjoy

# Mission
Implement a **program** to solve the Sudoku.


### Input:
The program will ask you if you want to set up your own board to make sure the transparency.

Press **0**: You set up by yourself.

And then the program validate your board:
   - 9 lines
   - 9 numbers each line
   - right syntax
   - unique board 

Press **1**: The program will use the default board.


### Output:
Return the solutions of the given board. 



# Analysis: Data structures and Functions


- Use **list** in **list** to store a board.

    First, we need a function to display the board. 
    
    "0" - the unknown cell. 
    
    "1-->9" - the fixed cell.
    
    It's going turn a matrix like this:
```
[[0, 0, 0, 5, 3, 4, 0, 0, 8],
[0, 0, 3, 6, 0, 0, 0, 5, 0],
[5, 0, 0, 0, 1, 0, 0, 0, 4],
[0, 7, 0, 0, 0, 0, 5, 2, 0],
[9, 0, 0, 0, 2, 0, 0, 0, 1],
[3, 0, 2, 0, 0, 0, 0, 8, 0],
[8, 0, 0, 0, 6, 0, 0, 0, 5],
[0, 3, 5, 0, 0, 8, 7, 0, 0],
[7, 0, 0, 1, 5, 0, 8, 0, 3]]
```
Into this:
```
0 0 0 | 5 3 4 | 0 0 8
0 0 3 | 6 0 0 | 0 5 0
5 0 0 | 0 1 0 | 0 0 4
----------------------
0 7 0 | 0 0 0 | 5 2 0
9 0 0 | 0 2 0 | 0 0 1
3 0 2 | 0 0 0 | 0 8 0
----------------------
8 0 0 | 0 6 0 | 0 0 5
0 3 5 | 0 0 8 | 7 0 0
7 0 0 | 1 5 0 | 8 0 3

```
- We need functions:
    - To validate and print the board.
    - To pick a number for a cell (increasing). 
    - To validate each cell with its vertical, horizontal, diagonal direction)

 
# Solution and related skills/knowledge:

## Solution:

- Browse for an empty cell.

- If the empty cell don't exist => return True (Finish solving)
    
   else => note this cell
 
- Pick a number from 1 to 9 into this cell and validate it.
    - If it is the valid cell => assign the number into the current position of the board.
    - If **the problem is solved** (Repeat recursively all the steps above)=> return True (Finish solving)
    - Assign the current position by zero (back-track step)
- Return False (break out the program and can't find a solution)

## Related skills/knowledge:

- **Recursive**
    
    `In recursion function calls itself until reaches a base case.` - stackoverflow.com
    
- **Back-tracking idea** (like DFS when searching in tree)
    `In back-tracking you use recursion in order to explore all the possibilities until you get the best result for the problem` - - stackoverflow.com

```
Recursion is an algorithm structure, backtracking is an algorithm idea.

Back-tracking is an approach to solve certain kind of problems.
Common examples would be : N-Queens, Sudoku etc.
Recursion is used to implement an algorithm that back-tracks.
```
# Coding Journey

| Day        | Duration   |Describe Stuck or A done feature      |Cause or Result       |
|------------|------------|--------------------------------------|----------------------|
| 23/12/2019 | 3h         | Thinking and researching             | ....                 |
| 24/12/2019 | ...        | Write README.md and coding           | Basic structure      |
| 25/12/2019 | 3h         | Write func allow user to fill the board           | Func: give  board                |
| 26/12/2019 | 3h         | Complete the validate of the given board by user. | Func: check board and check line |
| 26/12/2019 | 2h         | add solutions and knowledge into README | Done - Ver 1.0.0

@TechWithTim