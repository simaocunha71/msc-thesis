    int n = grid.size();
    vector<int> res;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            vector<int> temp;
            dfs(grid, i, j, k, temp, res);
        }
    }
    return res;
}

void dfs(vector<vector<int>>& grid, int i, int j, int k, vector<int>& temp, vector<int>& res){
    if(k == 0){
        res = temp;
        return;
    }
    if(i < 0 || i >= grid.size() || j < 0 || j >= grid.size() || visited[i][j]){
        return;
    }
    visited[i][j] = true;
    temp.push_back(grid[i][j]);
    dfs(grid, i-1, j, k-1, temp, res);
    dfs(grid, i+1, j, k-1, temp, res);
    dfs(grid, i, j-1, k-1, temp, res);
    dfs(grid, i, j+1, k-1, temp, res);
    visited[i][j] = false;
    temp.pop_back();
}

int main(){
    vector<vector<int>> grid = {{1,2,3},{4,5,6},{7,8,9}};
    int k = 3;
    vector<int> res = minPath(grid, k);
    for(int i = 0; i < res.size(); i++){
        printf("%d ", res[i]);
    }
    printf("\n");
    return 0;
}
