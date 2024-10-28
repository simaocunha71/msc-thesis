    int n = grid.size();
    int m = grid.get(0).size();
    int[][] dp = new int[n][m];
    int res = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid.get(i).get(j) == 1) {
                dp[i][j] = 1;
            } else {
                dp[i][j] = 0;
            }
        }
    }
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid.get(i).get(j) == 0) {
                continue;
            }
            dp[i][j] += Math.min(dp[i-1][j], capacity);
        }
    }
    for (int j = 1; j < m; j++) {
        for (int i = 0; i < n; i++) {
            if (grid.get(i).get(j) == 0) {
                continue;
            }
            dp[i][j] += Math.min(dp[i][j-1], capacity);
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            res = Math.max(res, dp[i][j]);
        }
    }
    return res;
    }
}

































































































































