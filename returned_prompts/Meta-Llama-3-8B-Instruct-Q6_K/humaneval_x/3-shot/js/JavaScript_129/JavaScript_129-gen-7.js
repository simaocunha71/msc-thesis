  let n = grid.length;
  let minPath = [];
  let minPathSum = Infinity;
  let minPathSumArr = [];
  let visited = new Array(n).fill(false).map(() => new Array(n).fill(false));

  function dfs(i, j, pathSum, path) {
    if (path.length === k) {
      if (pathSum < minPathSum) {
        minPathSum = pathSum;
        minPathSumArr = path;
        minPath = path.slice();
      }
      return;
    }
    for (let ni = Math.max(0, i - 1); ni <= Math.min(n - 1, i + 1); ni++) {
      for (let nj = Math.max(0, j - 1); nj <= Math.min(n - 1, j + 1); nj++) {
        if (!visited[ni][nj]) {
          visited[ni][nj] = true;
          dfs(ni, nj, pathSum + grid[ni][nj], [...path, grid[ni][nj]]);
          visited[ni][nj] = false;
        }
      }
    }
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      dfs(i, j, grid[i][j], [grid[i][j]]);
    }
  }
  return minPath;
}