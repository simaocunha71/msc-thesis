    vector<int> grid_path;
    vector<vector<int>> grid_sorted;
    int i,j,m;
    int grid_size=grid.size();
    for (i=0;i<grid_size;i++)
    {
        for (j=0;j<grid_size;j++)
        {
            grid_sorted.push_back(vector<int>(1,grid[i][j]));
        }
    }
    sort(grid_sorted.begin(), grid_sorted.end());
    grid_path.push_back(grid_sorted[0][0]);
    for (m=2;m<k;m++)
    {
        i=m-1;
        j=0;
        while (grid_sorted[i][0]==grid_path[m-2])
        {
            if (j<grid_size)
            {
                grid_path.push_back(grid_sorted[j][0]);
                j+=1;
            }
            else
            {
                i+=1;
                if (i<grid_size)
                {
                    grid_path.push_back(grid_sorted[i][0]);
                }
            }
        }
    }
    return grid_path;
}




































































































































































































