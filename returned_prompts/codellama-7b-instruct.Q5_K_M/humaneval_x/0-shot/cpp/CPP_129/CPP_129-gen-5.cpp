    int N = grid.size();
    int M = grid[0].size();
    vector<vector<int>> dp(N, vector<int>(M, 0));
    vector<int> path(N, 0);
    for(int i = 0; i < N; i++)
        for(int j = 0; j < M; j++)
            dp[i][j] = grid[i][j];
    for(int i = 1; i < N; i++){
        for(int j = 1; j < M; j++){
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1);
            if(i > 1 && j > 1)
                dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1);
            dp[i][j] = min(dp[i][j], dp[i][j]);
        }
    }
    for(int i = N-1; i >= 0 && k > 0; i--){
        for(int j = M-1; j >= 0 && k > 0; j--){
            if(dp[i][j] == k){
                path[i] = grid[i][j];
                k--;
            }
        }
    }
    return path;
}
int main()
{
    vector<vector<int>> grid = { {1,2,3}, {4,5,6}, {7,8,9} };
    int k = 3;
    vector<int> ans = minPath(grid, k);
    for(int i = 0; i < ans.size(); i++)
        printf("%d ", ans[i]);
    printf("\n");
    return 0;
}

