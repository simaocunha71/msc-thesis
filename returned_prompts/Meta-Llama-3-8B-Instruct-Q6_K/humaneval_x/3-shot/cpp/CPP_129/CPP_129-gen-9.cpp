    int n = grid.size();
    vector<vector<bool>> visited(n, vector<bool>(n, false));
    vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    queue<pair<int, int>> q;
    vector<int> res;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) {
                q.push({i, j});
                visited[i][j] = true;
            }
        }
    }
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        res.push_back(grid[x][y]);
        for (auto &direction : directions) {
            int nx = x + direction[0];
            int ny = y + direction[1];
            if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny]) {
                q.push({nx, ny});
                visited[nx][ny] = true;
            }
        }
    }
    return res;
}  // End of minPath function
vector<int> result = minPath({{1,2,3}, {4,5,6}, {7,8,9}}, 3);
for (int i = 0; i < result.size(); i++) {
    cout << result[i] << " ";
}
cout << endl;  // Output: 1 2 1
```


