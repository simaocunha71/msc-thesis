    int n = grid.size();
    int m = grid[0].size();
    vector<vector<int>> dp(n,vector<int>(m,INT_MAX));
    vector<vector<int>> dp2(n,vector<int>(m,INT_MAX));
    vector<vector<int>> next(n,vector<int>(m));
    vector<int> dx = {-1,0,1,0};
    vector<int> dy = {0,1,0,-1};
    priority_queue<pair<int,pair<int,int>>,vector<pair<int,pair<int,int>>>,greater<pair<int,pair<int,int>>>> pq;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(i+j==k-1){
                dp[i][j]=grid[i][j];
                pq.push({dp[i][j],{i,j}});
            }
        }
    }
    while(!pq.empty()){
        pair<int,int> p = pq.top().second;
        int x = p.first, y = p.second, dist = pq.top().first;
        pq.pop();
        if(dp2[x][y]>dist){
            dp2[x][y]=dist;
            for(int i=0;i<4;i++){
                int nx = x+dx[i], ny = y+dy[i];
                if(nx>=0 && ny>=0 && nx<n && ny<m){
                    if(dp2[nx][ny]>dp2[x][y]+grid[nx][ny]){
                        dp[nx][ny]=grid[nx][ny];
                        pq.push({dp[nx][ny],{nx,ny}});
                    }
                }
            }
        }
    }
    vector<int> ans;
    for(int i=0;i<n;i++){
