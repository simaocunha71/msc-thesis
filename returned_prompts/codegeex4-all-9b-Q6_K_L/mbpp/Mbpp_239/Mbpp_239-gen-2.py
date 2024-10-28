def get_total_number_of_sequences(m: int, n: int) -> int:
    if n == 1:
        return m
    count = 0
    for i in range(1, m//2+1):
        count += get_total_number_of_sequences(i, n-1)
    return count