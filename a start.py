import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost estimate to goal
        self.f = 0  # Total cost

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

    def __hash__(self):
        return hash(self.position)

def heuristic(current, goal):
    # Using Manhattan distance as heuristic function
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def astar(maze, start, end):
    start_node = Node(start)
    end_node = Node(end)

    open_list = []
    closed_list = set()

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node)

        if current_node == end_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Adjacent squares (up, down, left, right)

        for new_position in neighbors:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] < 0 or node_position[0] >= len(maze) or node_position[1] < 0 or node_position[1] >= len(maze[0]):
                continue  # Ensure within bounds

            if maze[node_position[0]][node_position[1]] != 0:
                continue  # Ensure walkable terrain

            neighbor = Node(node_position, current_node)

            if neighbor in closed_list:
                continue

            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor.position, end_node.position)
            neighbor.f = neighbor.g + neighbor.h

            if add_to_open(open_list, neighbor):
                heapq.heappush(open_list, neighbor)

    return None

def add_to_open(open_list, neighbor):
    for node in open_list:
        if neighbor == node and neighbor.g > node.g:
            return False
    return True

# Example usage
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

path = astar(maze, start, end)
print("Path:", path)
