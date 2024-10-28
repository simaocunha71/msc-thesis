    int max_count = 0;
    for(int i=0;i<grid.size();i++){
        int count = 0;
        for(int j=0;j<grid[i].size();j++){
            if(grid[i][j]==1){
                count++;
            }
        }
        if(count>max_count){
            max_count = count;
        }
    }
    if(max_count<=capacity){
        return max_count;
    }
    else{
        return capacity;
    }
}

int main(){
    vector<vector<int>> grid;
    int capacity;
    grid.push_back({0,0,1,0});
    grid.push_back({0,1,0,0});
    grid.push_back({1,1,1,1});
    capacity = 1;
    printf("%d\n",max_fill(grid,capacity));
}