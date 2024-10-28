    int i,j;
    vector<string> res;
    int sum1=0,sum2=0;
    for (i=0;i<lst1.size();i++)
    sum1+=lst1[i].length();
    for (i=0;i<lst2.size();i++)
    sum2+=lst2[i].length();

    if (sum1<sum2)
    return lst1;
    else if (sum1>sum2)
    return lst2;
    else
    {
        for (i=0;i<lst1.size();i++)
        {
            for (j=0;j<lst2.size();j++)
            if (lst1[i]==lst2[j])
            res.push_back(lst1[i]);
        }
    }
    return res;
}



