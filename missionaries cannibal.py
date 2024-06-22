from collections import deque

# Define the starting and goal states
start_state = (3, 3, 1)  # (Missionaries on the left, Cannibals on the left, Boat on the left)
goal_state = (0, 0, 0)   # (Missionaries on the right, Cannibals on the right, Boat on the right)

# Define valid moves
moves = [
    (1, 0),  # One missionary crosses the river
    (2, 0),  # Two missionaries cross the river
    (0, 1),  # One cannibal crosses the river
    (0, 2),  # Two cannibals cross the river
    (1, 1)   # One missionary and one cannibal cross the river
]

def is_valid(state):
    m, c, _ = state
    # Check for invalid conditions
    if m < 0 or m > 3 or c < 0 or c > 3:
        return False
    if m != 0 and m < c:  # More cannibals than missionaries on the left bank
        return False
    if (3 - m) != 0 and (3 - m) < (3 - c):  # More cannibals than missionaries on the right bank
        return False
    return True

def bfs(start_state, goal_state):
    queue = deque([(start_state, [])])
    visited = set()
    visited.add(start_state)

    while queue:
        (m, c, b), path = queue.popleft()

        if (m, c, b) == goal_state:
            return path + [(m, c, b)]

        for move in moves:
            if b == 1:  # Boat on the left bank
                new_state = (m - move[0], c - move[1], 0)
            else:  # Boat on the right bank
                new_state = (m + move[0], c + move[1], 1)

            if is_valid(new_state) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [(m, c, b)]))

    return None

# Solve the problem
solution = bfs(start_state, goal_state)

# Print the solution
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found")
