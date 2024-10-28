
def get_total_number_of_sequences(m, n):
    if m < 2 or n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return m - 1
    return m * get_total_number_of_sequences(m - 1, n - 2) + get_total_number_of_sequences(m - 1, n - 1)


