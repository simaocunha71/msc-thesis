    vector<vector<int>> all_row;
    vector<int> tmp;
    int i,j;
    for (i=0;i<lst.size();i++)
    for (j=0;j<lst[i].size();j++)
    if (x==lst[i][j])
    {
        tmp.push_back(i);
        tmp.push_back(j);
        all_row.push_back(tmp);
        tmp.clear();
    }

    sort(all_row.begin(), all_row.end());
    return all_row;
}



