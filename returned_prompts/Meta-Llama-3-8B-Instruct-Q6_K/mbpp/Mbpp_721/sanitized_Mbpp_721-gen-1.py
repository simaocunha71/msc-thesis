def maxAverageOfPath(matrix):
    N = len(matrix)
    memo = [[0]*N for _ in range(N)]
    max_avg = float('-inf')

    def dfs(i, j):
        if i<0 or j<0 or i>=N or j>=N:
            return 0
        if memo[i][j] != 0:
            return memo[i][j]
        path_cost = matrix[i][j]
        if i == N-1 and j == N-1:
            memo[i][j] = path_cost
        else:
            memo[i][j] = path_cost + max(dfs(i+1, j), dfs(i, j+1))
        return memo[i][j]

    for i in range(N):
        for j in range(N):
            path_cost = dfs(i, j)
            if path_cost > 0:
                avg = path_cost / (i+1+j+1)
                max_avg = max(max_avg, avg)

    return max_avg