    int start1=interval1[0];
    int end1=interval1[1];
    int start2=interval2[0];
    int end2=interval2[1];
    if (start1>end2 || start2>end1)
    return "NO";
    int start=max(start1,start2);
    int end=min(end1,end2);
    int len=end-start+1;
    for (int i=2;i<=len;i++)
    if (len%i==0)
    return "NO";
    return "YES";
}


