def get_total_number_of_sequences(m, n):
    def recurse(i, prev):
        if i == n:
            return 1
        count = 0
        for j in range(2 * prev, m + 1):
            count += recurse(i + 1, j)
        return count

    return recurse(0, 1)