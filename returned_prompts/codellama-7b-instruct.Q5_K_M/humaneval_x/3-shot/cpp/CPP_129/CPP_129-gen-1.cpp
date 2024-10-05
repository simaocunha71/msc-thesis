    vector<int> values;
    int i,j;
    for (i=0;i<grid.size();i++){
        for (j=0;j<grid[i].size();j++){
            values.push_back(grid[i][j]);
        }
    }
    return values;
}


