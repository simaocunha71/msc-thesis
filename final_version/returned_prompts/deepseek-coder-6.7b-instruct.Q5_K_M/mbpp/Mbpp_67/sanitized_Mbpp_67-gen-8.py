def bell_number(n):
    # Create a 2D table to store results of sub-problems
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    for i in range(1, n+1):
        # Explicitly fill for j = 0
        bell[i][0] = bell[i-1][i-1]
        # Fill for remaining values of j
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    # The total number of ways is the sum of all the numbers in the last row
    return sum(bell[n])