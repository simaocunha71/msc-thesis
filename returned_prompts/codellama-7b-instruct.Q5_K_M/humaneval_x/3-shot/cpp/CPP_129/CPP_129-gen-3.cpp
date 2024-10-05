    int n=grid.size();
    vector<int> res;
    vector<int> dir={0,1,0,-1,0};
    vector<vector<int>> dp(n,vector<int>(n,0));
    vector<vector<int>> path(n,vector<int>(n,0));
    vector<int> visited(n*n,0);
    int i=0,j=0,idx=0;
    while(k>0){
        i=idx%n;
        j=idx/n;
        if (visited[i*n+j]==0){
            visited[i*n+j]=1;
            dp[i][j]=1;
            path[i][j]=1;
            idx++;
            k--;
        }
        else{
            for (int p=0;p<4;p++){
                int new_i=i+dir[p];
                int new_j=j+dir[p+1];
                if (new_i>=0&&new_i<n&&new_j>=0&&new_j<n&&visited[new_i*n+new_j]==0){
                    if (dp[new_i][new_j]>dp[i][j]+1){
                        dp[new_i][new_j]=dp[i][j]+1;
                        path[new_i][new_j]=path[i][j];
                    }
                }
            }
        }
    }
    i=idx%n;
    j=idx/n;
    while(i>=0&&j>=0){
        res.push_back(grid[i][j]);
        i-=dir[path[i][j]];
        j-=dir[path[i][j]+1];
    }
    return res;
}



