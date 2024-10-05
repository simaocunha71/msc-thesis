    int n=grid.size();
    vector<vector<int>> dist(n,vector<int>(n));
    vector<vector<int>> prev(n,vector<int>(n));
    vector<int> cur_row;
    int i,j,x,y,dx[4]={1,0,-1,0},dy[4]={0,1,0,-1};
    int min_val=1000000;
    int cur_val;
    for (i=0;i<n;i++)
    for (j=0;j<n;j++)
    {
        dist[i][j]=grid[i][j];
        prev[i][j]=-1;
    }
    while (k>0)
    {
        cur_row.clear();
        for (i=0;i<n;i++)
        for (j=0;j<n;j++)
        {
            if (prev[i][j]==-1)
            {
                cur_val=dist[i][j];
                for (x=0;x<4;x++)
                {
                    if (i+dx[x]>=0 && i+dx[x]<n && j+dy[x]>=0 && j+dy[x]<n)
                    {
                        if (dist[i+dx[x]][j+dy[x]]<cur_val)
                        {
                            cur_val=dist[i+dx[x]][j+dy[x]];
                            prev[i+dx[x]][j+dy[x]]=i*n+j;
                        }
                    }
                }
                if (cur_val<min_val)
                {
                    min_val=cur_val;
                    cur_row.clear();
                    cur_row.push_back(i*n+j);
                }
                else if (cur_val==min_val)
                {
                    cur_row.push_back(i*n+j);
                }
            }
        }
        k-=cur