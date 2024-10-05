    int a=max(interval1[0], interval2[0]);
    int b=min(interval1[1], interval2[1]);
    int len=b-a;
    if(len<0)
        return "NO";
    if(len==0||len==1)
        return "NO";
    for(int i=2;i*i<=len;i++)
        if(len%i==0)
            return "NO";
    return "YES";
}

