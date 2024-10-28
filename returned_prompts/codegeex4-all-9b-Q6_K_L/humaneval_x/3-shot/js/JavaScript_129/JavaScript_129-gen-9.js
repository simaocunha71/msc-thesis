  var n = grid.length;
  var dp = Array(n).fill(0).map(() => Array(n).fill(Infinity));
  var directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];

  for (var i = 0; i < n; i++) {
    for (var j = 0; j < n; j++) {
      dp[i][j] = grid[i][j];
    }
  }

  for (var step = 1; step < k; step++) {
    for (var i = 0; i < n; i++) {
      for (var j = 0; j < n; j++) {
        for (var [dx, dy] of directions) {
          var ni = i + dx;
          var nj = j + dy;
          if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
            dp[i][j] = Math.min(dp[i][j], dp[ni][nj] + grid[i][j]);
          }
        }
      }
    }
  }

  var result = [];
  var [x, y] = [0, 0];
  result.push(grid[x][y]);
  for (var step = 1; step < k; step++) {
    for (var [dx, dy] of directions) {
      var ni = x + dx;
      var nj = y + dy;
      if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
        if (grid[ni][nj] < grid[x][y]) {
          x = ni;
          y = nj;
          result.push(grid[x][y]);
          break;
        }
      }
    }
  }

  return result;
}