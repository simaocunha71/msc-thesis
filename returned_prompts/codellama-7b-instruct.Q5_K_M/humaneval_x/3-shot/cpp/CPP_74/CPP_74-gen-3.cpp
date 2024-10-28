    int i,j;
    int total1=0,total2=0;
    for (i=0;i<lst1.size();i++)
    total1+=lst1[i].length();
    for (j=0;j<lst2.size();j++)
    total2+=lst2[j].length();
    if (total1<total2)
    return lst2;
    if (total1>total2)
    return lst1;
    else
    return lst1;
}



