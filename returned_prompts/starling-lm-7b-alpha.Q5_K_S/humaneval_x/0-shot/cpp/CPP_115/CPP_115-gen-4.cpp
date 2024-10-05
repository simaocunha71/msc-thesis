    int n = grid.size(),m = grid[0].size();
    int res = 0;
    for(int i = 0;i < n;i++){
        for(int j = 0;j < m;j++){
            if(grid[i][j]){
                grid[i][j] -= capacity;
                res++;
            }
        }
    }
    while(true){
        bool flag = true;
        for(int i = 0;i < n;i++){
            for(int j = 0;j < m;j++){
                if(grid[i][j] > 0){
                    grid[i][j] -= capacity;
                    res++;
                    flag = false;
                }
            }
        }
        if(flag)return res;
    }
}

int main(){
    int n,m,capacity;
    scanf("%d%d%d",&n,&m,&capacity);
    vector<vector<int>> grid(n,vector<int>(m,0));
    for(int i = 0;i < n;i++)
        for(int j = 0;j < m;j++)
            scanf("%d",&grid[i][j]);
    int res = max_fill(grid,capacity);
    printf("%d\n",res);
    return 0;
}

*/


















































































































































































