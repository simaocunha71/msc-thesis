    int i,j;
    int odd_cnt=0;
    int even_cnt=0;
    for (i=0;i<lst1.size();i++)
    if (lst1[i]%2==1)
    odd_cnt+=1;
    for (i=0;i<lst2.size();i++)
    if (lst2[i]%2==1)
    even_cnt+=1;
    if (odd_cnt>even_cnt)
    return "NO";
    else
    return "YES";
}



