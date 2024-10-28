        int n = grid.size();
        int[][] dp = new int[n][n];
        int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = 100000000;
            }
        }
        dp[0][0] = grid.get(0).get(0);

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < n; j++) {
                for (int[] d : dir) {
                    int x = i + d[0];
                    int y = j + d[1];
                    if (x >= 0 && x < n && y >= 0 && y < n) {
                        dp[i][j] = Math.min(dp[i][j], dp[x][y] + 1);
                    }
                }
            }
        }

        return null;
    }
}

