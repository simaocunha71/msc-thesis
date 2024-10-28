        int result = 0;
        int n = grid.size();
        int m = grid.get(0).size();
        int[][] dp = new int[n + 1][m + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (grid.get(i - 1).get(j - 1) == 1) {
                    dp[i][j] = Math.min(dp[i - 1][j], Math.min(dp[i][j - 1], dp[i - 1][j - 1])) + 1;
                } else {
                    dp[i][j] = 0;
                }
                if (dp[i][j] == capacity) {
                    result += 1;
                    dp[i][j] = 0;
                }
            }
        }
        return result;
    }
}


```