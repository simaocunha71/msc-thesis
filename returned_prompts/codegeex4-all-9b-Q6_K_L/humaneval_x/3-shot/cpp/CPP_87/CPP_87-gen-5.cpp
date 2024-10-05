    vector<vector<int>> coordinates;
    int row,column;
    for (row=0;row<lst.size();row++)
    {
        for (column=lst[row].size()-1;column>=0;column--)
        {
            if (lst[row][column]==x)
            {
                coordinates.push_back({row,column});
            }
        }
    }
    return coordinates;
}

