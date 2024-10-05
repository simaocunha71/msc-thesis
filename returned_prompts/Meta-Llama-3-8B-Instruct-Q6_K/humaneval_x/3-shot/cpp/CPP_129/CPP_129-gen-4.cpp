    int N = grid.size();
    int result[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            result[i][j] = grid[i][j];
        }
    }
    vector<int> res;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i > 0) result[i][j] = min(result[i][j], result[i - 1][j]);
            if (j > 0) result[i][j] = min(result[i][j], result[i][j - 1]);
        }
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i < N - 1) result[i][j] = min(result[i][j], result[i + 1][j]);
            if (j < N - 1) result[i][j] = min(result[i][j], result[i][j + 1]);
        }
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i > 0 && j > 0) result[i][j] = min(result[i][j], result[i - 1][j - 1]);
        }
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i < N - 1 && j < N - 1) result[i][j] = min(result[i][j], result[i + 1][j + 1]);
        }
    }
    int x = 0, y = 0;
    for (int i = 0; i < k; i++) {
        res.push_back(result[x][y]);
        if (x > 0 && y > 0) {
            if (result[x][y] == result[x - 1][y - 1]) {
                x--;
                y--;
            }
            else if (result[x][y] == result[x - 1][y]) {
                x--;
            }
            else if (