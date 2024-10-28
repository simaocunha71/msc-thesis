  // initialize the 2D dp array with maximum value
  let dp = new Array(grid.length);
  for (let i = 0; i < grid.length; i++) {
    dp[i] = new Array(grid[i].length).fill(Number.MAX_VALUE);
  }

  // initialize the 2D visited array with false
  let visited = new Array(grid.length);
  for (let i = 0; i < grid.length; i++) {
    visited[i] = new Array(grid[i].length).fill(false);
  }

  // directions array for the 4 possible moves
  let dir = [[0, 1], [1, 0], [0, -1], [-1, 0]];

  // dfs helper function
  const dfs = (x, y, k) => {
    if (k === 0) return [grid[x][y]];
    let path = [];
    for (let i = 0; i < 4; i++) {
      let nx = x + dir[i][0], ny = y + dir[i][1];
      if (nx >= 0 && nx < grid.length && ny >= 0 && ny < grid[0].length && !visited[nx][ny]) {
        visited[nx][ny] = true;
        let tempPath = dfs(nx, ny, k - 1);
        if (tempPath.length > 0) {
          tempPath.push(grid[x][y]);
          if (path.length === 0 || tempPath < path) {
            path = tempPath;
          }
        }
        visited[nx][ny] = false;
      }
    }
    return path;
  }

  // start from each cell and get the minimum path
  let minPath = [];
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      visited[i][j] = true;
      let path = dfs(i, j, k - 1);
     