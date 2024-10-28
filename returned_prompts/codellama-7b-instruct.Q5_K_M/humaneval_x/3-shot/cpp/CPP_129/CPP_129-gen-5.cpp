    int rows = grid.size();
    int columns = grid[0].size();
    vector<int> values;
    int i, j, min_value;
    for (i=0; i<rows; i++)
    for (j=0; j<columns; j++)
    values.push_back(grid[i][j]);
    vector<vector<int>> dp(rows, vector<int>(columns, 0));
    dp[0][0] = values[0];
    for (i=1; i<rows; i++)
    dp[i][0] = dp[i-1][0]+values[i*columns];
    for (j=1; j<columns; j++)
    dp[0][j] = dp[0][j-1]+values[j];
    for (i=1; i<rows; i++)
    for (j=1; j<columns; j++)
    dp[i][j] = min(dp[i-1][j], dp[i][j-1])+values[i*columns+j];
    int index = 0;
    for (i=0; i<rows; i++)
    for (j=0; j<columns; j++)
    if (dp[i][j]<dp[index][0])
    index = i*columns+j;
    vector<int> path;
    int row = index/columns, column = index%columns;
    while (row>0 || column>0)
    {
        path.push_back(values[index]);
        int next_row = row-1, next_column = column;
        if (next_row<0)
        next_row = row;
        if (next_column<0)
        next_column = column-1;
        if (next_row<0 || next_column<0)
        break;
        index = next_row*columns+next_column;
        row = next_row;
        column = next_column;
    }
    return path;
}


