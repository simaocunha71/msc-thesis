    int N = grid.size();
    vector<int> path;
    int i, j;
    for (i = 0; i < N; i++)
        for (j = 0; j < N; j++)
            if (grid[i][j] == 1) {
                path = dfs(grid, i, j, k, path);
                if (!path.empty()) return path;
            }
    return path;
}

vector<int> dfs(vector<vector<int>>& grid, int i, int j, int k, vector<int>& path) {
    int N = grid.size();
    if (k == 0) return path;
    path.push_back(grid[i][j]);
    vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    for (int d = 0; d < 4; d++) {
        int ni = i + directions[d][0];
        int nj = j + directions[d][1];
        if (ni >= 0 && ni < N && nj >= 0 && nj < N && !binary_search(path.begin(), path.end(), grid[ni][nj])) {
            dfs(grid, ni, nj, k - 1, path);
        }
    }
    path.pop_back();
    return path;
}  //dfs

bool binary_search(vector<int>& vec, int target) {
    int left = 0, right = vec.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (vec[mid] == target) return true;
        if (vec[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return false;
}
//binary_search function
//This function checks if a target value exists in a sorted array.
//It returns true if the target value is found in the array and false if it's not.
//The function takes two parameters: the array and the target value.
//The function returns a boolean value.  //binary_search function
//This function checks if a target value exists in a sorted array.
//It returns true if the target value is found in the array and false if it's not.
//The function takes two parameters: the array and the target value.
//The function returns a boolean value.  //binary_search function
//This function checks if