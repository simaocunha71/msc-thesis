    int rows=grid.size();
    int cols=grid[0].size();
    int min_path[rows][cols];
    int min_path_len[rows][cols];
    for (int i=0;i<rows;i++)
    for (int j=0;j<cols;j++)
    {
        min_path[i][j]=0;
        min_path_len[i][j]=1;
    }

    int min_path_len_total=1;
    vector<int> min_path_values;
    for (int i=0;i<rows;i++)
    for (int j=0;j<cols;j++)
    {
        min_path_values.push_back(grid[i][j]);
    }

    for (int k=2;k<=rows*cols;k++)
    {
        for (int i=0;i<rows;i++)
        for (int j=0;j<cols;j++)
        {
            int min_path_len_temp=min_path_len[i][j];
            int min_path_temp=min_path[i][j];
            if (i>0)
            {
                if (min_path_len_temp>min_path_len[i-1][j]+1)
                {
                    min_path_temp=i-1;
                    min_path_len_temp=min_path_len[i-1][j]+1;
                }
            }
            if (j>0)
            {
                if (min_path_len_temp>min_path_len[i][j-1]+1)
                {
                    min_path_temp=i;
                    min_path_len_temp=min_path_len[i][j-1]+1;
                }
            }
            if (i<rows-1)
            {
                if (min_path_len_temp>min_path_len[i+1][j]+1)
                {
                    min_path_temp=i+1;
                    min_path_len_temp=min_path