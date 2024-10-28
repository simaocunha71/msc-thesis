    int n = grid.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    vector<vector<int>> visit(n, vector<int>(n, 0));
    vector<int> res;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if(k == 0) {
                dp[i][j] = grid[i][j];
            }
            else {
                for(int x = max(0, i-1); x <= min(n-1, i+1); x++) {
                    for(int y = max(0, j-1); y <= min(n-1, j+1); y++) {
                        if(x != i || y != j) {
                            dp[i][j] = min(dp[i][j], dp[x][y] + grid[i][j]);
                        }
                    }
                }
            }
        }
    }
    int min_val = dp[0][0];
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if(dp[i][j] < min_val) {
                min_val = dp[i][j];
                res = vector<int>();
                path(res, grid, i, j, k-1, min_val);
            }
        }
    }
    return res;
}

void path(vector<int>& res, vector<vector<int>>& grid, int i, int j, int k, int val) {
    res.push_back(val);
    if(k == 0) return;
    for(int x = max(0, i-1); x <= min(grid.size()-1, i+1); x++) {
        for(int y = max(0, j-1); y <= min(grid.size()-1, j+1); y++) {
            if(x != i || y != j) {
                if(grid[x][y] == val - res.back()) {
                    path(res, grid, x, y, k-1, grid[x][y]);
                    return;
                }
            }
        }
    }
}