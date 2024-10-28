def get_max_sum(n):
    # Initialize a table to store the maximum sum for each number
    table = [0] * (n+1)

    # Base cases
    table[1] = 1
    table[2] = 2
    table[3] = 3
    table[4] = 4
    table[5] = 5

    # Calculate the maximum sum for each number using the given equation
    for i in range(6, n+1):
        table[i] = max(table[i//2] + table[i//3] + table[i//4] + table[i//5], i)

    return table[n]