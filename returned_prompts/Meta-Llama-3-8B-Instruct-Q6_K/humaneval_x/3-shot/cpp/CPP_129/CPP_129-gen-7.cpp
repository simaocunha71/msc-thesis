    int n = grid.size();
    vector<int> res;
    vector<vector<bool>> visited(n, vector<bool>(n, false));
    vector<vector<int>> dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    queue<pair<int, int>> q;
    q.push({0, 0});
    visited[0][0] = true;
    res.push_back(grid[0][0]);
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        res.push_back(grid[x][y]);
        if (k > 1) {
            for (auto dir : dirs) {
                int nx = x + dir[0];
                int ny = y + dir[1];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny]) {
                    q.push({nx, ny});
                    visited[nx][ny] = true;
                }
            }
        }
        k--;
        if (k == 0) {
            break;
        }
    }
    return res;
}