  let n = grid.length;
  let dp = new Array(n).fill(0).map(() => new Array(n).fill(Infinity));
  let directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
  let min = Infinity;

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] < min) {
        min = grid[i][j];
      }
      dp[i][j] = min;
    }
  }

  for (let l = 2; l <= k; l++) {
    let newDp = new Array(n).fill(0).map(() => new Array(n).fill(Infinity));
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        for (let [dx, dy] of directions) {
          let x = i + dx;
          let y = j + dy;
          if (x >= 0 && x < n && y >= 0 && y < n) {
            newDp[i][j] = Math.min(newDp[i][j], dp[x][y]);
          }
        }
        newDp[i][j] += grid[i][j];
      }
    }
    dp = newDp;
  }

  let result = [];
  let minVal = Infinity;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (dp[i][j] < minVal) {
        minVal = dp[i][j];
      }
    }
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (dp[i][j] == minVal) {
        result.push(grid[i][j]);
      }
    }
  }

  return result;
}