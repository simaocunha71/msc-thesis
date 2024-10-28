    int row = grid.size();
    int col = grid[0].size();
    vector<vector<int>> dp(row,vector<int>(col,0));
    int max_fill = 0;

    for(int i=0;i<row;i++){
        for(int j=0;j<col;j++){
            if(grid[i][j] == 0) continue;
            if(i==0 && j==0) dp[i][j] = grid[i][j];
            else if(i==0) dp[i][j] = max(dp[i][j-1],grid[i][j]);
            else if(j==0) dp[i][j] = max(dp[i-1][j],grid[i][j]);
            else dp[i][j] = max(max(dp[i-1][j],dp[i][j-1]),grid[i][j]);

            if(dp[i][j] > max_fill) max_fill = dp[i][j];
        }
    }
    return max_fill;
}

int main(){
    vector<vector<int>> grid;
    grid.push_back({0,0,1,0});
    grid.push_back({0,1,0,0});
    grid.push_back({1,1,1,1});
    int capacity = 1;
    int max_fill = max_fill(grid,capacity);
    printf("%d",max_fill);
    return 0;
}

