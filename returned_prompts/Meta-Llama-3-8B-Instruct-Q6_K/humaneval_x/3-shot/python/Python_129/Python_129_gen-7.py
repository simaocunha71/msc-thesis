    def dfs(i, j, k, visited, path):
        if k == 0:
            res.append(path)
            return
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited:
                visited.add((x, y))
                dfs(x, y, k-1, visited, path + [grid[x][y]])
                visited.remove((x, y))

    res = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            dfs(i, j, k, set([(i, j)]), [grid[i][j]])
    res.sort()
    return res[0]  # Return the first result, as it's guaranteed to be unique.
    # You can also return res, but the problem guarantees that the answer is unique.
    # This is because we're only considering paths of length k, and the problem
    # guarantees that there's only one such path. If there were multiple paths of
    # length k, we would have to return all of them. But in this case, we can
    # just return the first one.  #


