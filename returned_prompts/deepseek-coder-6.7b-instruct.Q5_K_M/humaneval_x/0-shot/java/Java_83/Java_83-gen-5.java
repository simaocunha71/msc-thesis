        int count = 0;

        if (n == 1) {
            return 2;
        } else if (n <= 0) {
            return 0;
        } else {
            int[][] dp = new int[n][10];
            dp[0][1] = 1;
            dp[0][0] = 1;

            for(int i = 1; i < n; i++){
                dp[i][0] = dp[i-1][4] + dp[i-1][6] + dp[i-1][8];
                dp[i][1] = dp[i-1][6];
                dp[i][2] = dp[i-1][5] + dp[i-1][7];
                dp[i][3] = dp[i-1][5];
                dp[i][4] = dp[i-1][0] + dp[i-1][2] + dp[i-1][8];
                dp[i][5] = dp[i-1][0] + dp[i-1][1] + dp[i-1][7] + dp[i-1][9];
                dp[i][6] = dp[i-1][0] + dp[i-1][3] + dp[i-1][7] + dp[i-1][9];
                dp[i][7] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][4] + dp[i-1][6] + dp[i-1][9];
                dp[i][8] = dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4] + dp[i-1][5] + dp[i-1][9];
                dp[i][9] = dp[i-1][0] + dp[i-1][1] +