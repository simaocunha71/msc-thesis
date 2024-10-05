    int i,j;
    int rows=grid.size();
    int cols=grid[0].size();
    int r,c;
    vector<int> path;
    vector<int> curr_path;
    int min_path_val;
    int min_path_val_so_far;

    min_path_val_so_far=(1<<30);
    for (i=0;i<rows;i++)
    for (j=0;j<cols;j++)
    {
        r=i+1;
        c=j+1;
        curr_path.push_back(grid[i][j]);
        if (i<rows-1)
        curr_path.push_back(grid[i+1][j]);
        if (j<cols-1)
        curr_path.push_back(grid[i][j+1]);
        if (i<rows-1 && j<cols-1)
        curr_path.push_back(grid[i+1][j+1]);
        if (curr_path.size()<k)
        continue;
        min_path_val=0;
        for (int k=0;k<curr_path.size();k++)
        {
            min_path_val=min(min_path_val,curr_path[k]);
        }
        if (min_path_val<min_path_val_so_far)
        {
            min_path_val_so_far=min_path_val;
            path=curr_path;
        }
        curr_path.clear();
    }

    return path;
}







