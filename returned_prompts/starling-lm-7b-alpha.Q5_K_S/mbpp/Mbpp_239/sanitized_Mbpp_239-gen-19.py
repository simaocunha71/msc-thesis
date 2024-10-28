def get_total_number_of_sequences(m: int, n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return m
    return m * get_total_number_of_sequences(m, n - 1) // n