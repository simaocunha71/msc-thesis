    vector<vector<int>> res;
    vector<int> temp;
    int i,j;
    int row;
    int col;
    for (i=0;i<lst.size();i++)
    {
        temp.clear();
        for (j=0;j<lst[i].size();j++)
        if (lst[i][j]==x)
        {
            temp.push_back(i);
            temp.push_back(j);
            res.push_back(temp);
            temp.clear();
        }
    }
    for (i=0;i<res.size();i++)
    {
        row=res[i][0];
        col=res[i][1];
        for (j=i+1;j<res.size();j++)
        {
            if (res[j][0]<row)
            {
                temp=res[j];
                res[j]=res[i];
                res[i]=temp;
            }
        }
    }
    for (i=0;i<res.size();i++)
    {
        row=res[i][0];
        for (j=0;j<res.size();j++)
        {
            if (res[j][0]==row)
            {
                col=res[j][1];
                for (int k=j+1;k<res.size();k++)
                {
                    if (res[k][1]>col)
                    {
                        temp=res[k];
                        res[k]=res[j];
                        res[j]=temp;
                    }
                }
            }
        }
    }
    return res;
}



