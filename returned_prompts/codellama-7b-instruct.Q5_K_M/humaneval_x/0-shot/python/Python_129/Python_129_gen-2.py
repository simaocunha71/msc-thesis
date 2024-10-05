
def minPath(grid, k):
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: List[int]
    """
    N = len(grid)
    assert N >= 2 and k >= 0
    m = [[float('inf') for _ in range(N)] for _ in range(N)]
    for i in range(N):
        m[i][i] = 0
    for i in range(N):
        for j in range(i + 1, N):
            m[i][j] = 1
    for i in range(N - 1, -1, -1):
        for j in range(i + 1, N):
            m[i][j] = min(m[i][j], m[i][j - 1] + 1)
    ans = []
    for i in range(N):
        for j in range(i + 1, N):
            if m[i][j] == k:
                ans.append(grid[i][j - 1])
                break
    return ans
