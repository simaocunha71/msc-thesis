    int rows = grid.size();
    int cols = grid[0].size();
    int total_water_units = 0;
    for(int i=0; i<rows; i++){
        for(int j=0; j<cols; j++){
            total_water_units += grid[i][j];
        }
    }
    return (total_water_units + capacity - 1) / capacity;
}


