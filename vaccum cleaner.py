from collections import deque

# Define the directions the vacuum cleaner can move
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

# Define the initial state of the grid and the vacuum cleaner's starting position
initial_grid = [
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 1]
]

start_position = (0, 0)  # Starting at the top-left corner

def is_valid(grid, pos):
    rows, cols = len(grid), len(grid[0])
    x, y = pos
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] != -1

def bfs(grid, start):
    queue = deque([(start, [])])
    visited = set()
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()

        # If all cells are cleaned, return the path
        if all(all(cell == 0 for cell in row) for row in grid):
            return path + [(x, y)]

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if is_valid(grid, (nx, ny)) and (nx, ny) not in visited:
                # Clean the current cell
                grid[x][y] = 0
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(x, y)]))
                # Restore the current cell's dirty state to continue search
                grid[x][y] = 1

    return None

# Solve the vacuum cleaner problem
solution = bfs(initial_grid, start_position)

# Print the solution
if solution:
    print("Path to clean all cells:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
