import heapq

# Define the goal state
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


# Helper function to find the position of the blank (0) tile
def find_blank_position(state):
    for i, row in enumerate(state):
        for j, tile in enumerate(row):
            if tile == 0:
                return i, j


# Helper function to calculate the Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:
                goal_i, goal_j = divmod(tile - 1, 3)
                distance += abs(goal_i - i) + abs(goal_j - j)
    return distance


# Helper function to generate the possible moves from the current state
def generate_moves(state):
    blank_i, blank_j = find_blank_position(state)
    moves = []
    if blank_i > 0:
        new_state = [row[:] for row in state]
        new_state[blank_i][blank_j], new_state[blank_i - 1][blank_j] = new_state[blank_i - 1][blank_j], \
                                                                       new_state[blank_i][blank_j]
        moves.append(new_state)
    if blank_i < 2:
        new_state = [row[:] for row in state]
        new_state[blank_i][blank_j], new_state[blank_i + 1][blank_j] = new_state[blank_i + 1][blank_j], \
                                                                       new_state[blank_i][blank_j]
        moves.append(new_state)
    if blank_j > 0:
        new_state = [row[:] for row in state]
        new_state[blank_i][blank_j], new_state[blank_i][blank_j - 1] = new_state[blank_i][blank_j - 1], \
                                                                       new_state[blank_i][blank_j]
        moves.append(new_state)
    if blank_j < 2:
        new_state = [row[:] for row in state]
        new_state[blank_i][blank_j], new_state[blank_i][blank_j + 1] = new_state[blank_i][blank_j + 1], \
                                                                       new_state[blank_i][blank_j]
        moves.append(new_state)
    return moves


# A* search algorithm
def a_star_search(start_state):
    open_list = []
    heapq.heappush(open_list, (0 + manhattan_distance(start_state), 0, start_state, None))
    closed_list = set()
    came_from = {}

    while open_list:
        _, cost, current, parent = heapq.heappop(open_list)
        if current == GOAL_STATE:
            path = []
            while parent:
                path.append(current)
                current = parent
                parent = came_from.get(tuple(map(tuple, current)), None)
            path.append(start_state)
            path.reverse()
            return path

        closed_list.add(tuple(map(tuple, current)))

        for neighbor in generate_moves(current):
            if tuple(map(tuple, neighbor)) in closed_list:
                continue
            new_cost = cost + 1
            heapq.heappush(open_list, (new_cost + manhattan_distance(neighbor), new_cost, neighbor, current))
            came_from[tuple(map(tuple, neighbor))] = current

    return None
initial_state = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]

# Solve the puzzle
solution_path = a_star_search(initial_state)

# Print the solution path
if solution_path:
    for step in solution_path:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
