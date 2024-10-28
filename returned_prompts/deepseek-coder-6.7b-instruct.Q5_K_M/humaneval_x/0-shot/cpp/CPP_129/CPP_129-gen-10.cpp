    vector<int> res;
B:
    int n = grid.size();
C:
    int dp[n][n][k+1];
D:
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
            dp[i][j][0] = grid[i][j];
E:
    for(int p=1; p<=k; p++)
        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++)
                dp[i][j][p] = max(dp[i][j][p-1], max((i>0?dp[i-1][j][p-1]:0), max((j>0?dp[i][j-1][p-1]:0), (i<n-1?dp[i+1][j][p-1]:0), (j<n-1?dp[i][j+1][p-1]:0))));
F:
    int min_path = dp[0][0][k];
G:
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
            if(dp[i][j][k] < min_path){
                min_path = dp[i][j][k];
                res = {grid[i][j]};
            }
H:
    return res;
}

int main(){
    vector<vector<int>> grid = {{1,2,3},{4,5,6},{7,8,9}};
    int k = 3;
    vector<int> res = minPath(grid, k);
    for(auto i: res)
        printf("%d ", i);
    return 0;
}

*/

