    vector<vector<int>> lst_ret;
    vector<int> temp;
    int i,j,n;
    for (i=0;i<lst.size();i++)
    {
        n=0;
        for (j=0;j<lst[i].size();j++)
        {
            if (lst[i][j]==x)
            {
                temp.push_back(i);
                temp.push_back(j);
                lst_ret.push_back(temp);
                temp.clear();
            }
        }
    }
    return lst_ret;
}



