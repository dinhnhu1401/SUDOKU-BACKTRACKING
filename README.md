# SUDOKU - BACK TRACKING - Python3


SUDOKU is a logic-based, combinatorial number-placement puzzle. 

The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") 
contain all of the digits from 1 to 9. 

The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution.

You can search more about the rules on the internet, even you can try a little at game online website.

[Play SODUKU Now!](https://www.sudoku-solutions.com/)


#### Clone my repository
```python3
git clone https://github.com/dinhnhu1401/SUDOKU-BACKTRACKING.git
cd SUDOKU-BACKTRACKING
python3 sudoku.py
```

#### A quick  on the Online Python Compiler
Visit [![Run on Repl.it](https://repl.it/badge/github/dinhnhu1401/SUDOKU-BACKTRACKING)](https://repl.it/github/dinhnhu1401/SUDOKU-BACKTRACKING) and enjoy

# Mission
Implement a **program** to solve the Sudoku.


### Input:
The board => user fills  in

### End condition
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



(continue)



 
# Solution and related skills:

## Solution:


## Ralated skills:

- Use **collections** import *defaultdict*
- Use **itertools**
  
# Coding Journey

| Day        | Duration   |Describe Stuck or A done feature      |Cause or Result       |
|------------|------------|--------------------------------------|----------------------|
| 23/12/2019 | 3h         | Thinking and researching             | ....                 |
| 24/12/2019 | 2h         | Write README. md                     | Basic structure      |
| 23/12/2019 | 3h         | ....                                 | ....                 |
| 23/12/2019 | 3h         | ....                                 | ....                 |


@TECHWITHTIM