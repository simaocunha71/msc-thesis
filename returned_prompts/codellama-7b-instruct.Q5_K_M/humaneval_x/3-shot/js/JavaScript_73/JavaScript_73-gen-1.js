  const n = arr.length;
  const dp = new Array(n).fill(0).map(() => new Array(n).fill(0));
  for (let i = 0; i < n; i++) {
    dp[i][i] = 0;
  }
  for (let i = n - 1; i >= 1; i--) {
    for (let j = i + 1; j < n; j++) {
      dp[i][j] = Infinity;
      for (let k = i; k <= j; k++) {
        dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k + 1][j] + 1);
      }
    }
  }
  return dp[0][n - 1];
}



