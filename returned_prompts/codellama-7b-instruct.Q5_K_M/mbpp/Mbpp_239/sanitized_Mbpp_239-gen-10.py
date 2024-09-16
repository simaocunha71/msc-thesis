def get_total_number_of_sequences(m, n):
    memo = {}

    def T(n, m):
        if n == 0:
            return 1
        if (n, m) in memo:
            return memo[(n, m)]
        total = 0
        for i in range(2, m+1):
            total += T(n-1, i)
        memo[(n, m)] = total
        return total

    return T(n, m)