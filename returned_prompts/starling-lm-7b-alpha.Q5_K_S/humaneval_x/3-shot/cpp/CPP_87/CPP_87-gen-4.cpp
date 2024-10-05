    vector<vector<int>> all_rows;
    vector<int> all_cols;
    int i,j;
    for (i=0;i<lst.size();i++)
    {
        if (x==lst[i].size())
        {
            all_cols.clear();
            for (j=lst[i].size()-1;j>=0;j--)
            all_cols.push_back(lst[i][j]);
            all_rows.push_back(all_cols);
        }
    }

    sort(all_rows.begin(), all_rows.end(), [](vector<int> a, vector<int> b) {return a[0]<b[0];});
    for (i=1;i<all_rows.size();i++)
    {
        if (all_rows[i][0]==all_rows[i-1][0])
        sort(all_rows[i].begin(), all_rows[i].end(), [](int a, int b) {return a>b;});
    }
    return all_rows;
}


