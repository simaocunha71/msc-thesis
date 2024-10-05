    int n = grid.size();
    vector<vector<int>> dp(n * n + 1, vector<int>(k + 1, INT_MAX));
    dp[0][0] = 0;
    for (int i = 1; i <= n * n; ++i) {
        for (int j = 1; j <= min(i, k); ++j) {
            for (int p = 1; p <= j; ++p) {
                dp[i][j] = min(dp[i][j], max(dp[i - 1][j - p], grid[i / n][i % n]));
            }
        }
    }
    vector<int> res;
    int i = n * n, j = k;
    while (j > 0) {
        for (int p = 1; p <= j; ++p) {
            if (dp[i][j] == max(dp[i - 1][j - p], grid[i / n][i % n])) {
                res.push_back(grid[i / n][i % n]);
                i -= 1;
                j -= p;
                break;
            }
        }
    }
    reverse(res.begin(), res.end());
    return res;
}


