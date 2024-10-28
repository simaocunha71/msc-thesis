"""
dp = {}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == 0 and j == 0:
            dp[(i, j)] = matrix[i][j]
        elif i == 0:
            dp[(i, j)] = max(matrix[i][j], dp[(i, j-1)] + matrix[i][j])
        elif j == 0:
            dp[(i, j)] = max(matrix[i][j], dp[(i-1, j)] + matrix[i][j])
        else:
            dp[(i, j)] = max(dp[(i, j-1)] + matrix[i][j], dp[(i-1, j)] + matrix[i][j])

return sum(dp.values())/len(dp)
"""
