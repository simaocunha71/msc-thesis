  const rows = grid.length;
  const cols = grid[0].length;
  const visited = Array(rows).fill(0).map(() => Array(cols).fill(false));
  const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
  let minPath = null;
  let minPathValue = null;

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      const currentValue = grid[i][j];
      const path = [currentValue];
      const dfs = (i, j, k, path) => {
        if (k === 0) {
          if (!minPath || path.join('') < minPathValue) {
            minPath = path;
            minPathValue = path.join('');
          }
          return;
        }
        for (const [di, dj] of directions) {
          const ni = i + di;
          const nj = j + dj;
          if (ni >= 0 && ni < rows && nj >= 0 && nj < cols && !visited[ni][nj]) {
            visited[ni][nj] = true;
            dfs(ni, nj, k - 1, [...path, grid[ni][nj]]);
            visited[ni][nj] = false;
          }
        }
      };
      dfs(i, j, k, path);
    }
  }
  return minPath;
}