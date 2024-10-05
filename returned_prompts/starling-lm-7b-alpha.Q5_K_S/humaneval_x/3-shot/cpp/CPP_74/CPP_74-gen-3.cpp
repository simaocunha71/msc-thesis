    int i,j;
    int sum1,sum2;
    vector<string> result;
    for (i=0;i<lst1.size();i++)
    {
        sum1=0;
        for (j=0;j<lst1[i].length();j++)
        sum1+=lst1[i][j];
        sum2=0;
        for (j=0;j<lst2[i].length();j++)
        sum2+=lst2[i][j];
        if (sum1<sum2)
        result.push_back(lst1[i]);
        else if (sum1==sum2)
        {
            result.push_back(lst1[i]);
            break;
        }
    }
    for (i=0;i<lst2.size();i++)
    {
        sum1=0;
        for (j=0;j<lst1.size();j++)
        sum1+=lst1[j].length();
        sum2=0;
        for (j=0;j<lst2[i].length();j++)
        sum2+=lst2[i][j];
        if (sum1<sum2)
        result.push_back(lst2[i]);
        else if (sum1==sum2)
        {
            result.push_back(lst2[i]);
            break;
        }
    }
    return result;
}




