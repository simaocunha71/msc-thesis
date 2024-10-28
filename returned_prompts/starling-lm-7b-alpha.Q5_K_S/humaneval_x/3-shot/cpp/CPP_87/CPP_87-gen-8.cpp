    vector<vector<int>> all_coords;
    vector<int> coord;
    int i,j;
    for (i=0;i<lst.size();i++)
    for (j=0;j<lst[i].size();j++)
    if (lst[i][j]==x)
    {
        coord.push_back(i);
        coord.push_back(j);
        all_coords.push_back(coord);
        coord.clear();
    }
    sort(all_coords.begin(), all_coords.end());
    return all_coords;
}


