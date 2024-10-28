    vector<vector<int>> result;
    vector<int> temp;
    int row=0;
    int col=0;
    for (int i=0;i<lst.size();i++)
    {
        row=0;
        for (int j=0;j<lst[i].size();j++)
        {
            if (lst[i][j]==x)
            {
                temp={row, col};
                result.push_back(temp);
            }
            col++;
        }
        row++;
        col=0;
    }
    sort(result.begin(), result.end(),
        [](vector<int>& v1, vector<int>& v2) {
            if (v1[0] < v2[0])
                return true;
            else if (v1[0] > v2[0])
                return false;
            else
                return v1[1] > v2[1];
        });
    return result;
}


