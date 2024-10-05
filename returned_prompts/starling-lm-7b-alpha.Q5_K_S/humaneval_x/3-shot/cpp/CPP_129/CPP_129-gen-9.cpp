    int i,j,n=grid.size(),m=grid[0].size();
    vector<vector<pair<int,int>>> directions;
    directions.resize(n);
    for (i=0;i<n;i++)
    directions[i].resize(m);
    for (i=0;i<n;i++)
    for (j=0;j<m;j++)
    directions[i][j].first=i;
    directions[i][j].second=j;
    vector<vector<int>> distances;
    distances.resize(n);
    for (i=0;i<n;i++)
    distances[i].resize(m);
    for (i=0;i<n;i++)
    for (j=0;j<m;j++)
    distances[i][j]=1000000;
    distances[0][0]=0;
    vector<vector<int>> queue;
    queue.resize(n);
    for (i=0;i<n;i++)
    queue[i].resize(m);
    queue[0][0]=grid[0][0];
    vector<pair<int,int>> q;
    q.push_back(make_pair(0,0));
    while (q.size())
    {
        int curr_i=q[0].first;
        int curr_j=q[0].second;
        q.erase(q.begin());
        for (i=0;i<4;i++)
        {
            int new_i=curr_i+directions[curr_i][curr_j].first;
            int new_j=curr_j+directions[curr_i][curr_j].second;
            if (new_i<n && new_j<m && new_i>=0 && new_j>=0 && distances[new_i][new_j]>distances[curr_i][curr_j]+1 && grid[new_i][new_j]<k)
            {
                distances[new_i][new_j]=distances[curr_i][curr_j]+1;
                queue[new_i][