    for(int i=grid.size()-1;i>=0;i--){
        for(int j=0;j<grid[0].size();j++){
            if(grid[i][j]==1){
                int counter=0;
                int k=i;
                while(k<grid.size()){
                    if(grid[k][j]==1){
                        counter++;
                        grid[k][j]=0;
                    }
                    k++;
                }
                if(counter>capacity)
                    goto A;
            }
        }
    }
    return 0;
}
int min_fill(vector<vector<int>> grid,int capacity){
    int counter=0;
    for(int i=0;i<grid.size();i++){
        for(int j=0;j<grid[0].size();j++){
            if(grid[i][j]==1){
                int k=i;
                while(k<grid.size()){
                    if(grid[k][j]==1){
                        counter++;
                        grid[k][j]=0;
                    }
                    k++;
                }
            }
        }
    }
    return counter;
}
int main(){
    vector<vector<int>> grid;
    grid.push_back({1,0,0,0});
    grid.push_back({0,0,1,0});
    grid.push_back({0,1,0,0});
    grid.push_back({1,1,1,0});
    grid.push_back({0,0,1,0});
    grid.push_back({0,0,1,0});
    grid.push_back({0,0,1,0});
    grid.push_back({0,0,1,0});
    grid.push_back({0,0,1,0});
    grid.push_back({0,0,1,0});
    grid.push_back({0,0,1,0});
    grid.push_back({0,0,1,0});
    grid.push