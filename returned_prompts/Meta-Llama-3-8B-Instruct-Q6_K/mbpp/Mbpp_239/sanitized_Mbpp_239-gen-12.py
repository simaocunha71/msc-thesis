def get_total_number_of_sequences(m, n):
    if n == 1:
        return m
    if n == 2:
        return m * (m - 1) // 2
    
    total = 0
    for i in range(2, m):
        total += get_total_number_of_sequences(m, n - 1)
    return total