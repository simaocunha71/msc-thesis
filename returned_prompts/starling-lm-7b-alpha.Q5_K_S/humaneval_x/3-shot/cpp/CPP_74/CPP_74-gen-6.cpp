    int i;
    int n1=0,n2=0;
    for (i=0;i<lst1.size();i++)
    n1+=lst1[i].length();
    for (i=0;i<lst2.size();i++)
    n2+=lst2[i].length();

    if (n1<n2)
    return lst1;
    if (n2<n1)
    return lst2;

    return lst1;
}


