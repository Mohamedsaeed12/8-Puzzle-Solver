🔢 8-Puzzle Solver using A* Search with Manhattan Distance
Author: Mohamed Saeed
Date: February 14, 2025
🧠 Purpose
This program implements an A* informed search algorithm using the Manhattan Distance heuristic to solve a 3×3 sliding tile puzzle (commonly known as the 8-puzzle).

It demonstrates:

Heuristic-based state-space search

Node expansion and cost calculation

Solution reconstruction and step tracking

📌 Problem Definition
The goal state of the puzzle is:

csharp
Copy
Edit
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]   ← 0 represents the empty space
The initial state (hardcoded in the script) is:

csharp
Copy
Edit
[1, 3, 4]
[7, 0, 2]
[5, 8, 6]
💡 Algorithm Overview
This project uses the A* search algorithm, which evaluates nodes using:

Copy
Edit
f(n) = g(n) + h(n)
Where:

g(n) is the cost from the start node to current node (depth)

h(n) is the Manhattan Distance of all tiles from their correct positions

f(n) is the total estimated cost to reach the goal

🔍 Features
✅ Priority queue for node expansion using Python’s heapq

✅ Custom Node class for storing state, cost, move, and path

✅ Tracks and prints every state explored

✅ Reconstructs the full move sequence from initial to goal state

✅ Uses pandas DataFrame for clean solution visualization

📦 File Structure
a_star_8puzzle.py: Main solver using A* with Manhattan Distance

No external inputs required — puzzle state is hardcoded

▶️ How to Run
Ensure you have Python 3 installed

Install required package:

bash
Copy
Edit
pip install pandas
Run the script:

bash
Copy
Edit
python a_star_8puzzle.py
📈 Sample Output (Truncated)
python-repl
Copy
Edit
Expanding Node: [1, 3, 4, 7, 0, 2, 5, 8, 6]
f(n) = g(n) + h(n) -> 7 = 0 + 7
===============================================================
...
Solution found!

A* Algorithm - State Exploration:
   Puzzle State                 Move
0  [1, 3, 4, 7, 0, 2, 5, 8, 6]  Start
1  [1, 3, 4, 0, 7, 2, 5, 8, 6]  Left
...

Solution Sequence:
0: Move Start  
1: Move Left  
2: Move Down  
...
✏️ Greedy Search (Write-up)
If this algorithm used Greedy Best-First Search, we would only use the heuristic function h(n), and ignore the path cost g(n).
This would change f(n) to:

Copy
Edit
f(n) = h(n)
Effect:
Search may be faster but less optimal

Might find longer or suboptimal paths

Code change: modify comparison to use only h_n for sorting in the priority queue

🧩 Future Improvements
Add GUI for puzzle interaction

Allow user-defined initial states via CLI

Add more heuristics (e.g., misplaced tiles, linear conflict)