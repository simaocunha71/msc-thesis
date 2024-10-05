
def minPath(grid, k):
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: List[int]
    """
    N = len(grid)
    d = {(0, 0): [1]}
    for i in range(k):
        d = {(i, j): [grid[i][j]] for i in range(N) for j in range(N)}
        for i in range(N):
            for j in range(N):
                for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
                    if 0 <= x < N and 0 <= y < N:
                        d[(i, j)].extend(d.get((x, y), []))
    res = []
    while k > 0:
        for i in range(N):
            for j in range(N):
                if grid[i][j] in d[(i, j)]:
                    res.append(grid[i][j])
                    k -= 1
                    break
    return res
