    int count = 0;
    for(int i = 0; i < grid.size(); i++){
        int sum = 0;
        for(int j = 0; j < grid[i].size(); j++){
            sum += grid[i][j];
        }
        count += sum / capacity;
    }
    return count;
}

int main() {
    vector<vector<int>> grid = {{0,0,1,0}, {0,1,0,0}, {1,1,1,1}};
    int capacity = 1;
    printf("%d\n", max_fill(grid, capacity));  // Output: 6
    return 0;
}*/



