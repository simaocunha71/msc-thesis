    int i;
    int ct1=0;
    int ct2=0;
    for (i=0;i<lst1.size();i++)
    if (lst1[i]%2==0)
    ct1+=1;
    for (i=0;i<lst2.size();i++)
    if (lst2[i]%2==0)
    ct2+=1;
    if (ct1>ct2)
    return "NO";
    else
    return "YES";
}





