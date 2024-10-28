        int m = grid.size();
        int n = grid.get(0).size();
        int[][] dp = new int[m+1][n+1];
        for (int i = 0; i <= m; i++) {
            Arrays.fill(dp[i], -1);
        }

        return maxFill(grid, m, n, capacity, dp);
    }

    private int maxFill(List<List<Integer>> grid, int m, int n, int capacity, int[][] dp) {
        if (m == 0 || n == 0) return 0;

        if (dp[m][n] != -1) return dp[m][n];

        int res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid.get(i).get(j) == 0) continue;
                int currCapacity = grid.get(i).get(j);
                if (currCapacity > capacity) continue;

                int left = maxFill(grid, i, j, capacity - currCapacity, dp);
                int right = maxFill(grid, m-1, n-1, capacity - currCapacity, dp);

                res = Math.max(res, left + right + 1);
            }
        }

        dp[m][n] = res;
        return res;
    }
}