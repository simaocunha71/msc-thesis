  if (k == 0) {
    return;
  }
  visited[i][j] = true;
  path.push(grid[i][j]);
  if (i - 1 >= 0 && visited[i - 1][j] == false && grid[i - 1][j] == grid[i][j]) {
    dfs(grid, visited, i - 1, j, k - 1);
  }
  if (i + 1 < visited.length && visited[i + 1][j] == false && grid[i + 1][j] == grid[i][j]) {
    dfs(grid, visited, i + 1, j, k - 1);
  }
  if (j - 1 >= 0 && visited[i][j - 1] == false && grid[i][j - 1] == grid[i][j]) {
    dfs(grid, visited, i, j - 1, k - 1);
  }
  if (j + 1 < visited[0].length && visited[i][j + 1] == false && grid[i][j + 1] == grid[i][j]) {
