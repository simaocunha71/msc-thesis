        int m = grid.size();
        int n = grid.get(0).size();

        int[][] dp = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid.get(i).get(j) == 1) {
                    dp[i][j] = 1;
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dp[i][j] == 0) continue;

                if (i == 0 && j == 0) continue;

                if (i == 0) {
                    if (j - 1 >= 0 && dp[i][j - 1] > 0) {
                        dp[i][j] += dp[i][j - 1];
                    }
                } else if (j == 0) {
                    if (i - 1 >= 0 && dp[i - 1][j] > 0) {
                        dp[i][j] += dp[i - 1][j];
                    }
                } else {
                    if (i - 1 >= 0 && j - 1 >= 0 && dp[i - 1][j] > 0 && dp[i][j - 1] > 0) {
                        dp[i][j] += Math.min(dp[i][j - 1], dp[i - 1][j]);
                    }
                }

                if (dp[i][j] > capacity) {
                    return -1;
                }
            }
        }

        int res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dp[i][j] > 0) {
                    res += 1;
                }
            }
       