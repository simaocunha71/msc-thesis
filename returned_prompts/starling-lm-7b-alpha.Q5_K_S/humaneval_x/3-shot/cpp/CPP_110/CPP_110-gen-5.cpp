    int i;
    int o=0;
    int e=0;
    for (i=0;i<lst1.size();i++)
    if (lst1[i]%2==0)
    e+=1;
    else
    o+=1;

    for (i=0;i<lst2.size();i++)
    if (lst2[i]%2==0)
    e+=1;
    else
    o+=1;

    if (o<e)
    return "YES";
    else
    return "NO";
}



