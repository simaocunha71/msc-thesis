    int rows = grid.size();
    int cols = grid[0].size();
    int res = 0;
    vector<vector<int>> visited(rows, vector<int>(cols,0));
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            if(visited[i][j] == 0){
                int fill = dfs(grid, visited, i, j, capacity);
                res += fill;
            }
        }
    }
    return res;
}
int dfs(vector<vector<int>>& grid, vector<vector<int>>& visited, int i, int j, int capacity){
    if(i < 0 || i >= grid.size() || j < 0 || j >= grid[0].size() || visited[i][j] == 1){
        return 0;
    }
    int fill = 0;
    if(grid[i][j] == 1){
        fill = min(capacity, 1);
        capacity -= fill;
        visited[i][j] = 1;
    }
    int res = 0;
    for(int k = -1; k <= 1; k++){
        for(int l = -1; l <= 1; l++){
            if(k == 0 && l == 0){
                continue;
            }
            int ni = i + k;
            int nj = j + l;
            if(ni >= 0 && ni < grid.size() && nj >= 0 && nj < grid[0].size() && visited[ni][nj] == 0){
                res += dfs(grid, visited, ni, nj, capacity);
            }
        }
    }
    return res + fill;
}

int main(){
    vector<vector<int>> grid = {{0,0,1,0}, {0,1,0,0}, {1,1,1,1}};
    int capacity = 1;
    printf("%d\n",max_fill(grid, capacity));
    return 0;
}
*/



