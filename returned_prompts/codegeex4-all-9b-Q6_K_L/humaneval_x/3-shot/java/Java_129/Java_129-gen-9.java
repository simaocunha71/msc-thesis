        List<Integer> result = new ArrayList<>();
        int n = grid.size();

        int[][] dp = new int[n][n];
        for (int[] row : dp) {
            Arrays.fill(row, Integer.MAX_VALUE);
        }

        dp[0][0] = grid.get(0).get(0);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i > 0) {
                    dp[i][j] = Math.min(dp[i][j], dp[i - 1][j] + grid.get(i).get(j));
                }
                if (j > 0) {
                    dp[i][j] = Math.min(dp[i][j], dp[i][j - 1] + grid.get(i).get(j));
                }
            }
        }

        int i = n - 1;
        int j = n - 1;
        while (i > 0 || j > 0) {
            result.add(0, grid.get(i).get(j));

            if (i > 0 && dp[i - 1][j] < dp[i][j - 1]) {
                i -= 1;
            } else {
                j -= 1;
            }
        }
        result.add(0, grid.get(0).get(0));
        return result;

    }
}

