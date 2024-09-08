    int N = grid.size();
    if(N <= 1) return {};

    vector<vector<bool>> visited(N, vector<bool>(N, false));
    vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    vector<vector<int>> dp(N, vector<int>(N, INT_MAX));
    vector<vector<int>> path(N, vector<int>(N, -1));
    vector<int> result;

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(i == 0 && j == 0){
                dp[i][j] = grid[i][j];
            }else{
                for(int d = 0; d < 4; d++){
                    int ni = i + directions[d][0];
                    int nj = j + directions[d][1];
                    if(ni >= 0 && ni < N && nj >= 0 && nj < N && !visited[ni][nj]){
                        int cost = dp[i][j] + grid[ni][nj];
                        if(cost < dp[ni][nj]){
                            dp[ni][nj] = cost;
                            path[ni][nj] = i;
                            visited[ni][nj] = true;
                        }
                    }
                }
            }
        }
    }

    int i = N - 1;
    int j = N - 1;
    for(int l = 0; l < k; l++){
        result.push_back(grid[i][j]);
        i = path[i][j];
        j = N - 1;
        for(int d = 0; d < 4; d++){
            int ni = i + directions[d][0];
            int nj = j + directions[d][1];
            if(ni >= 0 && ni < N && nj >= 0 && nj < N && path[ni][nj] == i){
                j = nj;
                break;
            }
        }
    }
    reverse(result.begin(), result.end());
    return result;
}

int main()
{
    vector<vector<int>> grid = {{1,2,3}, {4,5,6}, {7,8,9}};
    int k = 3;
    vector<int> result = minPath(grid, k);
    for(int i = 0; i < result.size(); i++){
        printf("%d ",