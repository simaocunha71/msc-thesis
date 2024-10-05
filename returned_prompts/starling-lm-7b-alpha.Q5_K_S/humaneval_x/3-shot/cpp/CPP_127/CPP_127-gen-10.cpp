    int i1,i2,start,end;
    i1=interval1[0];
    i2=interval1[1];
    start=max(i1,i2);
    i1=interval2[0];
    i2=interval2[1];
    end=min(i1,i2);
    if (start>end)
    return "NO";
    if (end-start==1)
    return "NO";
    for (i1=start;i1<=end;i1++)
    {
        if (i1%2==0)
        return "YES";
    }
    return "NO";
}


