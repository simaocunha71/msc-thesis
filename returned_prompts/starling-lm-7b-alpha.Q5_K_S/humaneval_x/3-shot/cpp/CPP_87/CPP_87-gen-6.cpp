    vector<vector<int>> res;
    int i,j,l;
    for (i=0;i<lst.size();i++)
    {
        for (j=0;j<lst[i].size();j++)
        {
            if (lst[i][j]==x)
            {
                vector<int> tmp;
                tmp.push_back(i);
                tmp.push_back(j);
                res.push_back(tmp);
            }
        }
    }

    sort(res.begin(), res.end());
    return res;
}




