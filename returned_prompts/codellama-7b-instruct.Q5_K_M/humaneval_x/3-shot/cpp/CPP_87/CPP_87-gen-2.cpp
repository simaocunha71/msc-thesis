    vector<vector<int>> result;
    int i,j;
    for (i=0;i<lst.size();i++)
    {
        for (j=0;j<lst[i].size();j++)
        {
            if (lst[i][j]==x)
            {
                vector<int> tmp;
                tmp.push_back(i);
                tmp.push_back(j);
                result.push_back(tmp);
            }
        }
    }
    return result;
}


