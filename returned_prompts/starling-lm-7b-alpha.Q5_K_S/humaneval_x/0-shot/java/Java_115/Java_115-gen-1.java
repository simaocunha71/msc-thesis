        int m = grid.size();
        int n = grid.get(0).size();
        int[][] dp = new int[m][n];
        int[][] gridCopy = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                gridCopy[i][j] = grid.get(i).get(j);
                if (i > 0 && grid.get(i - 1).get(j) == 1) {
                    gridCopy[i][j] = gridCopy[i - 1][j] + 1;
                }
                if (j > 0 && grid.get(i).get(j - 1) == 1) {
                    gridCopy[i][j] = gridCopy[i][j - 1] + 1;
                }
            }
        }

        int total = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (gridCopy[i][j] > capacity) {
                    total++;
                    gridCopy[i][j] -= capacity;
                    gridCopy[i][j] %= capacity;
                    dp[i][j] = gridCopy[i][j];
                } else {
                    dp[i][j] = gridCopy[i][j];
                }
            }
        }

        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (i + 1 < m && j + 1 < n) {
                    dp[i][j] = Math.min(dp[i][j], dp[i + 1][j] + dp[i][j + 1]);
                } else if (i + 1 < m) {
                    dp[i][j] = Math.min(dp[i][j], dp[i + 1][j]);
