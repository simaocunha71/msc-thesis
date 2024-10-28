        int n = grid.size();
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = grid.get(i).get(j);
            }
        }
        int[][] dirs = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };
        int[][][] dp2 = new int[n][n][k + 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i < n - 1 && grid.get(i).get(j) < grid.get(i + 1).get(j)) {
                    dp2[i][j][1] = grid.get(i).get(j);
                } else {
                    dp2[i][j][1] = grid.get(i + 1).get(j);
                }
            }
        }
        for (int len = 2; len <= k; len++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    int max = -1;
                    for (int[] dir : dirs) {
                        int ni = i + dir[0];
                        int nj = j + dir[1];
                        if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                            if (dp2[ni][nj][len - 1] > max) {
                                max = dp2[ni][nj][len - 1];
                            }
                        }
                    }
                    dp2[i][j][len] = max;
                }
            }
        }
        int[][] dp3 = new int[n][n];
        for (int i = 0; i < n; i++) {
            for