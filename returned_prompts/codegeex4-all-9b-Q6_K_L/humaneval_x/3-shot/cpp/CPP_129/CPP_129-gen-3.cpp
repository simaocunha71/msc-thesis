    vector<int> path;
    int i,j;
    for (i=0;i<grid.size();i++)
    for (j=0;j<grid.size();j++)
    if (grid[i][j]==1)
    path.push_back(grid[i][j]);

    return path;
}

