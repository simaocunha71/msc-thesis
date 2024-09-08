def get_total_number_of_sequences(m, n):
    def count_sequences(m, n, prev):
        if n == 0:
            return 1
        count = 0
        for i in range(prev * 2, min(m, prev * 2 + 1)):
            count += count_sequences(m, n - 1, i)
        return count

    return count_sequences(m, n, 1)