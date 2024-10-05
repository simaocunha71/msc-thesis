        int m = grid.size();
        int n = grid.get(0).size();
        int[][] dp = new int[m][n];

        int max_fill = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid.get(i).get(j) == 1) {
                    dp[i][j] = 1;
                }
                max_fill = Math.max(max_fill, dp[i][j]);
            }
        }

        while (true) {
            int[][] dp_new = new int[m][n];
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (grid.get(i).get(j) == 1) {
                        dp_new[i][j] = 1;
                    } else {
                        for (int k = Math.max(0, i - 1); k <= Math.min(i + 1, m - 1); k++) {
                            for (int l = Math.max(0, j - 1); l <= Math.min(j + 1, n - 1); l++) {
                                dp_new[i][j] = Math.max(dp_new[i][j], dp[k][l] + 1);
                            }
                        }
                    }
                }
            }
            if (Arrays.deepEquals(dp, dp_new)) break;
            dp = dp_new;
        }

        return max_fill;
    }
}

