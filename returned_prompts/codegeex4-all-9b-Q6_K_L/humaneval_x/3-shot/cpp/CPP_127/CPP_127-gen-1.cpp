    int start, end;
    if (interval1[0]>interval2[0])
        start=interval1[0];
    else start=interval2[0];
    if (interval1[1]>interval2[1])
        end=interval2[1];
    else end=interval1[1];
    if (start>end)
        return "NO";
    int len=end-start+1;
    if (len<2)
        return "NO";
    for (int i=2;i<len;i++)
    {
        if (len%i==0)
            return "NO";
    }
    return "YES";
}

