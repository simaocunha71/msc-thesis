    int n = grid.size();
    int m = grid[0].size();
    int total = 0;
    vector<vector<int>> grid_copy = grid;
    while(true){
        bool flag = false;
        for(int i = 0;i<n;i++){
            for(int j = 0;j<m;j++){
                if(grid[i][j]>0){
                    if(grid[i][j]>=capacity){
                        grid[i][j]-=capacity;
                        total+=capacity;
                        grid_copy[i][j]-=capacity;
                        flag = true;
                    }else{
                        total+=grid[i][j];
                        grid_copy[i][j]-=grid[i][j];
                        grid[i][j] = 0;
                        flag = true;
                    }
                }
            }
        }
        if(!flag)break;
    }
    return total;
}
int main(){
    vector<vector<int>> grid = {{0,0,1,0}, {0,1,0,0}, {1,1,1,1}};
    int capacity = 1;
    printf("%d\n",max_fill(grid,capacity));
    return 0;
}
*/































































































































































































