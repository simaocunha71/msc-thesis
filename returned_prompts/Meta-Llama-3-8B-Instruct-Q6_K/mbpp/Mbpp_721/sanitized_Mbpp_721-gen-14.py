def maxAverageOfPath(matrix):
    def dfs(i, j, total, count):
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
            return total / count if count > 0 else 0
        total += matrix[i][j]
        count += 1
        matrix[i][j] = -1
        return max(dfs(i + 1, j, total, count), dfs(i, j + 1, total, count))

    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                res = max(res, dfs(i, j, 0, 1))
    return res