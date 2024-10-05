  let n = grid.length;
  let dp = Array.from({ length: k + 1 }, () => Array.from({ length: n }, () => Array.from({ length: n }, () => Infinity)));
  let directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];
  let path = Array.from({ length: k + 1 }, () => Array.from({ length: n }, () => Array.from({ length: n }, () => null)));

  dp[0][0][0] = grid[0][0];

  for (let i = 1; i < k + 1; i++) {
    for (let j = 0; j < n; j++) {
      for (let l = 0; l < n; l++) {
        for (let [dx, dy] of directions) {
          let nx = j + dx, ny = l + dy;
          if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
            let cost = dp[i - 1][j][l] + grid[nx][ny];
            if (cost < dp[i][nx][ny]) {
              dp[i][nx][ny] = cost;
              path[i][nx][ny] = path[i - 1][j][l];
            }
          }
        }
      }
    }
  }

  let min_cost = Infinity, min_x = 0, min_y = 0;
  for (let j = 0; j < n; j++) {
    for (let l = 0; l < n; l++) {
      if (dp[k][j][l] < min_cost) {
        min_cost = dp[k][j][l];
        min_x = j;
        min_y = l;
      }
    }
  }

  let result = [];
  let x = min_x, y = min_y;
  for (let i = k; i > 0; i--) {
    result.push(grid[x][y]);
    x = path[i][x][y][0];
    y = path[i][x][y][1];
  }
  result.push(grid[min_x][min_y]);

  return result.reverse();
}