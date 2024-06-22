from collections import deque

def is_valid_state(state, max_jug1, max_jug2):
    jug1, jug2 = state
    return 0 <= jug1 <= max_jug1 and 0 <= jug2 <= max_jug2

def get_next_states(state, max_jug1, max_jug2):
    jug1, jug2 = state
    next_states = []

    # Fill Jug 1
    next_states.append((max_jug1, jug2))

    # Fill Jug 2
    next_states.append((jug1, max_jug2))

    # Empty Jug 1
    next_states.append((0, jug2))

    # Empty Jug 2
    next_states.append((jug1, 0))

    # Pour Jug 1 -> Jug 2
    pour_to_jug2 = min(jug1, max_jug2 - jug2)
    next_states.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2))

    # Pour Jug 2 -> Jug 1
    pour_to_jug1 = min(jug2, max_jug1 - jug1)
    next_states.append((jug1 + pour_to_jug1, jug2 - pour_to_jug1))

    return next_states

def bfs(max_jug1, max_jug2, target):
    start_state = (0, 0)
    queue = deque([start_state])
    visited = set()
    visited.add(start_state)

    while queue:
        current_state = queue.popleft()
        jug1, jug2 = current_state

        if jug1 == target or jug2 == target:
            return True

        for next_state in get_next_states(current_state, max_jug1, max_jug2):
            if is_valid_state(next_state, max_jug1, max_jug2) and next_state not in visited:
                queue.append(next_state)
                visited.add(next_state)

    return False

# Get user input for the capacities of the jugs and the target amount
max_jug1 = int(input("Enter the capacity of Jug 1: "))
max_jug2 = int(input("Enter the capacity of Jug 2: "))
target = int(input("Enter the target amount of water to measure: "))

# Call the function to solve the Water Jug problem
if bfs(max_jug1, max_jug2, target):
    print("It is possible to measure the target amount of water.")
else:
    print("It is not possible to measure the target amount of water.")
