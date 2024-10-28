    int N = grid.size();
    vector<vector<int>> dp(N*N+1, vector<int>(k+1, INT_MAX));
    dp[0][0] = 0;
    for (int n = 1; n <= N*N; ++n)
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                if (grid[i][j] == n)
                    for (int l = 0; l < k; ++l)
                        dp[n][l+1] = min(dp[n][l+1], dp[n-1][l]);
    vector<int> path(k);
    int n = N*N, l = k;
    while (l > 0) {
        path[--l] = n;
        for (int m = n-1; m >= 0; --m)
            if (dp[m][l] < dp[n][l]) {
                n = m;
                break;
            }
    }
    return path;
}


