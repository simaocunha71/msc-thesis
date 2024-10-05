    for(int i = 0; i < grid.size(); i++){
        for(int j = 0; j < grid[0].size(); j++){
            if(grid[i][j] == 1){
                if(i == 0){
                    if(grid[i][j-1] == 1 || grid[i][j+1] == 1)
                        return 2;
                    else
                        return 1;
                }
                else if(i == grid.size() - 1){
                    if(grid[i-1][j] == 1 || grid[i][j-1] == 1)
                        return 2;
                    else
                        return 1;
                }
                else{
                    if(grid[i-1][j] == 1 || grid[i-1][j-1] == 1 || grid[i-1][j+1] == 1 || grid[i][j-1] == 1 || grid[i][j+1] == 1 || grid[i+1][j] == 1 || grid[i+1][j-1] == 1 || grid[i+1][j+1] == 1)
                        return 2;
                    else
                        return 1;
                }
            }
        }
    }
}

int main(){
    int grid_size;
    int capacity;
    scanf("%d",&grid_size);
    vector<vector<int>> grid(grid_size, vector<int>(grid_size));
    for(int i = 0; i < grid_size; i++){
        for(int j = 0; j < grid_size; j++){
            scanf("%d",&grid[i][j]);
        }
    }
    scanf("%d",&capacity);
    printf("%d",max_fill(grid,capacity));
    return 0;
}

/*
Note:
    * 0 means empty
    * 1 means filled
    * we need to find the maximum number of times we need to lower the bucket
*/
