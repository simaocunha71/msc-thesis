  const m = grid.length;
  const n = grid[0].length;

  const dp = new Array(m);
  for (let i = 0; i < m; i++) {
    dp[i] = new Array(n);
    for (let j = 0; j < n; j++) {
      dp[i][j] = new Array(k + 1);
      for (let l = 0; l <= k; l++) {
        dp[i][j][l] = Infinity;
      }
    }
  }

  // Initialize
  dp[0][0][0] = grid[0][0];

  // Start
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      for (let k = 0; k < dp[i][j].length; k++) {
        if (i > 0 && j > 0 && dp[i - 1][j - 1][k] != Infinity) {
          dp[i][j][k] = Math.min(dp[i][j][k], dp[i - 1][j - 1][k] + grid[i][j]);
        }
        if (i > 0 && dp[i - 1][j][k] != Infinity) {
          dp[i][j][k] = Math.min(dp[i][j][k], dp[i - 1][j][k] + grid[i][j]);
        }
        if (j > 0 && dp[i][j - 1][k] != Infinity) {
          dp[i][j][k] = Math.min(dp[i][j][k], dp[i][j - 1][k] + grid[i][j]);
        }
      }
    }
  }

  // Result
  let min_path = [];
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
     