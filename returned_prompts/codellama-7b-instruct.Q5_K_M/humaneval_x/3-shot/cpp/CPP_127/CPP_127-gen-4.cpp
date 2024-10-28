    int start1,start2,end1,end2,length;
    start1=interval1[0];
    end1=interval1[1];
    start2=interval2[0];
    end2=interval2[1];
    if (start1>end2||end1<start2)
    return "NO";
    else
    {
    start2=max(start1,start2);
    start1=min(start1,start2);
    end1=min(end1,end2);
    end2=max(end1,end2);
    length=end2-start2;
    if (length==0)
    return "NO";
    for (int i=2;i<=length;i++)
    if (length%i==0)
    return "NO";
    return "YES";
    }
}



