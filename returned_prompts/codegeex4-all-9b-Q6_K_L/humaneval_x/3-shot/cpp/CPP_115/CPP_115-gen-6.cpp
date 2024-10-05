    int row = grid.size();
    int col = grid[0].size();

    int i,j;
    int sum=0;
    int count=0;

    for (i=0;i<row;i++)
    for (j=0;j<col;j++)
    {
        sum+=grid[i][j];
        if (sum==capacity)
        {
            count+=1;
            sum=0;
        }
    }

    if (sum!=0)
    count+=1;

    return count;
}

