    int n = grid.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == 0 && j == 0) {
                dp[i][j] = grid[i][j];
            } else if (i == 0) {
                dp[i][j] = min(dp[i][j-1], dp[i][j-1]+grid[i][j]);
            } else if (j == 0) {
                dp[i][j] = min(dp[i-1][j], dp[i-1][j]+grid[i][j]);
            } else {
                dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]+grid[i][j]);
            }
        }
    }
    int i = n-1, j = n-1;
    vector<int> res;
    while (k > 0) {
        res.push_back(grid[i][j]);
        if (i > 0 && j > 0 && dp[i-1][j-1] <= min(dp[i-1][j], dp[i][j-1])) {
            i--; j--;
        } else if (i > 0) {
            i--;
        } else {
            j--;
        }
        k--;
    }
    reverse(res.begin(), res.end());
    return res;
}  // O(n^2) time complexity


