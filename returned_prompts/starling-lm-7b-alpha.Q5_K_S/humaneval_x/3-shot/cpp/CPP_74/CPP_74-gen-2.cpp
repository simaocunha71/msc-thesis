    int i,j,sum1,sum2;
    vector<string> result;
    for (i=0;i<lst1.size();i++)
    {
        sum1=0;
        for (j=0;j<lst1[i].length();j++)
        sum1+=lst1[i][j];
        if (sum1<sum2)
        {
            result.push_back(lst1[i]);
        }
    }
    return result;
}


