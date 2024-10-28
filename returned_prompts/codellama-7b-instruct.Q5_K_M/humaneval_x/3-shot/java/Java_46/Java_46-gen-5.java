        int[] dp = new int[n+1];

        dp[0] = 0;
        dp[1] = 0;
        dp[2] = 2;
        dp[3] = 0;

        for (int i = 4; i <= n; i++) {
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4];
        }
        return dp[n];
    }
}

