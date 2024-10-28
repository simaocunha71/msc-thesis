    int i,j;
    int odd_count1=0,odd_count2=0;
    for (i=0;i<lst1.size();i++)
    if (lst1[i]%2!=0)
    odd_count1+=1;
    for (j=0;j<lst2.size();j++)
    if (lst2[j]%2!=0)
    odd_count2+=1;
    if (odd_count1>odd_count2)
    return "NO";
    return "YES";
}


