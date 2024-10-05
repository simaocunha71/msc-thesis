    int res = 0,n = grid.size(),m = grid[0].size();
    vector<vector<int>> vis(n,vector<int>(m));
    for(int i = 0;i < n;i++)
        for(int j = 0;j < m;j++)
            if(!vis[i][j] && grid[i][j]){
                int cnt = grid[i][j];
                queue<pair<int,int>> q;
                q.push(make_pair(i,j));
                vis[i][j] = 1;
                while(!q.empty()){
                    int x = q.front().first,y = q.front().second;
                    q.pop();
                    for(int a = -1;a <= 1;a++)
                        for(int b = -1;b <= 1;b++)
                            if(a && b && grid[x + a][y + b]){
                                grid[x + a][y + b]--;
                                q.push(make_pair(x + a,y + b));
                                vis[x + a][y + b] = 1;
                            }
                }
                res += (cnt + capacity - 1) / capacity;
            }
    return res;
}

int main()
{
    int n,m,capacity;
    vector<vector<int>> grid;
    scanf("%d %d %d",&n,&m,&capacity);
    grid.resize(n);
    for(int i = 0;i < n;i++)
        grid[i].resize(m);
    for(int i = 0;i < n;i++)
        for(int j = 0;j < m;j++)
            scanf("%d",&grid[i][j]);
    printf("%d\n",max_fill(grid,capacity));
    return 0;
}


*/






























#include <stdio.h