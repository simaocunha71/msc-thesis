
def get_total_number_of_sequences(m, n):
    if n == 0:
        return 1
    else:
        return sum(get_total_number_of_sequences(m, n - 1) for _ in range(m // (n - 1)))


