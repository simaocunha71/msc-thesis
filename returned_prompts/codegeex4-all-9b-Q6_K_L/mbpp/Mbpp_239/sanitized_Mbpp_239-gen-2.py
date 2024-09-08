def get_total_number_of_sequences(m, n):
    def dfs(m, n, prev):
        if n == 0:
            return 1
        count = 0
        for i in range(2*prev, m+1):
            count += dfs(m, n-1, i)
        return count

    return dfs(m, n, 1)