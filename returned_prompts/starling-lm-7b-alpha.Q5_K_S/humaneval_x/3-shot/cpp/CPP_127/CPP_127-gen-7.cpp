    int i,j;
    for (i=0;i<interval1.size();i++)
    if (interval1[i]>interval2[i])
    return "NO";

    int start=max(interval1[0], interval2[0]);
    int end=min(interval1[1], interval2[1]);
    if (end<start)
    return "NO";
    if (end-start==1)
    return "YES";

    return "NO";
}




