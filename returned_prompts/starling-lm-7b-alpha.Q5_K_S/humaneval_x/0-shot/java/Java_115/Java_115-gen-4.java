    int n = grid.size();
    int m = grid.get(0).size();
    int[][] dp = new int[n][m];
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(grid.get(i).get(j) == 1) {
                dp[i][j] = 1;
            }
        }
    }

    for(int i = 1; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(grid.get(i).get(j) == 1) {
                dp[i][j] = dp[i-1][j] + 1;
            }
        }
    }

    for(int i = 0; i < m; i++) {
        for(int j = 1; j < n; j++) {
            if(grid.get(j).get(i) == 1) {
                dp[j][i] = dp[j-1][i] + 1;
            }
        }
    }

    int res = 0;
    int sum = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(grid.get(i).get(j) == 1) {
                int l = Math.min(dp[i][j], dp[i][j+1]);
                int r = Math.min(dp[i][j], dp[i+1][j]);
                int min = Math.min(l, r);
                sum += min;
                res = Math.max(res, sum/capacity);
            }
        }
    }

    return res;
}
}


























































