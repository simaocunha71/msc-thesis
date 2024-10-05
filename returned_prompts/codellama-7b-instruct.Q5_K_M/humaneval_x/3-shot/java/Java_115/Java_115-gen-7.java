        int rows = grid.size();
        int cols = grid.get(0).size();

        int[][] dp = new int[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                dp[i][j] = 1;
            }
        }

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid.get(i).get(j) == 0) continue;
                if (i == 0 && j == 0) continue;

                dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]);
            }
        }

        int result = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid.get(i).get(j) == 0) continue;
                result += dp[i][j];
            }
        }
        return result;
    }
}

