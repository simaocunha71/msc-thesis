    vector<vector<int>> coords;
    for (int i=0;i<lst.size();i++)
    for (int j=0;j<lst[i].size();j++)
    if (lst[i][j]==x)
    {
        vector<int> coord;
        coord.push_back(i);
        coord.push_back(j);
        coords.push_back(coord);
    }
    return coords;
}



