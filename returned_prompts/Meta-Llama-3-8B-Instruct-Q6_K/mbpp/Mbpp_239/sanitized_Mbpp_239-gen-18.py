def get_total_number_of_sequences(m, n):
    if n == 1:
        return 1
    total = 0
    for i in range(2, m):
        total += get_total_number_of_sequences(i, n - 1)
    return total