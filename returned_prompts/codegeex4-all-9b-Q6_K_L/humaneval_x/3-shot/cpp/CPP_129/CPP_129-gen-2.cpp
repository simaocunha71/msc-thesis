    vector<int> min_path;
    int i,j;
    int min=grid.size()*grid.size();
    for (i=0;i<grid.size();i++)
    for (j=0;j<grid.size();j++)
    if (grid[i][j]<min)
    min=grid[i][j];
    min_path.push_back(min);
    return min_path;
}

