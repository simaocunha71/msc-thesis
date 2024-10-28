    vector<vector<int>> row_with_col;
    vector<int> row;
    int i,j,n=0;
    for (i=0;i<lst.size();i++)
    {
    for (j=0;j<lst[i].size();j++)
    if (lst[i][j]==x)
    {
        row.push_back(i);
        row.push_back(j);
        row_with_col.push_back(row);
        n+=1;
        row.clear();
    }
    }
    if (n>0)
    {
    for (i=0;i<row_with_col.size();i++)
    {
        for (j=0;j<row_with_col.size()-1;j++)
        {
            if (row_with_col[j][0]>row_with_col[j+1][0])
            {
                row_with_col[j].swap(row_with_col[j+1]);
            }
        }
    }
    for (i=0;i<row_with_col.size();i++)
    {
        for (j=0;j<row_with_col[i].size()-1;j++)
        {
            if (row_with_col[i][1]<row_with_col[i+1][1])
            {
                row_with_col[i].swap(row_with_col[i+1]);
            }
        }
    }
    }
    return row_with_col;
}


