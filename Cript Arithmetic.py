import itertools

def is_solution_valid(send, more, money):
    # Convert letters to their corresponding digit values
    s = int(send[0])
    e = int(send[1])
    n = int(send[2])
    d = int(send[3])
    m = int(more[0])
    o = int(more[1])
    r = int(more[2])
    y = int(money[4])
    
    # Construct the integers from the digits
    send_value = 1000 * s + 100 * e + 10 * n + d
    more_value = 1000 * m + 100 * o + 10 * r + e
    money_value = 10000 * m + 1000 * o + 100 * n + 10 * e + y
    
    # Check if SEND + MORE == MONEY
    return send_value + more_value == money_value

def solve_cryptarithmetic():
    # Letters used in the problem
    letters = 'SENDMOREY'
    
    # Digits to assign to the letters
    digits = '0123456789'
    
    # Generate all possible permutations of the digits for the letters
    for perm in itertools.permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))
        
        send = ''.join(mapping[c] for c in 'SEND')
        more = ''.join(mapping[c] for c in 'MORE')
        money = ''.join(mapping[c] for c in 'MONEY')
        
        if send[0] != '0' and more[0] != '0' and money[0] != '0':  # No leading zeros
            if is_solution_valid(send, more, money):
                return mapping
                
    return None

# Solve the problem and print the solution
solution = solve_cryptarithmetic()
if solution:
    print("Solution found:")
    for letter, digit in solution.items():
        print("{letter}: {digit}")
else:
    print("No solution exists.")
