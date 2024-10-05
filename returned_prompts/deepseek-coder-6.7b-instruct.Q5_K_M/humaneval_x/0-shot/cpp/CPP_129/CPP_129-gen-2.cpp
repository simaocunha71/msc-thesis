    int n = grid.size();
    vector<vector<int>> dp(n*n+1, vector<int>(k+1));
    vector<vector<int>> path(n*n+1, vector<int>(k+1));
    for(int i = 0; i <= k; i++){
        dp[0][i] = INT_MAX;
    }
    for(int i = 1; i <= n*n; i++){
        dp[i][0] = INT_MAX;
    }
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            for(int l = 1; l <= k; l++){
                if(l < i*j){
                    dp[i*j][l] = dp[i*j-1][l];
                    path[i*j][l] = path[i*j-1][l];
                }
                else{
                    int temp = dp[i*j-1][l-i*j] + grid[i-1][j-1];
                    if(temp < dp[i*j][l]){
                        dp[i*j][l] = temp;
                        path[i*j][l] = i*j;
                    }
                }
            }
        }
    }
    vector<int> result(k);
    int i = n*n, j = k;
    while(i > 0){
        result[--j] = path[i][k];
        i -= path[i][k];
        k -= path[i][k];
    }
    return result;
}

int main()
{
    vector<vector<int>> grid1 = {{1,2,3}, {4,5,6}, {7,8,9}};
    vector<int> res = minPath(grid1, 3);
    for(int i=0; i<res.size(); i++)
        printf("%d ", res[i]);
    printf("\n");

    vector<vector<int>> grid2 = {{5,9,