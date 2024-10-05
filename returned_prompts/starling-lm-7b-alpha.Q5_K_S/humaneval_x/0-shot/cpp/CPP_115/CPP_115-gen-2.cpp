    int n=grid.size(),m=grid[0].size();
    int ans=0;
    while(true){
        vector<vector<int>> grid_cpy=grid;
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                if(grid_cpy[i][j]){
                    grid_cpy[i][j]--;
                    if(i+capacity<n)
                        grid_cpy[i+capacity][j]--;
                    if(j+capacity<m)
                        grid_cpy[i][j+capacity]--;
                }
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                if(grid_cpy[i][j])
                    return ans;
        ans++;
    }
}
int main(){
    int n,m,capacity;
    scanf("%d %d %d",&n,&m,&capacity);
    vector<vector<int>> grid(n,vector<int>(m,0));
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            scanf("%d",&grid[i][j]);
    printf("%d",max_fill(grid,capacity));
    return 0;
}

*/




















































































































































































