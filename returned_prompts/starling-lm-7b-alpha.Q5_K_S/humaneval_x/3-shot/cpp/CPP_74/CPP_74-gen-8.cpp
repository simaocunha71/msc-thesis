    int i,j;
    int sum1=0;
    int sum2=0;
    for (i=0;i<lst1.size();i++)
    sum1+=lst1[i].length();
    for (j=0;j<lst2.size();j++)
    sum2+=lst2[j].length();

    if (sum1<sum2) return lst1;
    if (sum1>sum2) return lst2;
    return lst1;
}




