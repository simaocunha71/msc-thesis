def get_total_number_of_sequences(m, n):
    if n == 1:
        return 1
    if n == 2:
        return m
    total_sequences = 0
    for i in range(2, m):
        total_sequences += get_total_number_of_sequences(m, n-1)
    return total_sequences