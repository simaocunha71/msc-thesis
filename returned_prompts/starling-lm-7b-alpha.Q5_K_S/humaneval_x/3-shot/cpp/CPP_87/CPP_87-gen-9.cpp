    vector<vector<int>> result;
    int i,j;
    for (i=0;i<lst.size();i++)
    for (j=0;j<lst[i].size();j++)
    if (lst[i][j]==x)
    {result.push_back({i,j});}

    sort(result.begin(),result.end());
    return result;
}



