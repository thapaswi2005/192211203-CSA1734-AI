from typing import List, Dict, Tuple, Optional

def is_consistent(region: str, color: str, assignment: Dict[str, str], neighbors: Dict[str, List[str]]) -> bool:
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def select_unassigned_variable(assignment: Dict[str, str], domains: Dict[str, List[str]]) -> str:
    unassigned = [v for v in domains.keys() if v not in assignment]
    # Minimum Remaining Values (MRV) heuristic
    return min(unassigned, key=lambda var: len(domains[var]))

def order_domain_values(region: str, assignment: Dict[str, str], domains: Dict[str, List[str]]) -> List[str]:
    return domains[region]

def forward_checking(region: str, color: str, domains: Dict[str, List[str]], neighbors: Dict[str, List[str]]):
    for neighbor in neighbors[region]:
        if color in domains[neighbor]:
            domains[neighbor].remove(color)

def backtracking_search(assignment: Dict[str, str], domains: Dict[str, List[str]], neighbors: Dict[str, List[str]]) -> Optional[Dict[str, str]]:
    if len(assignment) == len(domains):
        return assignment

    region = select_unassigned_variable(assignment, domains)

    for color in order_domain_values(region, assignment, domains):
        if is_consistent(region, color, assignment, neighbors):
            assignment[region] = color
            # Forward checking
            original_domains = domains.copy()
            forward_checking(region, color, domains, neighbors)
            
            result = backtracking_search(assignment, domains, neighbors)
            if result is not None:
                return result
            
            # Restore domains
            assignment.pop(region)
            domains = original_domains

    return None

# Define the map and constraints
regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

colors = ['Red', 'Green', 'Blue']

# Initialize domains
domains = {region: colors[:] for region in regions}

# Run the map coloring CSP
assignment = {}
solution = backtracking_search(assignment, domains, neighbors)

if solution:
    print("Solution found:")
    for region in solution:
        print(f"{region}: {solution[region]}")
else:
    print("No solution found")
