def get_total_number_of_sequences(m, n):
    memo = {}

    def helper(prev, n):
        if n == 0:
            return 1
        if (prev, n) in memo:
            return memo[(prev, n)]
        total = 0
        for i in range(2 * prev, min(m, 2 * prev + 1)):
            total += helper(i, n - 1)
        memo[(prev, n)] = total
        return total

    return helper(0, n)