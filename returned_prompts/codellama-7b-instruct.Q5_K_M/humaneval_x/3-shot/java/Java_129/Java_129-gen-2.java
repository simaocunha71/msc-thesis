        int N = grid.size();
        int M = grid.get(0).size();
        int[][] dp = new int[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                dp[i][j] = grid.get(i).get(j);
            }
        }

        for (int d = 1; d < k; d++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    int up = i - 1 < 0 ? Integer.MAX_VALUE : dp[i - 1][j];
                    int down = i + 1 >= N ? Integer.MAX_VALUE : dp[i + 1][j];
                    int left = j - 1 < 0 ? Integer.MAX_VALUE : dp[i][j - 1];
                    int right = j + 1 >= M ? Integer.MAX_VALUE : dp[i][j + 1];

                    dp[i][j] = Math.min(up, Math.min(down, Math.min(left, right)));
                }
            }
        }

        int min = Integer.MAX_VALUE;
        int index = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (dp[i][j] < min) {
                    min = dp[i][j];
                    index = dp[i][j];
                }
            }
        }

        List<Integer> result = new ArrayList<>();
        result.add(index);

        return result;

    }
}

