    int ret = 0;
    int i,j;
    for(i=0;i<grid.size();i++){
        for(j=0;j<grid[i].size();j++){
            if(grid[i][j] == 1){
                ret++;
            }
        }
    }
    return ret;
}

int main(){

    int n,m,capacity;
    scanf("%d%d%d",&n,&m,&capacity);
    vector<vector<int>> grid(n,vector<int>(m,0));
    int i,j;
    for(i=0;i<n;i++){
        for(j=0;j<m;j++){
            scanf("%d",&grid[i][j]);
        }
    }
    printf("%d",max_fill(grid,capacity));
}
