    vector<vector<int>> all_paths;
    vector<int> min_path;
    int i,j;
    for (i=0;i<grid.size();i++)
    for (j=0;j<grid[i].size();j++)
    {
        vector<int> current_path;
        current_path.push_back(grid[i][j]);
    }
    return min_path;
}

