        int n = grid.size();
        int[][] dp = new int[k+1][n*n+1];
        int[][] next = new int[k+1][n*n+1];
        for (int i = 0; i <= k; i++) {
            for (int j = 0; j <= n*n; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        dp[0][0] = 0;
        for (int i = 1; i <= k; i++) {
            for (int j = 1; j <= n*n; j++) {
                for (int l = 1; l <= n; l++) {
                    for (int m = 1; m <= n; m++) {
                        if (Math.abs(l-m) > 1 || Math.abs(l-m) > i || grid[l-1][m-1] > j) continue;
                        if (dp[i-1][j-grid[l-1][m-1]] + grid[l-1][m-1] < dp[i][j]) {
                            dp[i][j] = dp[i-1][j-grid[l-1][m-1]] + grid[l-1][m-1];
                            next[i][j] = grid[l-1][m-1];
                        }
                    }
                }
            }
        }
        List<Integer> result = new ArrayList<>();
        int i = k, j = n*n;
        while (i > 0) {
            result.add(next[i][j]);
            j -= next[i][j];
            i--;
        }
        Collections.reverse(result);
        return result;
    }
}

This is a dynamic programming problem. We create a 2D array dp to store the minimum path sum for each length and each value. We also create a 2D array next to store the next cell in the path.

We iterate over each cell in the grid and for each cell, we try to move to all its neighbors. If the move is valid (i