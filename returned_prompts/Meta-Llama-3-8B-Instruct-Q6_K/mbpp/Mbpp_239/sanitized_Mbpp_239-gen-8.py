def get_total_number_of_sequences(m, n):
    if n == 1:
        return 1
    total = 1
    for _ in range(1, n):
        total *= (m - 2 * total)
    return total