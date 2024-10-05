    int m = grid.size();
    int n = grid[0].size();
    vector<vector<int>> dp(m,vector<int>(n,0));
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(grid[i][j] == 0)
                dp[i][j] = 0;
            else{
                dp[i][j] = 1;
                if(j-1>=0 && dp[i][j-1] == 0)
                    goto A;
                if(i-1>=0 && dp[i-1][j] == 0)
                    goto A;
                if(i-1>=0 && j-1>=0 && dp[i-1][j-1] == 0)
                    goto A;
            }
        }
    }
    return dp[m-1][n-1];
}
int min_fill(vector<vector<int>> grid,int capacity){

B:
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<int>> dp(m,vector<int>(n,0));
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(grid[i][j] == 0)
                dp[i][j] = 0;
            else{
                dp[i][j] = 1;
                if(j+1<n && dp[i][j+1] == 0)
                    goto B;
                if(i+1<m && dp[i+1][j] == 0)
                    goto B;
                if(i+1<m && j+1<n && dp[i+1][j+1] == 0)
                    goto B;
            }
        }
    }
    return dp[0][0];
}
int main(){
    vector<vector<int>> grid;
    vector<int>