        int m = grid.size();
        int n = grid.get(0).size();
        int[][] dp = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid.get(i).get(j) == 0) {
                    dp[i][j] = 0;
                } else {
                    dp[i][j] = 1;
                }
            }
        }

        int max_fill = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid.get(i).get(j) == 1 && j > 0) {
                    dp[i][j] = Math.min(dp[i][j], dp[i][j-1] + 1);
                }

                if (grid.get(i).get(j) == 1 && j < n-1) {
                    dp[i][j] = Math.min(dp[i][j], dp[i][j+1] + 1);
                }

                if (grid.get(i).get(j) == 1 && i > 0) {
                    dp[i][j] = Math.min(dp[i][j], dp[i-1][j] + 1);
                }

                if (grid.get(i).get(j) == 1 && i < m-1) {
                    dp[i][j] = Math.min(dp[i][j], dp[i+1][j] + 1);
                }

                max_fill = Math.max(max_fill, dp[i][j]);
            }
        }

        return max_fill;
    }
}

