    vector<vector<int>> result;
    for (int i=0; i<lst.size();i++)
    {
        for (int j=0; j<lst[i].size();j++)
        {
            if (lst[i][j]==x)
            {
                result.push_back({i, j});
            }
        }
    }
    sort(result.begin(), result.end(), [](vector<int> a, vector<int> b) {
        if (a[0] != b[0]) return a[0] < b[0];
        return a[1] > b[1];
    });
    return result;
} // 1-based indexing
// 0-based indexing
// 0-based indexing
// 0-based indexing
// 1-based indexing

