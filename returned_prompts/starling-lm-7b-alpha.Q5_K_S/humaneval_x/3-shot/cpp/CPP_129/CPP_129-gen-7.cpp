    int i,j,n,m;
    n=grid.size();
    m=grid[0].size();
    int kk=k%n;
    if (kk==0)
    kk=n;
    vector<vector<int>> new_grid;
    for (i=0;i<n;i++)
    {
        vector<int> new_row;
        for (j=0;j<m;j++)
        {
            new_row.push_back(grid[i][j]+grid[i][(j+kk)%m]);
        }
        new_grid.push_back(new_row);
    }
    vector<int> path;
    for (i=0;i<k/n;i++)
    {
        vector<int> new_path;
        int min_val;
        for (j=0;j<n;j++)
        {
            min_val=1000000;
            for (int l=0;l<m;l++)
            {
                if (min_val>new_grid[j][l])
                {
                    min_val=new_grid[j][l];
                }
            }
            new_path.push_back(min_val);
        }
        path.insert(path.end(),new_path.begin(),new_path.end());
    }
    return path;
}



