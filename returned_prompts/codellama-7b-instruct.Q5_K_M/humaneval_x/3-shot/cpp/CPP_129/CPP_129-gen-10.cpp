    int N = grid.size();
    int m = N*N;
    int i,j,x,y;
    vector<int> ans;
    vector<vector<int>> dist(N,vector<int>(N,m));
    for (i=0;i<N;i++)
        for (j=0;j<N;j++)
        dist[i][j]=m;
    vector<vector<bool>> visited(N,vector<bool>(N,false));
    for (i=0;i<N;i++)
        for (j=0;j<N;j++)
        dist[i][j]=abs(i-j);
    vector<vector<int>> prev(N,vector<int>(N,-1));
    for (i=0;i<N;i++)
        for (j=0;j<N;j++)
        prev[i][j]=i*N+j;
    x=0;
    y=0;
    vector<int> current;
    int d,dx,dy;
    for (i=0;i<k;i++){
        current.clear();
        for (d=1;d<=N*N;d++){
            dx=x+d/N-1;
            dy=y+d%N;
            if (dx>=0 && dx<N && dy>=0 && dy<N && dist[dx][dy]==d && !visited[dx][dy]){
                current.push_back(grid[dx][dy]);
                visited[dx][dy]=true;
                dist[dx][dy]=m;
                prev[dx][dy]=-1;
            }
        }
        if (current.size()==0)
        return ans;
        ans=current;
        x=dx;
        y=dy;
    }
    return ans;
}


