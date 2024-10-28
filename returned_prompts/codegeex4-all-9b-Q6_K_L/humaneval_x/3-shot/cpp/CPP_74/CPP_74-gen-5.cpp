    int sum1=0,sum2=0,i,j;
    for (i=0;i<lst1.size();i++)
    {
        for (j=0;j<lst1[i].length();j++)
        sum1+=1;
    }
    for (i=0;i<lst2.size();i++)
    {
        for (j=0;j<lst2[i].length();j++)
        sum2+=1;
    }
    if (sum1<sum2)
        return lst1;
    if (sum1>sum2)
        return lst2;
    if (sum1==sum2)
        return lst1;
}

