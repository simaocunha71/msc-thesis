        if (n < 4 || n % 2 == 1) {
            return false;
        }
        if (n == 4 || n == 6 || n == 10) {
            return false;
        }
        if (n == 8) {
            return true;
        }
        if (n % 4 != 0) {
            return false;
        }
        int[][] dp = new int[20][n + 1];
        for (int i = 2; i < 11; i++) {
            dp[i][0] = 1;
        }
        for (int i = 2; i < 11; i++) {
            for (int j = 2; j <= n / 4; j++) {
                if (i * j <= n) {
                    dp[i][j * i] = 1;
                }
                if (i * j * 2 <= n) {
                    dp[i][j * i * 2] = 1;
                }
                if (i * j * 3 <= n) {
                    dp[i][j * i * 3] = 1;
                }
                if (i * j * 4 <= n) {
                    dp[i][j * i * 4] = 1;
                }
            }
        }
        for (int i = 2; i < 11; i++) {
            if (dp[i][n / 4 * i] == 1) {
                return true;
            }
        }
        return false;
    }
}






















































































































