    vector<vector<int>> all_coords;
    int i,j;
    vector<int> current_coord;
    for (i=0;i<lst.size();i++)
    for (j=0;j<lst[i].size();j++)
    if (lst[i][j]==x)
    {
        current_coord={i,j};
        all_coords.push_back(current_coord);
    }
    sort(all_coords.begin(), all_coords.end(), [](vector<int> &a, vector<int> &b){ return a[0] < b[0];});
    sort(all_coords.begin(), all_coords.end(), [](vector<int> &a, vector<int> &b){ return a[1] > b[1];});
    return all_coords;
}


