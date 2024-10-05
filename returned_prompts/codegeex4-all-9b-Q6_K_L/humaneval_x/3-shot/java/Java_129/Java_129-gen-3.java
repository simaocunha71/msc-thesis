        List<Integer> result = new ArrayList<>();
        int n = grid.size();
        int[][][] dp = new int[n][n][k + 1];
        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int l = 0; l <= k; l++) {
                    dp[i][j][l] = Integer.MAX_VALUE;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) {
                    dp[0][0][0] = grid.get(0).get(0);
                } else {
                    for (int[] direction : directions) {
                        int new_i = i + direction[0];
                        int new_j = j + direction[1];
                        if (new_i >= 0 && new_i < n && new_j >= 0 && new_j < n) {
                            for (int l = 1; l <= k; l++) {
                                dp[i][j][l] = Math.min(dp[i][j][l], dp[new_i][new_j][l - 1] + grid.get(i).get(j));
                            }
                        }
                    }
                }
            }
        }

        int min_value = Integer.MAX_VALUE;
        int min_i = -1;
        int min_j = -1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dp[i][j][k] < min_value) {
                    min_value = dp[i][j][k];
                    min_i = i;
                    min_j = j;
                }
            }
        }

        while (min_i != 0 || min_j != 0) {
            result.add(grid.get(min_i).get(min_j));
            for (int[] direction : directions) {
                int new_i = min_i + direction[0];
                int new_j = min_j + direction[1];
                if (new_i >= 0 && new_i < n && new_j >= 0 && new_j < n && dp