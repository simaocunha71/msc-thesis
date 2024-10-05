    vector<int> path;
    int rows=grid.size();
    int cols=grid[0].size();
    int visited[rows][cols];
    int i,j;
    for (i=0;i<rows;i++)
    for (j=0;j<cols;j++)
    visited[i][j]=0;
    int min=1000000000;
    int minx,miny;
    for (i=0;i<rows;i++)
    for (j=0;j<cols;j++)
    {
        if (grid[i][j]<min){
            min=grid[i][j];
            minx=i;
            miny=j;
        }
    }
    visited[minx][miny]=1;
    path.push_back(grid[minx][miny]);
    k=k-1;
    if (k==0) return path;
    int x,y;
    x=minx;
    y=miny;
    int nextx,nexty;
    int minn=1000000000;
    while (k>0)
    {
        if (x==0 && y==0) 
        {
            if (grid[x+1][y]<minn) 
            {
            minn=grid[x+1][y];
            nextx=x+1;
            nexty=y;
            }
            if (grid[x][y+1]<minn) 
            {
            minn=grid[x][y+1];
            nextx=x;
            nexty=y+1;
            }
        }
        else if (x==0 && y==cols-1)
        {
            if (grid[x+1][y]<minn) 
            {
            minn=grid[x+1][y];
            nextx=x+1;
            nexty=y;
            }
            if (grid[x][y-1]<minn) 
            {
            minn=grid[x][y-1];
            nextx=x;
            nexty=y-1;
            }
        }
        else if (x==rows-1 && y==0)
        {
            if (grid[x-1][y]<minn) 
            {
            minn=grid[x-1][y];
            nextx=x-1;
            nexty=y;
            }
            if (grid[x][y+1]<minn) 
            {
            minn=grid[x][y+1];
            nextx=x;
            nexty=y+1;
            }
