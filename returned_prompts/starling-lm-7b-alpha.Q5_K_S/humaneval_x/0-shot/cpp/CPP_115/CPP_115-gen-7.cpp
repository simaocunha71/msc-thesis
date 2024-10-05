    int n=grid.size(),m=grid[0].size();
    vector<vector<int>> dist(n,vector<int>(m,0));
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(grid[i][j]==1)dist[i][j]=1;
        }
    }
    vector<vector<int>> dir={{0,1},{1,0},{0,-1},{-1,0}};
    vector<vector<bool>> visited(n,vector<bool>(m,false));
    int cnt=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(!visited[i][j]&&grid[i][j]==1){
                vector<vector<int>> tmp;
                int tmp_dist=0;
                queue<pair<int,int>> q;
                q.push({i,j});
                while(!q.empty()){
                    int x=q.front().first,y=q.front().second;
                    q.pop();
                    if(visited[x][y])continue;
                    visited[x][y]=true;
                    tmp_dist++;
                    tmp.push_back({x,y});
                    for(int k=0;k<4;k++){
                        int dx=x+dir[k][0],dy=y+dir[k][1];
                        if(dx>=0&&dx<n&&dy>=0&&dy<m&&!visited[dx][dy]&&grid[dx][dy]==1){
                            q.push({dx,dy});
                        }
                    }
                }
                cnt++;
                for(int i=0;i<tmp.size();i++){
                    int x=tmp[i][0],y=tmp[i][1];
                    for(int j=0;j<tmp_dist;j++){
                        grid[x][y]=0;
                        x+=dir[i][0];
