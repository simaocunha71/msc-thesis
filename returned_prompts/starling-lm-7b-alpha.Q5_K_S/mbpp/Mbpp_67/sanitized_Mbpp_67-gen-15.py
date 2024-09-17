def bell_number(n):
    # Create a table to store results of subproblems
    b = [0 for row in range(n + 1)]
    b[0] = 1 
    b[1] = 1
    for i in range(2, n + 1):
        b[i] = b[i-1] + b[i-2] + i - 1
    return b[n]