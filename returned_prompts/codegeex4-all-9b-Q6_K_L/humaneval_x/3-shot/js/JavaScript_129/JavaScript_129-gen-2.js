  let n = grid.length;
  let dp = Array.from({ length: n }, () => Array.from({ length: n }, () => Array(k + 1).fill(Infinity)));
  let directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      dp[i][j][0] = grid[i][j];
    }
  }

  for (let step = 1; step <= k; step++) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        for (let [di, dj] of directions) {
          let ni = i + di;
          let nj = j + dj;
          if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
            dp[ni][nj][step] = Math.min(dp[ni][nj][step], dp[i][j][step - 1]);
          }
        }
      }
    }
  }

  let result = [];
  let i = 0, j = 0, step = k;
  while (step > 0) {
    result.push(grid[i][j]);
    for (let [di, dj] of directions) {
      let ni = i + di;
      let nj = j + dj;
      if (ni >= 0 && ni < n && nj >= 0 && nj < n && dp[ni][nj][step - 1] < dp[i][j][step]) {
        i = ni;
        j = nj;
        break;
      }
    }
    step--;
  }

  return result;
}