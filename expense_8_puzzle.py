import sys
from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue


def print_solution(path, c, num_gen=None, num_pop=None, FrLmt=None, curr_depth=None, dump_flag=False, output_file="output.txt"):
    if path is None:
        optStr = "No solution found."
    else:
        optStr = "Solution found with cost {}:\n".format(c)
        for i, (state, successor) in enumerate(path):
            optStr += "Step {}\n".format(i + 1)
            for row in successor:
                optStr += " ".join(str(x) for x in row) + "\n"
            optStr += "\n"
        optStr += "Nodes generated: {}\n".format(num_gen)
        optStr += "Nodes popped: {}\n".format(num_pop)
        optStr += "Fringe size: {}\n".format(FrLmt)
        optStr += "Step cost: {}\n".format(c)

    if curr_depth is not None:
        optStr += "Goal state state found in: {}\n".format(curr_depth)
    if dump_flag:
        with open(output_file, 'a') as f:
            f.write(optStr)
    else:
        print(optStr)


# Define the possible moves
Possible_Moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


# Define a function to get the coordinates of a tile in a state
def get_tile_coords(state, tile):
    for i in range(3):
        for j in range(3):
            if state[i][j] == tile:
                return (i, j)


# Define a function to generate the successor states
def succ_function(state):
    ith_z, jth_z = get_tile_coords(state, 0)
    for move, (di, dj) in Possible_Moves.items():
        i_new, j_new = ith_z + di, jth_z + dj
        if 0 <= i_new < 3 and 0 <= j_new < 3:
            new_state = [row[:] for row in state]
            tile = new_state[i_new][j_new]
            step_cost = tile
            new_state[i_new][j_new] = 0
            new_state[ith_z][jth_z] = tile
            yield (new_state, step_cost)


def euclidean_distance(state):
    
    # Compute the Euclidean distance heuristic for the 8-puzzle problem.
    
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                target_i, target_j = divmod(state[i][j]-1, 3)
                distance += ((i - target_i) ** 2 + (j - target_j) ** 2) ** 0.5
    return distance


def depthLimitedSearch(state, path, cost, depth, limit, visited):
    if depth == limit:
        return (None, None, None, None, None, None) # depth limit reached without finding goal state
    visited.add(tuple(map(tuple, state)))
    generated_number = 0
    popped_number = 0
    maxFriSize = 1
    for successor, step_cost in succ_function(state):
        generated_number += 1
        if tuple(map(tuple, successor)) in visited:
            continue
        new_path = path + [(state, successor)]
        new_cost = cost + step_cost
        if successor == GOAL_STATE:
            return (new_path, new_cost, generated_number, num_popped, maxFriSize, depth + 1) # goal state found
        result = depthLimitedSearch(successor, new_path, new_cost, depth + 1, limit, visited)
        if result[0] is not None:
            return result # goal state found in recursive call
        popped_number+= 1
        maxFriSize = max(maxFriSize, generated_number - popped_number+ 1)
    return (None, None, generated_number, num_popped, maxFriSize, None) # goal state not found in this subtree

def iterativeDeepeningSearch(start_state, max_depth):
    limit = 0
    while limit <= max_depth:
        visited = set()
        path, cost, generated_number, num_popped, maximumFringe, depth = depthLimitedSearch(start_state, [], 0, 0, limit, visited)
        if path is not None:
            return (path, cost, generated_number, num_popped, maximumFringe, depth)
        limit += 1
    return (None, None, None, None, None, None)

def greedyBestFirstSearch(start_state):
    queue = PriorityQueue()
    queue.put((euclidean_distance(start_state), start_state, [], 0, 0))
    visited = set()
    generated_number = 0
    popped_number= 0
    maximumFringe = 1

    if dump_flag:
        with open('output.txt', 'a') as f:
            output_String = "GREEDY BEST-FIRST SEARCH--------------\n"
            f.write(output_String)
    else:
        print("\nGREEDY BEST-FIRST SEARCH--------------\n")
    while not queue.empty():
        _, state, path, cost, depth = queue.get()
        if dump_flag:
            with open('output.txt', 'a') as f:
                output_String = "State: {}\n".format(state)
                f.write(output_String)
        else:
            print("State of Greedy Best First Search: {}\n".format(state))

        popped_number+= 1
        if state == GOAL_STATE:
            return (path, cost, generated_number, num_popped, maximumFringe, depth)
        if tuple(map(tuple, state)) in visited:
            continue
        visited.add(tuple(map(tuple, state)))
        for successor, step_cost in succ_function(state):
            generated_number += 1
            priority = euclidean_distance(successor)
            queue.put((priority, successor, path + [(state, successor)], cost + step_cost, depth + 1))
            maximumFringe = max(maximumFringe, queue.qsize())
    return (None, None, generated_number, num_popped, maximumFringe, None, None)

# Define a heuristic function for A* search
def h(state):
    # Calculate the Euclidean distance between the current state and the goal state
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:
                goal_i, goal_j = get_tile_coords(GOAL_STATE, tile)
                distance += ((i - target_i) ** 2 + (j - target_j) ** 2) ** 0.5
    return distance

def a_star(start_state):
    queue = PriorityQueue()
    queue.put((h(start_state), start_state, [], 0, 0))
    visited = set()
    generated_number = 0
    popped_number= 0
    maximumFringe = 1
    if dump_flag:
        with open('output.txt', 'a') as f:
            output_String = "\nA* SEARCH------------------\n"
            f.write(output_String)
    else:
        print("\nA* SEARCH------------------\n")
    while not queue.empty():
        _, state, path, cost, depth = queue.get()
        if dump_flag:
            with open('output.txt', 'a') as f:
                output_String = "State for A_Star: {}\n".format(state)
                f.write(output_String)
        else:
            print("State of ASTAR: {}\n".format(state))
        popped_number+= 1
        if state == GOAL_STATE:
            return (path, cost, generated_number, num_popped, maximumFringe, depth)
        if tuple(map(tuple, state)) in visited:
            continue
        visited.add(tuple(map(tuple, state)))
        for successor, step_cost in succ_function(state):
            generated_number += 1
            queue.put((h(successor) + cost + step_cost, successor, path + [(state, successor)], cost + step_cost, depth + 1))
            maximumFringe = max(maximumFringe, queue.qsize())
    return (None, None, generated_number, num_popped, maximumFringe, None, None)

def uniformCostSearch(start_state):
    queue = PriorityQueue()
    queue.put((0, start_state, [], 0, 0))
    visited = set()
    generated_number = 0
    popped_number= 0
    maximumFringe = 1
    if dump_flag:
        with open('output.txt', 'a') as f:
            output_String = "\nUNIFORM COST SEARCH------------------\n"
            f.write(output_String)
    else:
        print("\nUNIFORM COST SEARCH------------------\n")
    while not queue.empty():
        _, state, path, cost, depth = queue.get()
        if dump_flag:
            with open('output.txt', 'a') as f:
                output_String = "State: {}\n".format(state)
                f.write(output_String)
        else:
            print("State of Uniform Cost Search: {}\n".format(state))
        popped_number+= 1
        if state == GOAL_STATE:
            return (path, cost, generated_number, num_popped, maximumFringe, depth)
        if tuple(map(tuple, state)) in visited:
            continue
        visited.add(tuple(map(tuple, state)))
        for successor, step_cost in succ_function(state):
            generated_number += 1
            queue.put((cost + step_cost, successor, path + [(state, successor)], cost + step_cost, depth + 1))
            maximumFringe = max(maximumFringe, queue.qsize())
    return (None, None, generated_number, num_popped, maximumFringe, None, None)

def depthFirstSearch(start_state):
    stack = LifoQueue()
    stack.put((start_state, [], 0, 0))
    visited = set()
    generated_number = 0
    popped_number= 0
    maximumFringe = 1

    if dump_flag:
        with open('output.txt', 'a') as f:
            output_String = "\nDEPTH FIRST SEARCH------------------\n"
            f.write(output_String)
    else:
        print("\nDEPTH FIRST SEARCH------------------\n")
    while not stack.empty():
        state, path, cost, depth = stack.get()
        if dump_flag:
            with open('output.txt', 'a') as f:
                output_String = "State: {}\n".format(state)
                f.write(output_String)
        else:
            print("State of Depth First Search: {}\n".format(state))
        popped_number+= 1
        if state == GOAL_STATE:
            return (path, cost, generated_number, num_popped, maximumFringe, depth)
        if tuple(map(tuple, state)) in visited:
            continue
        visited.add(tuple(map(tuple, state)))
        for successor, step_cost in reversed(list(succ_function(state))):
            generated_number += 1
            stack.put((successor, path + [(state, successor)], cost + step_cost, depth + 1))
            maximumFringe = max(maximumFringe, stack.qsize())
    return (None, None, generated_number, num_popped, maximumFringe, None, None)

def breadthFirstSearch(start_state):
    queue = Queue()
    queue.put((start_state, [], 0, 0))
    visited = set()
    generated_number = 0
    num_popped= 0
    maximumFringe = 1

    if dump_flag:
        with open('output.txt', 'a') as f:
            output_String = "\nBREADTH FIRST SEARCH------------------\n"
            f.write(output_String)
    else:
        print("\nBREADTH FIRST SEARCH------------------\n")
    while not queue.empty():
        state, path, cost, depth = queue.get()
        if dump_flag:
            with open('output.txt', 'a') as f:
                output_String = "State: {}\n".format(state)
                f.write(output_String)
        else:
            print("State of Breadth first search: {}\n".format(state))
        num_popped += 1
        if state == GOAL_STATE:
            return (path, cost, generated_number, num_popped, maximumFringe, depth)
        if tuple(map(tuple, state)) in visited:
            continue
        visited.add(tuple(map(tuple, state)))
        for successor, step_cost in succ_function(state):
            generated_number += 1
            queue.put((successor, path + [(state, successor)], cost + step_cost, depth + 1))
            maximumFringe = max(maximumFringe, queue.qsize())
    return (None, None, generated_number, num_popped, maximumFringe, None, None)

# Define a function to read the input file
def readIPFile(file):
    with open(file) as f:
        lines = f.readlines()  #inbuilt
    state = []
    for line in lines:
        row = []
        for x in line.split():
            try:
                row.append(int(x))
            except ValueError:
                pass
        if row:
            state.append(row)
    return state

start = sys.argv[1]
goal = sys.argv[2]
method = sys.argv[3]
if len(sys.argv) > 4 and sys.argv[4] == "True":
    dump_flag = True
else:
    dump_flag = False
output_file = "output.txt"
# Define the goal state
start_state = readIPFile(start)
goal_state = readIPFile(goal)
GOAL_STATE = goal_state



# Define a dictionary that maps method names to functions
methods = {
    "breadthFirstSearch": breadthFirstSearch,
    "depthFirstSearch": depthFirstSearch,
    "uniformCostSearch": uniformCostSearch,
    "a_star": a_star,
    "greedyBestFirstSearch": greedyBestFirstSearch,
    "iterativeDeepeningSearch": lambda start_state: iterativeDeepeningSearch(start_state, 19),
    "depthLimitedSearch": depthLimitedSearch(start_state, 19)
}

# Look up the function based on the method name
search_func = methods.get(method)

# Call the function if it exists, or print an error message if it doesn't
if search_func is None:
    print("Invalid search method specified.")
else:
    path, cost, generated_number, num_popped, maximumFringe, depth = search_func(start_state)
    print_solution(path, cost, generated_number, num_popped, maximumFringe, depth, dump_flag, "output.txt")


