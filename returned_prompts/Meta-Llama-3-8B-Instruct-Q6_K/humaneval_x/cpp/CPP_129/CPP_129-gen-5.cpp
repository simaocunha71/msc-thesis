    int N = grid.size();
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(grid[i][j] == 1){
                vector<int> path;
                vector<vector<int>> visited(N, vector<int>(N, 0));
                dfs(grid, i, j, k, path, visited);
                return path;
            }
        }
    }
    return {};
}

void dfs(vector<vector<int>> grid, int i, int j, int k, vector<int>& path, vector<vector<int>>& visited){
    int N = grid.size();
    if(k == 0) return;
    path.push_back(grid[i][j]);
    visited[i][j] = 1;
    for(int x = -1; x <= 1; x++){
        for(int y = -1; y <= 1; y++){
            if(x == 0 && y == 0) continue;
            int ni = i + x, nj = j + y;
            if(ni >= 0 && ni < N && nj >= 0 && nj < N && !visited[ni][nj]){
                dfs(grid, ni, nj, k-1, path, visited);
            }
        }
    }
    path.pop_back();
    visited[i][j] = 0;
}

int main(int argc, char const *argv[]) {
    vector<vector<int>> grid = {{1,2,3},{4,5,6},{7,8,9}};
    int k = 3;
    vector<int> result = minPath(grid, k);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
} 
