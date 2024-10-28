def get_total_number_of_sequences(m, n):
    if n == 1:
        return 1
    total = 0
    for i in range(2, min(m, n*2), 2):
        total += get_total_number_of_sequences(m, n-1)
    return total