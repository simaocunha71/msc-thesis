def get_total_number_of_sequences(m, n):
    if n == 1:
        return 1
    total = 0
    for i in range(1, m//2 + 1):
        total += get_total_number_of_sequences(m, n - 1)
    return total