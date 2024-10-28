    vector<int> res(k);
    int n = grid.size();
    int m = grid[0].size();
    vector<vector<int>> dist(n, vector<int>(m));
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            dist[i][j] = grid[i][j];
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            if(dist[i][j] != 0)
                for(int d=0;d<4;d++)
                    if(i+dx[d]>=0&&i+dx[d]<n&&j+dy[d]>=0&&j+dy[d]<m)
                        dist[i+dx[d]][j+dy[d]] = min(dist[i+dx[d]][j+dy[d]], dist[i][j]+1);
    int minDist = 2e9;
    vector<int> minDistPos;
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            if(dist[i][j]<minDist){
                minDist = dist[i][j];
                minDistPos.clear();
                minDistPos.push_back(i);
                minDistPos.push_back(j);
            } else if(dist[i][j]==minDist){
                minDistPos.push_back(i);
                minDistPos.push_back(j);
            }
    if(minDistPos.size()>k)
        return res;
    if(minDistPos.size()==1)
        res[0] = grid[minDistPos[0]][minDistPos[1]];
    else{
        int i = minDistPos[0];
        int j = minDistPos[1];
        int d = 0;
        if(i+dx[d]!=minDistPos[0]||j+dy[d]!=minDistPos[1])
           