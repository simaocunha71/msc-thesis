    def helper(grid, sr, sc, k):
        n = len(grid)
        if k == 0:
            return []
        if sr < 0 or sc < 0 or sr >= n or sc >= n:
            return None
        original = grid[sr][sc]
        grid[sr][sc] = 0
        moves = [helper(grid, sr - 1, sc, k - 1),
                 helper(grid, sr + 1, sc, k - 1),
                 helper(grid, sr, sc - 1, k - 1),
                 helper(grid, sr, sc + 1, k - 1)]
        moves = [i for i in moves if i is not None]
        if not moves:
            return [original]
        min_path = min(moves,