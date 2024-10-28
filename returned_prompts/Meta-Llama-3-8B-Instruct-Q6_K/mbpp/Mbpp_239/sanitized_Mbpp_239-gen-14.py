def get_total_number_of_sequences(m, n):
    if n == 1:
        return m
    else:
        return m * get_total_number_of_sequences(m // 2, n - 1)