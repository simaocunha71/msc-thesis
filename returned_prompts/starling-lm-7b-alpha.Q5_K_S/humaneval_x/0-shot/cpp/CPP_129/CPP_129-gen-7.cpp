    int n = grid.size();
    vector<vector<int>> dist(n,vector<int>(n,99999999));
    vector<vector<int>> prev(n,vector<int>(n,-1));

    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            dist[i][j]=grid[i][j];

    for(int i=0;i<n;i++)
        dist[i][0]=grid[i][0];
    for(int j=1;j<n;j++)
        dist[0][j]=grid[0][j];

    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            for(int x=0;x<n;x++)
                for(int y=0;y<n;y++)
                    if(dist[x][y]+1<dist[i][j]){
                        dist[i][j]=dist[x][y]+1;
                        prev[i][j]=x;
                    }

    int curx=0,cury=0;
    vector<int> res;
    for(int i=0;i<k;i++)
        res.push_back(grid[curx][cury]);
    while(curx!=n-1||cury!=n-1){
        int tx=prev[curx][cury];
        int ty=prev[curx][cury]+1;
        if(dist[tx][cury]+1<dist[curx][cury]){
            curx=tx;
            cury=cury;
        }else{
            curx=curx;
            cury=ty;
        }
        res.push_back(grid[curx][cury]);
    }
    return res;
}

int main(){
    vector<vector<int>> grid={{1,2,3}, {4,5,6}, {7,8,9}};
    int k=3;
    printf("{");
    for(int i=0;i<k;i