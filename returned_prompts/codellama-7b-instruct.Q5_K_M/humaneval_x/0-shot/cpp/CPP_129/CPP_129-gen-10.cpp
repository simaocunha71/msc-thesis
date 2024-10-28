    int rows = grid.size(), cols = grid[0].size();
    int max_val = rows * cols;
    vector<vector<int>> dp(rows, vector<int>(cols, max_val));
    for (int i = 0; i < rows; i++) {
        dp[i][0] = grid[i][0];
    }
    for (int i = 0; i < cols; i++) {
        dp[0][i] = grid[0][i];
    }

    for (int i = 1; i < rows; i++) {
        for (int j = 1; j < cols; j++) {
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
        }
    }

    vector<int> path;
    int cur_row = rows - 1, cur_col = cols - 1, cur_val = dp[cur_row][cur_col];
    while (cur_val != max_val) {
        path.push_back(grid[cur_row][cur_col]);
        if (cur_row > 0 && dp[cur_row - 1][cur_col] == cur_val) {
            cur_row--;
        }
        else if (cur_col > 0 && dp[cur_row][cur_col - 1] == cur_val) {
            cur_col--;
        }
        else {
            break;
        }
        cur_val = dp[cur_row][cur_col];
    }
    if (path.size() < k) {
        goto A;
    }

    return path;
}

int main(){

    return 0;
}
