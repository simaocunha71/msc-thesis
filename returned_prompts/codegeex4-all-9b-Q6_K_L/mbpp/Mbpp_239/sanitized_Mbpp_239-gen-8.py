def get_total_number_of_sequences(m, n):
    if n == 0:
        return 1
    count = 0
    for i in range(2, m + 1):
        count += get_total_number_of_sequences(i, n - 1)
    return count