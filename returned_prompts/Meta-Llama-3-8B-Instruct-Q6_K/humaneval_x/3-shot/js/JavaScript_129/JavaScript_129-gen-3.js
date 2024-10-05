  let n = grid.length;
  let result = [];
  let visited = Array(n * n).fill(false);
  let minPath = [];
  let minPathValue = Infinity;

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      let value = grid[i][j];
      if (!visited[value - 1]) {
        visited[value - 1] = true;
        let path = [];
        dfs(grid, i, j, k, value, visited, path);
        if (path.length < minPathValue) {
          minPathValue = path.length;
          minPath = path;
          result = path;
        }
        visited[value - 1] = false;
      }
    }
  }

  return result;

  function dfs(grid, i, j, k, value, visited, path) {
    if (k == 0) {
      return;
    }
    path.push(value);
    visited[value - 1] = true;
    let directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    for (let direction of directions) {
      let ni = i + direction[0];
      let nj = j + direction[1];
      if (ni >= 0 && ni < n && nj >= 0 && nj < n && !visited[grid[ni][nj] - 1]) {
        dfs(grid, ni, nj, k - 1, grid[ni][nj], visited, path);
      }
    }
    path.pop();
    visited[value - 1] = false;
  }
}