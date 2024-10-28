        if (n <= 0) {
            return 0;
        }
        if (n == 1) {
            return 0;
        }
        if (n == 2) {
            return 1;
        }

        int[][] dp = new int[n+1][3];
        dp[0][0] = 0;
        dp[0][1] = 0;
        dp[0][2] = 1;
        dp[1][0] = 0;
        dp[1][1] = 0;
        dp[1][2] = 1;
        for (int i = 2; i <= n; i++) {
            dp[i][0] = dp[i-1][0];
            dp[i][1] = dp[i-1][1];
            dp[i][2] = dp[i-1][2];
            int temp = dp[i-2][0] + dp[i-3][1] + dp[i-3][2];
            dp[i][0] = temp;
            dp[i][1] = temp;
            dp[i][2] = temp;
        }
        return dp[n][0] + dp[n][1] + dp[n][2];
    }
}











































































































































































































