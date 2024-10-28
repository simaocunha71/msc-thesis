    int n = grid.size();
    vector<vector<int>> dp(n*n+1, vector<int>(k+1, INT_MAX));
    dp[1][0] = 0;
    for(int len=1; len<=k; len++){
        for(int i=1; i<=n*n; i++){
            for(int j=1; j*j<=i && j<=len; j++){
                if(i%j==0){
                    int row = i/j;
                    if(row<=n){
                        dp[i][len] = min(dp[i][len], dp[j][len-1] + (row-1)*1000 + grid[row-1][j-1]);
                    }else{
                        dp[i][len] = min(dp[i][len], dp[j][len-1] + (n-1)*1000 + grid[n-1][i/j-1]);
                    }
                }
            }
        }
    }
B:
    vector<int> res;
    int val = n*n;
    int len = k;
    while(len>0){
        for(int i=1; i<=n*n; i++){
            if(dp[i][len]<dp[val][len-1]){
                val = i;
                break;
            }
        }
        int row = val/n;
        int col = val%n;
        res.push_back(grid[row][col]);
        len--;
    }
C:
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    vector<vector<int>> grid = {{5,9,3},{4,1,6},{7,8,2}};
    int k = 1;
    vector<int> res = minPath(grid, k);
    for(int i=0; i<res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}
```

The solution to this