Name: APPALA SUNEEL VARRI
UTA ID: 1002111813
Programming Language: Python ,Version: 3.11.1


SOURCES AND REFERENCES:

manhattan distance - https://stackoverflow.com/questions/39759721/calculating-the-manhattan-distance-in-the-eight-puzzle

https://stackoverflow.com/questions/59839252/8-puzzle-using-depth-first-search-method

https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list

https://stackoverflow.com/questions/10607688/how-to-create-a-file-name-with-the-current-date-time-in-python

https://stackoverflow.com/questions/61739046/solving-8-puzzle-with-bfs-algorithm-using-python

https://stackoverflow.com/questions/33061805/python-8-puzzle-a-solution-path-much-longer-than-expected


CODE STRUCTURE:

'expense_8_puzzle.py' is the main program which consists the conditions for the arguments or parameters like input and output file reading,
setting dump_flag(need_logs) defaualt to false and method which needs to be implemented by importing from 'searchalgos.py' file.

'searchalgos.py' is a separate file where class created for search algorithms are defined one after another as separate functions.

In initial state, the step cost, which is the value of the tile is stored in a dictionary.

findzero function - returns the position or index value of 0(empty tile) in the matrix.

man_distance function - returns the manhattan distance by comparing the initial and goal state postion of the tile.

The below are the search algorithm functions defined and called while passing the method argument while executing

astar_search
dfs
dfs_search - calling the function call dfs by passing required parameters
bfs_search
dls_search
ids_search
ucs_search
greedy_search

Each funtion is defined with the conditions on printing the information of nodes, loading the dump file when set to true, required actions 
leading to solution.



TO RUN THE SCRIPT:

We need to copy 'expense_8_puzzle.py', 'searchalgos.py', 'start.txt', 'goal.txt' files in the same folder to execute the script.

Below is the sample command to be given in the command line(Windows Powershell) and pass the respective arguments.

python expense_8_puzzle.py start.txt goal.txt bfs true

python expense_8_puzzle.py start.txt goal.txt a* false

By default, without any parameters , A* search will be executed by default.

If dump file is to be created, we pass true and if not required to generate we pass false to the dump flag


