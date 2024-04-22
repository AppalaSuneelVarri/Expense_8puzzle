# Expense_8puzzle

Problem Statement: Solving Sliding Puzzle using Various Search Algorithms

Objective:
Implement various search algorithms to solve the sliding puzzle problem, specifically the 8-puzzle problem, which involves arranging tiles numbered 1 through 8 on a 3x3 grid with one empty space.

Description:
The sliding puzzle, also known as the 8-puzzle, is a classic puzzle game. It consists of a 3x3 grid with eight numbered tiles and one empty space. The objective is to arrange the tiles in a specific order by sliding them into the empty space. The tiles can only be moved into the empty space, either horizontally or vertically, and the empty space can only be filled by adjacent tiles.

Input:

The initial state of the puzzle, provided as a 3x3 grid with numbers representing the tiles. The empty space is denoted by the number 0.
The goal state of the puzzle, also provided as a 3x3 grid with numbers representing the desired arrangement of tiles.
Output:

If a solution is found, output the sequence of moves required to transform the initial state into the goal state.
If no solution is found, output "NO Solution found".
Algorithms to Implement:

A* (A-star) Search Algorithm
Depth-First Search (DFS)
Breadth-First Search (BFS)
Depth-Limited Search (DLS)
Iterative Deepening Search (IDS)
Uniform Cost Search (UCS)
Greedy Best-First Search Algorithm
Implementation Details:

The program should accept command-line arguments specifying the input file containing the initial state, the output file to write the solution or "NO Solution found," and optional arguments for selecting the search algorithm and enabling/disabling logging.
The search algorithms should be implemented as methods of a Searchalgo class, which should handle the logic for each algorithm.
•	Implemented various search algorithms like A* with Manhattan distance heuristic, DFS, BFS, DLS, IDS, and UCS to solve the 8-puzzle problem. 
•	The goal is to find the most efficient sequence of moves to reach the goal state from the starting configuration, considering factors like optimality, memory usage, and computational resources. 
•	The program returns the solution path or "None" if no solution exists, alongside statistics (nodes expanded, generated, fringe size). Additionally, it can log detailed information for further analysis and debugging.
The program should log various information, including nodes popped, nodes expanded, nodes generated, maximum fringe size, solution depth, and cost.
Instructions for Running the Program:

Provide the input file containing the initial state of the puzzle.
Provide the output file where the solution or "NO Solution found" will be written.
Optionally, specify the search algorithm to use and whether logging is needed.
