def get_total_number_of_sequences(m, n):
    def get_sequences(m, n, prev):
        if n == 0:
            return 1
        total = 0
        for i in range(2 * prev, min(m, 2 * prev + 1)):
            total += get_sequences(m, n - 1, i)
        return total

    return get_sequences(m, n, 1)