    int n = grid.size();
    vector<vector<int>> v(n,vector<int>(n,0));
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) v[i][j] = grid[i][j];
    vector<vector<int>> g(n*n+1);
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) for(int d=0;d<4;d++) {
        int i2 = i+dx[d], j2 = j+dy[d];
        if(i2>=0 && i2<n && j2>=0 && j2<n) {
            g[v[i][j]].push_back(v[i2][j2]);
        }
    }
    vector<int> dp(n*n+1);
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) dp[v[i][j]] = v[i][j];
    vector<int> d(n*n+1);
    for(int i=0;i<n*n;i++) d[i] = -1;
    for(int i=1;i<=n*n;i++) if(d[i]==-1) {
        vector<int> q;
        q.push_back(i); d[i] = 0;
        for(int j=0;j<k;j++) {
            vector<int> q2;
            for(int u:q) for(int v:g[u]) if(d[v]==-1) {
                d[v] = d[u]+1;
                q2.push_back(v);
            }
            q = q2;
        }
        int u = i, du = d[u];
        vector<int> p;
        for(int j=0;j<k;j++) {
            p.push_back(u);
            for(int v:g[u]) if(d[v]==du)