# Mohamed saeed 
# 2/14/2025
# purposed = Manhattan Distance Heuristic Function that solves a 0-8 puzzle 3x3 sliding puzzle
 
 
#•	Write up (10 points)
# Describe how your code would need to change if you instcd ead implemented 
# the greedy search algorithm. Note: You do not need to implement it.

# instead of measuring both g(n) and h(n) you would only need the heuristic cost and not the path cost to get the greedy first infomred search

import heapq
import pandas as pd

# Goal state of the 8-puzzle game (solved state)
GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # 0 represents the empty tile

# moves in a 1D list 
MOVES = {
    'Up': -3,    # Move up (shift index by -3)
    'Down': 3,   # Move down (shift index by +3)
    'Left': -1,  # Move left (shift index by -1)
    'Right': 1   # Move right (shift index by +1)
}

class Node:
    def __init__(self, state, g_n, h_n, parent=None, move=None):
        self.state = state
        self.g_n = g_n  # Path cost from start to current node
        self.h_n = h_n  # Heuristic estimate to goal
        self.f_n = g_n + h_n  # Total estimated cost
        self.parent = parent  # Reference to parent node in the tree
        self.move = move  # Move that led to this state
        self.children = []  # List to store child nodes
        self.depth = 0  # Depth in the tree
        if parent:
            self.depth = parent.depth + 1

    def __lt__(self, other):
        """Comparison method for priority queue ordering"""
        return self.f_n < other.f_n

    def __eq__(self, other):
        """Equality comparison for state checking"""
        return self.state == other.state

    def add_child(self, child):
        """Add a child node to this node"""
        self.children.append(child)
        child.parent = self

    def get_path(self):
        """Get the path from root to this node"""
        path = []
        current = self
        while current:
            path.append(current)
            current = current.parent
        return list(reversed(path))

    def is_leaf(self):
        """Check if this is a leaf node (no children)"""
        return len(self.children) == 0

    def get_state_string(self):
        """Get a string representation of the state"""
        return str(self.state)

    def get_cost_string(self):
        """Get a string representation of the costs"""
        return f"g(n)={self.g_n}, h(n)={self.h_n}, f(n)={self.f_n}"

# Manhattan Distance Heuristic Function
def manhattan_distance(state):
    """Computes the sum of Manhattan distances of all tiles from their goal positions."""
    
    print(f"Calculating Manhattan Distance for state: {state}")  #Print the current state being evaluated
    distance = 0  

    for i in range(1, 9):  # Ignore tile 0 (empty tile) only 1-8
        s_index = state.index(i)  # Get index of the tile in the current state
        goal_index = GOAL_STATE.index(i)  # Get index of the tile in the goal state
        tile_distance = abs(s_index // 3 - goal_index // 3) + abs(s_index % 3 - goal_index % 3)  # Manhattan distance formula
        distance += tile_distance  # total Manhattan distance

    print(f"Total Manhattan Distance: {distance}")  # Print the computed Manhattan distance
    return distance  # Return the heuristic value

# Function to get valid neighboring states
def get_neighbors(state):
    """Returns all valid moves and resulting puzzle states."""
    neighbors = []  # Initialize an empty list to store valid neighboring states
    zero_index = state.index(0)  # Find the index of the empty tile (0)

    for move, offset in MOVES.items():  # Loop through all possible moves
        new_index = zero_index + offset  # Calculate the new position of the empty tile

        # Prevent invalid moves (avoid wrapping around in rows)
        if 0 <= new_index < 9 and not (zero_index % 3 == 2 and move == 'Right') and not (zero_index % 3 == 0 and move == 'Left'):
            new_state = state[:]  # Copy of the current state 
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]  # Swap empty tile with the moved tile
            neighbors.append((new_state, move))  # Store the new state and the move taken
    
    return neighbors  # Return the list of valid neighboring states

def reconstruct_path(node):
    """Reconstructs the path from the goal node to the start node."""
    path = []
    states = []
    current = node
    
    while current:
        path.append(current.move if current.move else "Start")
        states.append(current.state)
        current = current.parent
    
    return list(reversed(path)), list(reversed(states))

# A* Search Algorithm
def a_star_with_states(initial_state):
    """Performs A* search using the Manhattan Distance heuristic and prints each state."""
    # Initialize the start node
    start_node = Node(initial_state, 0, manhattan_distance(initial_state))
    frontier = [start_node]
    visited = {}  # Dictionary to store visited states with their costs

    while frontier:
        current_node = heapq.heappop(frontier)
        
        # Print expanded node details
        print(f"Expanding Node: {current_node.state}")
        print(f"f(n) = g(n) + h(n) -> {current_node.f_n} = {current_node.g_n} + {current_node.h_n}")
        print("===============================================================")

        # If goal is reached, reconstruct and return the path
        if current_node.state == GOAL_STATE:
            print("\nSolution found!")
            return reconstruct_path(current_node)

        state_tuple = tuple(current_node.state)
        
        # Skip if we've found a better or equal path to this state
        if state_tuple in visited and visited[state_tuple] <= current_node.g_n:
            continue
            
        visited[state_tuple] = current_node.g_n

        # Expand the current state and find its valid neighbors
        for neighbor_state, move in get_neighbors(current_node.state):
            new_g = current_node.g_n + 1
            neighbor_tuple = tuple(neighbor_state)
            
            # Skip if we've already found a better path to this neighbor
            if neighbor_tuple in visited and visited[neighbor_tuple] <= new_g:
                continue
                
            h_n = manhattan_distance(neighbor_state)
            new_node = Node(neighbor_state, new_g, h_n, current_node, move)
            current_node.add_child(new_node)  # Add child to tree structure
            heapq.heappush(frontier, new_node)

    print("\nNo solution found.")
    return None, None

# Initial state of the puzzle
initial_state = [1, 3, 4, 7, 0, 2, 5, 8, 6]

# Run A* search algorithm
solution_path, explored_states = a_star_with_states(initial_state)

if solution_path and explored_states and len(solution_path) == len(explored_states):
    df_results = pd.DataFrame({
        "Puzzle State": explored_states,
        "Move": solution_path
    })

    # Print the final results of A* search
    print("\nA* Algorithm - State Exploration:")
    print(df_results.to_string())  # Print the DataFrame in text format
    
    # Print the solution sequence
    print("\nSolution Sequence:")
    for i, (state, move) in enumerate(zip(explored_states, solution_path)):
        print(f"{i}: Move {move}")
else:
    print("No valid solution or mismatch in solution lengths.")
