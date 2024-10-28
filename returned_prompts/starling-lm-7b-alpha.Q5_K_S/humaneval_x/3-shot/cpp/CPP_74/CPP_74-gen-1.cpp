    int i;
    int sum1=0;
    int sum2=0;
    for (i=0;i<lst1.size();i++)
    sum1+=lst1[i].size();
    for (i=0;i<lst2.size();i++)
    sum2+=lst2[i].size();
    if (sum1<sum2)
    return lst1;
    if (sum2<sum1)
    return lst2;
    return lst1;
}




