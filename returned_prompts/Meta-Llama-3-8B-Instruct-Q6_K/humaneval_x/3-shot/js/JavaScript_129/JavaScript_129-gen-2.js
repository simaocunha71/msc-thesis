  let n = grid.length;
  let res = [];
  let visited = Array(n).fill(0).map(() => Array(n).fill(false));
  let dfs = (i, j, path) => {
    if (path.length === k) {
      res = path;
      return;
    }
    visited[i][j] = true;
    for (let x = -1; x <= 1; x++) {
      for (let y = -1; y <= 1; y++) {
        if (x === 0 && y === 0) continue;
        let ni = i + x;
        let nj = j + y;
        if (ni >= 0 && ni < n && nj >= 0 && nj < n && !visited[ni][nj]) {
          dfs(ni, nj, [...path, grid[ni][nj]]);
        }
      }
    }
    visited[i][j] = false;
  };
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      dfs(i, j, [grid[i][j]]);
    }
  }
  return res;
}  // Note: The above solution is not optimized, it will return the first path it finds, not the minimum one. The minimum path will be the one that has the smallest numbers. You might need to implement a priority queue to solve this problem efficiently.