    int n=grid.size();
    int m=grid[0].size();
    vector<int> dp(n*m+1, 0);
    vector<int> prev(n*m+1, 0);
    vector<int> ans;
    int i,j,x,y,s,t,val;
    for (i=1;i<=n*m;i++){
        dp[i]=i;
        prev[i]=i;
    }
    for (x=0;x<n;x++){
        for (y=0;y<m;y++){
            for (i=1;i<n*m+1;i++){
                s=x*n+y;
                t=x*n+((y+1)%m);
                if (dp[i]>dp[i-1]+grid[x][y]){
                    dp[i]=dp[i-1]+grid[x][y];
                    prev[i]=s;
                }
                if (dp[i]>dp[i-n]+grid[x][(y+1)%m]){
                    dp[i]=dp[i-n]+grid[x][(y+1)%m];
                    prev[i]=t;
                }
            }
        }
    }
    for (i=n*m;i>0;i--){
        if (dp[i]==k){
            ans.push_back(grid[prev[i]/n][prev[i]%m]);
            val=i;
            break;
        }
    }
    for (i=val;i>0;i--){
        ans.push_back(grid[prev[i]/n][prev[i]%m]);
    }
    return ans;
}


