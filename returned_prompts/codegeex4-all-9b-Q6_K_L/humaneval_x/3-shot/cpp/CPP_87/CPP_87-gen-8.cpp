    vector<vector<int>> coordinates;
    vector<int> coordinate;
    int i,j;
    for (i=0;i<lst.size();i++)
    for (j=0;j<lst[i].size();j++)
    if (lst[i][j]==x)
    {
        coordinate.push_back(i);
        coordinate.push_back(j);
        coordinates.push_back(coordinate);
        coordinate.clear();
    }
    return coordinates;
}

