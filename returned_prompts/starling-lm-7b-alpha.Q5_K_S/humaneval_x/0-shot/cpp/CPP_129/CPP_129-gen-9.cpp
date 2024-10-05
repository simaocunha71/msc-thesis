    int n = grid.size();
    if(n == 0) return vector<int>();
    int m = grid[0].size();
    if(m == 0) return vector<int>();
    if(k == 0) return vector<int>();
    if(n == 1) {
        vector<int> res;
        for(int i = 0; i < m && k > 0; ++i, --k) {
            res.push_back(grid[0][i]);
        }
        return res;
    }
    if(m == 1) {
        vector<int> res;
        for(int i = 0; i < n && k > 0; ++i, --k) {
            res.push_back(grid[i][0]);
        }
        return res;
    }
    if(k == 1) return grid[0];

    vector<vector<int>> dp(n, vector<int>(m));
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < m; ++j) {
            dp[i][j] = grid[i][j];
        }
    }
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < m; ++j) {
            if(i > 0) dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j]);
            if(j > 0) dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j]);
        }
    }
    int min_val = INT_MAX;
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < m; ++j) {
            min_val = min(min_val, dp[i][j]);
        }
    }
    int min_count = 0;
    for(int i = 0; i < n; ++i) {
        for(