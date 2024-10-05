    int m=grid.size();
    int n=grid[0].size();
    int sum=0;
    vector<vector<int>> visited(m+2,vector<int>(n+2));
    for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
            sum+=grid[i][j];
    int times=sum/capacity;
    if(sum%capacity==0)
        return times;
    visited[0][0]=1;
    visited[0][n+1]=1;
    visited[m+1][0]=1;
    visited[m+1][n+1]=1;
    for(int i=0;i<m;i++)
        visited[i][0]=1;
    for(int j=0;j<n;j++)
        visited[m+1][j]=1;
    for(int i=0;i<m;i++)
        visited[i][n+1]=1;
    for(int j=0;j<n;j++)
        visited[0][j]=1;
    while(true){
        int i=-1,j=-1;
        for(int k=0;k<m;k++)
            for(int l=0;l<n;l++)
                if(grid[k][l]>0){
                    if(i==-1)
                        i=k,j=l;
                    else if(i!=k||j!=l)
                        return -1;
                }
        if(i==-1)
            return times;
        grid[i][j]-=capacity;
        if(visited[i-1][j])
            grid[i-1][j]+=capacity;
        if(visited[i+1][j])
            grid[i+1][j]+=capacity;
        if(visited[i][j-1])
            grid[i][j-1]+=capacity;
        if(visited[i][j+1])
            grid[i][j+1]+=capacity;
        times++;
    }
    return times