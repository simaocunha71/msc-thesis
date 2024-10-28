    vector<vector<int>> sorted_rows;
    vector<int> current_row;
    int i,j;
    for (i=0;i<lst.size();i++)
    {
        for (j=0;j<lst[i].size();j++)
        {
            if (lst[i][j]==x)
            {
                current_row.push_back(i);
                current_row.push_back(j);
                sorted_rows.push_back(current_row);
                current_row.clear();
            }
        }
    }
    return sorted_rows;
}





