from itertools import permutations

# Function to calculate the total distance of a given path
def calculate_distance(path, distance_matrix):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance_matrix[path[i]][path[i + 1]]
    total_distance += distance_matrix[path[-1]][path[0]]  # Return to the starting city
    return total_distance

# Function to solve TSP using brute-force approach
def travelling_salesman_bruteforce(distance_matrix):
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))
    min_path = None
    min_distance = float('inf')

    for perm in permutations(cities):
        current_distance = calculate_distance(perm, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = perm
    
    return min_path, min_distance

# Example usage
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_path, best_distance = travelling_salesman_bruteforce(distance_matrix)
print("Best path: {best_path}")
print("Best distance: {best_distance}")
