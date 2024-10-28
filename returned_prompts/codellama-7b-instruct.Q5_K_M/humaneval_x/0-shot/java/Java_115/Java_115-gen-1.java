        int result = 0;
        int row = grid.size();
        int col = grid[0].size();

        boolean[][] visited = new boolean[row][col];
        int[][] dp = new int[row][col];
        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                if (grid[i][j] == 0) {
                    dp[i][j] = 0;
                } else {
                    dp[i][j] = capacity;
                }
            }
        }

        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                if (grid[i][j] == 0) {
                    continue;
                }
                if (visited[i][j]) {
                    continue;
                }
                visited[i][j] = true;

                int max = 0;
                for (int k = 0; k < col; ++k) {
                    if (visited[i][k]) {
                        continue;
                    }
                    max = Math.max(max, dp[i][k]);
                }

                for (int k = 0; k < col; ++k) {
                    if (visited[i][k]) {
                        continue;
                    }
                    if (max - dp[i][k] < 0) {
                        continue;
                    }
                    visited[i][k] = true;
                    dp[i][k] = max - dp[i][k];
                    result++;
                }
            }
        }

        return result;
    }
}

