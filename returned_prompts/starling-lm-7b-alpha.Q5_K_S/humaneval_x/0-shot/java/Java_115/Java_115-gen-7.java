    int m = grid.size();
    int n = grid.get(0).size();

    int[][] dp = new int[m][n];
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            dp[i][j] = grid.get(i).get(j);
        }
    }

    for(int i = 1; i < m; i++) {
        for(int j = 0; j < n; j++) {
            dp[i][j] += dp[i - 1][j];
        }
    }

    for(int j = 1; j < n; j++) {
        for(int i = 0; i < m; i++) {
            dp[i][j] += dp[i][j - 1];
        }
    }

    int res = 0;
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            int left = j == 0 ? 0 : dp[i][j - 1];
            int up = i == 0 ? 0 : dp[i - 1][j];
            int dn = i == 0 ? 0 : dp[i][j];
            int lf = left + up - dn;
            if(lf <= capacity) {
                res++;
            } else {
                res += lf / capacity;
            }
        }
    }
    return res;
}
}


































































































































