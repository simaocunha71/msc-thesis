
from collections import deque


def minPath(grid, k):
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: List[int]
    """
    R, C = len(grid), len(grid[0])
    q = deque()
    for r in range(R):
        for c in range(C):
            q.append((r, c))
    if k == 1:
        return [grid[r][c] for r, c in q]

    lookup = [set() for _ in range(R * C + 1)]
    while q:
        r, c = q.popleft()
        if lookup[grid[r][c]]:
            continue
        lookup[grid[r][c]] = True

        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if not (0 <= nr < R) or not (0 <= nc < C):
                continue
            q.append((nr, nc))

    def dfs(grid, r, c, k, lookup, path, ret):
        """
        :type grid: List[List[int]]
        :type r: int
        :type c: int
        :type k: int
        :type lookup: List[set]
        :type path: List[int]
        :type ret: List[int]
        :rtype: List[int]
        """
        if k == 0:
            ret.append(path)
            return ret
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if not (0 <= nr < R) or not (0 <= nc < C):
                continue
            if grid[nr][nc] not in lookup[k]:
                path.append(grid[nr][nc])
                lookup[grid[nr][nc]] = True
                ret = dfs(grid, nr, nc, k -