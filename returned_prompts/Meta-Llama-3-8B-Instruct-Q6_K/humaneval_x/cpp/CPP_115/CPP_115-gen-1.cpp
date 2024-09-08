    int rows = grid.size();
    int cols = grid[0].size();
    int count = 0;
    for(int i =0; i<rows; i++){
        int water=0;
        for(int j =0; j<cols; j++){
            if(grid[i][j]==1){
                water++;
            }
        }
        count+=water/capacity;
        if(water%capacity!=0)count++;
    }
    return count;
}

int main(){
    vector<vector<int>> grid = {{0,0,1,0}, {0,1,0,0}, {1,1,1,1}};
    int capacity = 1;
    printf("%d\n",max_fill(grid, capacity));
    return 0;
}

