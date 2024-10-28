        int n_rows = grid.size();
        int n_cols = grid.get(0).size();

        int[][] dp = new int[n_rows][n_cols];

        for (int i = 0; i < n_rows; i++) {
            for (int j = 0; j < n_cols; j++) {
                if (grid.get(i).get(j) == 1) {
                    dp[i][j] = 1;
                }
            }
        }

        for (int i = 1; i < n_rows; i++) {
            for (int j = 1; j < n_cols; j++) {
                if (grid.get(i).get(j) == 1) {
                    dp[i][j] = Math.min(dp[i][j - 1] + 1, dp[i - 1][j] + 1);
                }
            }
        }

        int result = 0;
        for (int i = 0; i < n_rows; i++) {
            for (int j = 0; j < n_cols; j++) {
                result += dp[i][j];
            }
        }
        return result;
    }
}
