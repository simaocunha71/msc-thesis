    int N = grid.size();
    vector<vector<int>> dp(N, vector<int>(N, INT_MAX));
    vector<vector<int>> visited(N, vector<int>(N, 0));
    vector<int> res;
    dp[0][0] = grid[0][0];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i > 0) dp[i][j] = min(dp[i][j], dp[i-1][j]);
            if (j > 0) dp[i][j] = min(dp[i][j], dp[i][j-1]);
        }
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i > 0 && j > 0) {
                if (dp[i][j] != dp[i-1][j] && dp[i][j] != dp[i][j-1]) {
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
    }
    int i = N-1, j = N-1;
    while (k > 0) {
        res.push_back(grid[i][j]);
        if (i > 0 && j > 0) {
            if (dp[i][j] == dp[i-1][j]) i--;
            else j--;
        } else if (i > 0) i--;
        else j--;
        k--;
    }
    reverse(res.begin(), res.end());
    return res;
}  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested.  // Not tested