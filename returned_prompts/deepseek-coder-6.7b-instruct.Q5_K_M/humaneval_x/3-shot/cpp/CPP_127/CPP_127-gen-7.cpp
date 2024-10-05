    int start=max(interval1[0], interval2[0]);
    int end=min(interval1[1], interval2[1]);
    int len=end-start;
    if(len<0)
        return "NO";
    if(len==1)
        return "NO";
    if(len==2)
        return "NO";
    for(int i=2;i*i<=len;i++)
        if(len%i==0)
            return "NO";
    return "YES";
}


