    int n = grid.size();
    vector<vector<int>> dp(n,vector<int>(n,0));
    dp[0][0] = grid[0][0];

B:
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(i>0 && j>0) dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
            else if(i>0) dp[i][j] = dp[i-1][j] + grid[i][j];
            else if(j>0) dp[i][j] = dp[i][j-1] + grid[i][j];
        }
    }

C:
    vector<int> result;
    int i = n-1, j = n-1;
    result.push_back(grid[i][j]);
    k--;
    while(k--){
        if(i>0 && j>0 && dp[i-1][j] < dp[i][j-1]) {i--; result.push_back(grid[i][j]);}
        else if(i>0) {i--; result.push_back(grid[i][j]);}
        else if(j>0) {j--; result.push_back(grid[i][j]);}
    }
    reverse(result.begin(), result.end());
    return result;
}

int main(){
    vector<vector<int>> grid = {{5,9,3}, {4,1,6}, {7,8,2}};
    int k = 1;
    vector<int> result = minPath(grid, k);
    for(int i=0; i<result.size(); i++) printf("%d ", result[i]);
    return 0;
}
```

The above program uses dynamic programming to find the minimum path in the grid. 

The function minPath takes a 2D vector grid and an integer k as input and returns an ordered vector