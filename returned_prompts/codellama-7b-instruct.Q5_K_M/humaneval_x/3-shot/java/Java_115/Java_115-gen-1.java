        int m = grid.size();
        int n = grid.get(0).size();
        int[][] dp = new int[m][n];

        int ans = 0;
        int cur_capacity = capacity;

        // fill the first row with 0
        for (int j = 0; j < n; j++) dp[0][j] = 0;

        // fill the first column with 0
        for (int i = 0; i < m; i++) dp[i][0] = 0;

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (grid.get(i).get(j) == 0) {
                    dp[i][j] = 0;
                } else {
                    dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + 1;
                }

                if (dp[i][j] <= cur_capacity) {
                    cur_capacity -= dp[i][j];
                    ans += dp[i][j];
                } else {
                    break;
                }
            }
        }
        return ans;
    }
}

