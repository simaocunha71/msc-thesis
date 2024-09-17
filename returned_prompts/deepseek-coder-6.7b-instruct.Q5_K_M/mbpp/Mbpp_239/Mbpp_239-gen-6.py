
def get_total_number_of_sequences(m, n):
    seq = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        seq[i][1] = 1
    for i in range(2, n+1):
        for j in range(1, m+1):
            for k in range(1, j):
                seq[j][i] += seq[k][i-1]
    count = 0
    for i in range(1, m+1):
        count += seq[i][n]
    return count


