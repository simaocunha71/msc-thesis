    if(k == 1){
        return {1};
    }
    vector<vector<int>> grid2(grid.size(), vector<int>(grid[0].size() + 1));
    for(int i = 0; i < grid.size(); ++i){
        for(int j = 0; j < grid[0].size(); ++j){
            grid2[i][j] = grid[i][j];
        }
    }
    vector<vector<int>> grid3(grid2.size(), vector<int>(grid2[0].size() + 1));
    for(int i = 0; i < grid2.size(); ++i){
        for(int j = 0; j < grid2[0].size(); ++j){
            grid3[i][j] = grid2[i][j];
        }
    }

    int l = 0;
    for(int i = 0; i < grid2.size(); ++i){
        for(int j = 0; j < grid2[0].size(); ++j){
            if(grid2[i][j] == 1){
                grid2[i][j] = ++l;
            }
        }
    }
    int r = l;
    for(int i = grid3.size() - 1; i >= 0; --i){
        for(int j = grid3[0].size() - 1; j >= 0; --j){
            if(grid3[i][j] == r){
                grid3[i][j] = --r;
            }
        }
    }
    vector<int> res;
    for(int i = 0; i < grid.size(); ++i){
        for(int j = 0; j < grid[0].size(); ++j){
            if(grid[i][j] == k){
                res.push_back(grid2[i][j]);
                goto A;
            }
        }
    }
    return res;
}
int main(){
    vector<vector<int>> grid = {{5,9,3},{4,1,6