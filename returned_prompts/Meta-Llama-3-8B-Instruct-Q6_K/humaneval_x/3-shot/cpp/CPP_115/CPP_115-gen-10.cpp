    int total_water = 0;
    int bucket = 0;
    int water = 0;
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[i].size(); j++) {
            total_water += grid[i][j];
        }
    }
    while (total_water > 0) {
        bucket = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) {
                if (grid[i][j] > 0) {
                    grid[i][j]--;
                    bucket++;
                    water++;
                }
                if (water >= capacity) {
                    total_water -= capacity;
                    water = 0;
                }
            }
        }
    }
    return bucket;
}