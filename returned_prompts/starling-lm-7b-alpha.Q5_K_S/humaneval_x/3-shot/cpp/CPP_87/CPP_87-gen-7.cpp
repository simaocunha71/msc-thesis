    vector<vector<int>> result;
    int i,j;
    for (i=0;i<lst.size();i++)
    {
        for (j=0;j<lst[i].size();j++)
        {
            if (lst[i][j]==x)
            {
                vector<int> temp;
                temp.push_back(i);
                temp.push_back(j);
                result.push_back(temp);
            }
        }
    }
    sort(result.begin(), result.end());
    return result;
}


