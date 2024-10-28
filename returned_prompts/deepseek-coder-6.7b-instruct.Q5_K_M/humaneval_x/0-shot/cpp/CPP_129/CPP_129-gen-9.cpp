    int n = grid.size();
    int m = grid[0].size();
    vector<vector<int>> dp(n, vector<int>(m, 1e9));
    vector<vector<int>> dir = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    vector<vector<int>> pos(n * m + 1);
    vector<int> cell(n * m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
        {
            pos[grid[i][j]] = {i, j};
            cell[i * m + j] = grid[i][j];
        }
    int start = cell[0];
    dp[pos[start][0]][pos[start][1]] = start;
    for (int steps = 1; steps < k; steps++)
    {
        vector<vector<int>> tmp = dp;
        for (int c = 1; c <= n * m; c++)
        {
            int x = pos[c][0], y = pos[c][1];
            for (int d = 0; d < 4; d++)
            {
                int nx = x + dir[d][0], ny = y + dir[d][1];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m)
                    tmp[nx][ny] = min(tmp[nx][ny], dp[x][y] + c);
            }
        }
        dp = tmp;
    }
    int minPath = *min_element(dp[pos[k][0]][pos[k][1]].begin(), dp[pos[k][0]][pos[k][1]].end());
    return {cell.begin(), cell.begin() + minPath};
}

int main() {
    vector<vector<int>> grid = {{5,9,3}, {4,1,6}, {7,8,2}};
    int k = 1;
    vector<int> res