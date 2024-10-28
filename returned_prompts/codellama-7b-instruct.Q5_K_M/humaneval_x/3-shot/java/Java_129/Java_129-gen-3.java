        int N = grid.size();
        int[][] dp = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                dp[i][j] = grid.get(i).get(j);
            }
        }

        for (int step = 1; step < k; step++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (dp[i][j] == 0) continue;

                    int min = Integer.MAX_VALUE;

                    if (i - 1 >= 0 && dp[i - 1][j] != 0) min = Math.min(min, dp[i - 1][j]);
                    if (j - 1 >= 0 && dp[i][j - 1] != 0) min = Math.min(min, dp[i][j - 1]);
                    if (i + 1 < N && dp[i + 1][j] != 0) min = Math.min(min, dp[i + 1][j]);
                    if (j + 1 < N && dp[i][j + 1] != 0) min = Math.min(min, dp[i][j + 1]);

                    dp[i][j] = Math.min(dp[i][j], min);
                }
            }
        }

        int min = Integer.MAX_VALUE;
        int index = 0;
        int[] res = new int[k];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (dp[i][j] == 0) continue;

                min = Math.min(min, dp[i][j]);
                res[index] = grid.get(i).get(j);
                index++;
            }
        }

        return Arrays.