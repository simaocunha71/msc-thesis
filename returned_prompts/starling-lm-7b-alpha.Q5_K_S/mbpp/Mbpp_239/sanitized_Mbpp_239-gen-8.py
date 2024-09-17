def get_total_number_of_sequences(m, n):
    if n == 1:
        return m
    if n == 2:
        return m // 2 + 1
    if n == 3:
        return m // 2 + m // 4 + 1

    return sum(get_total_number_of_sequences(m, n - i - 1) * (m // (2 ** i) + 1) for i in range(n - 1))