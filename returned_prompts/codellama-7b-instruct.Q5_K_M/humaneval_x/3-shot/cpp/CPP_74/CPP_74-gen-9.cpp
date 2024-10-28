    int i,j;
    int t1=0,t2=0;
    for (i=0;i<lst1.size();i++)
    t1+=lst1[i].length();
    for (j=0;j<lst2.size();j++)
    t2+=lst2[j].length();
    if (t1<t2)
    return lst1;
    else if (t2<t1)
    return lst2;
    else
    return lst1;
}


