def get_total_number_of_sequences(m: int, n: int) -> int:
    if n <= 1:
        return 1
    if n == 2:
        return m
    total = 0
    for i in range(2, m):
        total += 1
    return total