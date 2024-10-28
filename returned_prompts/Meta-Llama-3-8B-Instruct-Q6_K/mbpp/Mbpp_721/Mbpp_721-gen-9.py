```
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
```

In this solution, we first generate all possible paths from the top-left cell to the bottom-right cell. Then we iterate over these paths and for each path, we calculate the total cost and the average cost. We keep track of the maximum average cost found so far and return it at the end. The unit test `assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2` ensures that the function is working correctly. 





The problem is asking us to find the maximum average cost of all possible paths from the top-left cell to the bottom-right cell in a given square matrix. The cost of a path is the sum of the costs of all cells in the path, divided by the number of cells in the path.

Here is a Python solution for this problem:
```
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
       