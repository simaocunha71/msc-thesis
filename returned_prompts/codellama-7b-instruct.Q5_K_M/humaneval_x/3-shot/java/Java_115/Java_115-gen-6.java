        int num_wells = grid.size();
        int[][] dp = new int[num_wells][num_wells];

        for (int i = 0; i < num_wells; i++) {
            for (int j = 0; j < num_wells; j++) {
                if (i == j) dp[i][j] = 0;
                else if (grid[i][j] == 0) dp[i][j] = 0;
                else dp[i][j] = Integer.MAX_VALUE;
            }
        }

        for (int i = 0; i < num_wells; i++) {
            for (int j = 0; j < num_wells; j++) {
                if (dp[i][j] == Integer.MAX_VALUE) continue;
                for (int k = 0; k < num_wells; k++) {
                    if (dp[i][k] == Integer.MAX_VALUE) continue;

                    dp[i][j] = Math.min(dp[i][j], dp[k][j] + 1);
                }
            }
        }

        int result = 0;
        for (int i = 0; i < num_wells; i++) {
            for (int j = 0; j < num_wells; j++) {
                if (dp[i][j] == Integer.MAX_VALUE) continue;
                result = Math.max(result, dp[i][j]);
            }
        }
        return result;

    }
}

