def get_total_number_of_sequences(m, n):
    # Initialize the table
    table = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        table[i][1] = 1
    for j in range(2, n+1):
        for i in range(1, m+1):
            for k in range(i*2, m+1):
                table[k][j] += table[i][j-1]
    return sum([table[i][n] for i in range(1, m+1)])