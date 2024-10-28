    int N = grid.size();
    int directions[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    vector<vector<int>> dp(N, vector<int>(N, INT_MAX));
    vector<vector<int>> path(N, vector<int>(N, -1));
    vector<int> res;

    function<int(int, int, int)> dfs = [&](int x, int y, int steps) {
        if (steps == k) {
            return grid[x][y];
        }
        if (dp[x][y] != INT_MAX) {
            return dp[x][y];
        }
        for (auto &d : directions) {
            int nx = x + d[0], ny = y + d[1];
            if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                int val = dfs(nx, ny, steps + 1);
                if (grid[x][y] < val) {
                    dp[x][y] = val;
                    path[x][y] = nx * N + ny;
                }
            }
        }
        return dp[x][y];
    };

    int minVal = INT_MAX;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            int val = dfs(i, j, 1);
            if (val < minVal) {
                minVal = val;
                res = {i * N + j};
            }
        }
    }

    while (path[res[0] / N][res[0] % N] != -1) {
        res.insert(res.begin(), path[res[0] / N][res[0] % N]);
        int next = path[res[0] / N][res[0] % N];
        res[0] = next;
    }

    return res;
}

