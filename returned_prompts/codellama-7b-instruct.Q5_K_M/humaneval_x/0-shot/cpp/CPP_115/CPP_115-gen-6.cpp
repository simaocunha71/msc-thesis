    if(grid[0][0]==0)
        return 0;
    int i,j,n=grid.size();
    int m=grid[0].size();
    vector<vector<int>> visited(n,vector<int>(m,0));
    vector<vector<int>> parent(n,vector<int>(m,-1));
    queue<pair<int,int>> q;
    q.push({0,0});
    visited[0][0]=1;
    parent[0][0]=0;
    while(!q.empty()){
        pair<int,int> top = q.front();
        q.pop();
        i = top.first;
        j = top.second;
        if(i==n-1&&j==m-1)
            break;
        if(i+1<n&&grid[i+1][j]!=0&&!visited[i+1][j]){
            visited[i+1][j]=1;
            parent[i+1][j]=i;
            q.push({i+1,j});
        }
        if(i>0&&grid[i-1][j]!=0&&!visited[i-1][j]){
            visited[i-1][j]=1;
            parent[i-1][j]=i;
            q.push({i-1,j});
        }
        if(j+1<m&&grid[i][j+1]!=0&&!visited[i][j+1]){
            visited[i][j+1]=1;
            parent[i][j+1]=i;
            q.push({i,j+1});
        }
        if(j>0&&grid[i][j-1]!=0&&!visited[i][j-1]){
            visited[i][j-1]=1;
            parent[i][j-1]=i;
            q.push({i,j-1});
        }
    }
    int count=0;
    while(parent[i][j]!=-1){
        i=parent[i][j];
        j=parent[i][j