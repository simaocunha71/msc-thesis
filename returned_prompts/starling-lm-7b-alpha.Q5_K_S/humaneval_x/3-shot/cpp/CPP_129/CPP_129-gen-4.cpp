    int i,j,row,col,min_row,min_col;
    int k_minus_1;
    vector<vector<int>> path;
    vector<int> p;
    int k_size;
    vector<int> current_path;
    int current_path_size;
    int smallest_num;
    int smallest_num_row;
    int smallest_num_col;

    k_minus_1=k-1;
    k_size=k;
    if (k==1)
    {
    for (i=0;i<grid.size();i++)
    for (j=0;j<grid[i].size();j++)
    {
        if (grid[i][j]==1)
        {
        p.push_back(grid[i][j]);
        break;
        }
    }
    return p;
    }
    for (i=0;i<grid.size();i++)
    for (j=0;j<grid[i].size();j++)
    {
        if (grid[i][j]==1)
        {
        current_path_size=0;
        current_path.clear();
        path.push_back(current_path);
        current_path.push_back(grid[i][j]);
        min_row=i;
        min_col=j;
        while (current_path_size!=k_size)
        {
        smallest_num=100000000;
        for (row=min_row-1;row<=min_row+1;row++)
        for (col=min_col-1;col<=min_col+1;col++)
        if (row>=0&&row<grid.size()&&col>=0&&col<grid[row].size())
        if (smallest_num>grid[row][col])
        {
        smallest_num=grid[row][col];
        smallest_num_row=row;
        smallest_num_col=col;
        }
        current_path.push_back(smallest_num);
        current_path_size+=1;
       