    int i,j;
    int l1,l2;
    int start;
    int end;
    if (interval1[0]>interval2[1])
    return "NO";
    if (interval1[1]<interval2[0])
    return "NO";
    start=max(interval1[0],interval2[0]);
    end=min(interval1[1],interval2[1]);
    l1=end-start+1;
    if (l1==1)
    return "YES";
    for (i=2;i<=l1/2;i++)
    if (l1%i==0)
    return "NO";
    return "YES";
}



