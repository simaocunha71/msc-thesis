  const n = grid.length;
  const dp = Array.from({ length: n }, () => Array.from({ length: k + 1 }, () => Array(n).fill(Infinity)));
  const directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];
  const visited = Array.from({ length: n }, () => Array(n).fill(false));

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      dp[i][1][j] = grid[i][j];
    }
  }

  for (let step = 2; step <= k; step++) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        for (const [di, dj] of directions) {
          const ni = i + di;
          const nj = j + dj;
          if (ni >= 0 && ni < n && nj >= 0 && nj < n && !visited[ni][nj]) {
            dp[ni][step][nj] = Math.min(dp[ni][step][nj], dp[i][step - 1][j] + grid[ni][nj]);
          }
        }
      }
    }
    visited.fill(false);
  }

  let min_value = Infinity;
  let min_index = -1;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (dp[i][k][j] < min_value) {
        min_value = dp[i][k][j];
        min_index = j;
      }
    }
  }

  const result = [];
  let i = min_index;
  let j = k;
  while (j > 1) {
    result.unshift(grid[i][j - 2]);
    for (const [di, dj] of directions) {
      const ni = i + di;
      const nj = j + dj;
      if (ni >= 0 && ni < n && nj >= 0 && nj < n && dp[ni][j - 1][nj] == dp[i][j - 2][j] + grid[ni][nj]) {
        i = ni;
        j -= 1;
        break;
     