        int N = grid.size();
        int M = grid.get(0).size();
        List<Integer> result = new ArrayList<>();
        int[][] dp = new int[N][M];
        int[][] min_path = new int[N][M];

        // Initialize the DP table
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                dp[i][j] = -1;
                min_path[i][j] = -1;
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (i == 0 && j == 0) {
                    dp[i][j] = 0;
                    min_path[i][j] = 0;
                } else if (i == 0) {
                    dp[i][j] = dp[i][j - 1] + 1;
                    min_path[i][j] = j - 1;
                } else if (j == 0) {
                    dp[i][j] = dp[i - 1][j] + 1;
                    min_path[i][j] = i - 1;
                } else {
                    if (dp[i - 1][j] == -1 && dp[i][j - 1] == -1) {
                        dp[i][j] = -1;
                        min_path[i][j] = -1;
                    } else if (dp[i - 1][j] == -1) {
                        dp[i][j] = dp[i][j - 1] + 1;
                        min_path[i][j] = j - 1;
                    } else if (dp[i][j - 1] == -1) {
                        dp[i][j] = dp[i - 1][j] + 1;
                        min_path[i][j