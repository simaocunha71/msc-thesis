def maxAverageOfPath(matrix):
    N = len(matrix)
    paths = [[(0, 0)]]
    for i in range(N):
        new_paths = []
        for path in paths:
            if path[-1][0] < N - 1:
                new_paths.append(path + [(path[-1][0] + 1, path[-1][1])])
            if path[-1][1] < N - 1:
                new_paths.append(path + [(path[-1][0], path[-1][1] + 1)])
        paths = new_paths
    max_avg = 0
    for path in paths:
        total_cost = sum(matrix[i][j] for i, j in path)
        max_avg = max(max_avg, total_cost / len(path))
    return max_avg