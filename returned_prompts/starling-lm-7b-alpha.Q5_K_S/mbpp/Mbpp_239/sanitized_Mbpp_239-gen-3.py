def get_total_number_of_sequences(m, n):
    if n == 1:
        return m
    elif n == 2:
        return m // 2 + 1
    else:
        return sum(get_total_number_of_sequences(m, i) for i in range(1, n))