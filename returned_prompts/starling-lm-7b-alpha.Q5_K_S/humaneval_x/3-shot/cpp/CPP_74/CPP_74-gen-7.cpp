    int i,j,sum1=0,sum2=0;
    for (i=0;i<lst1.size();i++)
    sum1+=lst1[i].length();
    for (i=0;i<lst2.size();i++)
    sum2+=lst2[i].length();
    if (sum1<sum2)
    return lst1;
    if (sum1>sum2)
    return lst2;
    return lst1;
}



