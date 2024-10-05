        int N = grid.size();
        int[][][] dp = new int[N][N][k + 1];
        for (int[][] d : dp) {
            for (int[] d1 : d) {
                Arrays.fill(d1, Integer.MAX_VALUE);
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                dp[i][j][0] = grid.get(i).get(j);
            }
        }

        for (int len = 1; len <= k; len++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (i - 1 >= 0) {
                        dp[i][j][len] = Math.min(dp[i - 1][j][len - 1] + grid.get(i).get(j),
                                                 dp[i][j][len]);
                    }
                    if (j - 1 >= 0) {
                        dp[i][j][len] = Math.min(dp[i][j - 1][len - 1] + grid.get(i).get(j),
                                                 dp[i][j][len]);
                    }
                }
            }
        }

        List<Integer> result = new ArrayList<>();
        for (int i = N - 1; i >= 0; i--) {
            for (int j = N - 1; j >= 0; j--) {
                if (i - 1 >= 0 || j - 1 >= 0) {
                    result.add(dp[i][j][k]);
                }
            }
        }
        Collections.reverse(result);
        return result;
    }
}

