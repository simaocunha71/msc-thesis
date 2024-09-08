def get_total_number_of_sequences(m: int, n: int) -> int:
    sequences = [[1 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(2, m+1):
        for j in range(2, n+1):
            sequences[i][j] = sequences[i-1][j] + sequences[i//2][j-1]
    return sequences[m][n]