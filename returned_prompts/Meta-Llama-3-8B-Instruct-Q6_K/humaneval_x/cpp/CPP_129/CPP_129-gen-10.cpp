    int N = grid.size();
    int res[N][N];
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            res[i][j] = grid[i][j];
        }
    }
    vector<int> result;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(res[i][j] == 1){
                dfs(res, i, j, k, result);
                if(result.size() == k){
                    return result;
                }
            }
        }
    }
    return result;

B:
    // DFS with backtracking
    int N = grid.size();
    vector<vector<int>> res(N, vector<int>(N));
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            res[i][j] = grid[i][j];
        }
    }
    vector<int> result;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(res[i][j] == 1){
                dfs(res, i, j, k, result);
                if(result.size() == k){
                    return result;
                }
            }
        }
    }
    return result;

C:
    int N = grid.size();
    vector<vector<int>> res(N, vector<int>(N));
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            res[i][j] = grid[i][j];
        }
    }
    vector<int> result;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(res[i][j] == 1){
                dfs(res, i, j, k, result);
                if(result.size() == k){
                    return result;
                }
            }
        }
    }
    return result;

D:
    vector<vector<int>> grid = {{1,2,3},{4,5,6},{7,8,9}};
    int k = 3;
    vector<int> result = minPath(grid, k);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
