    int i,j;
    int start,end;
    if (interval1[0]>interval2[1]||interval2[0]>interval1[1])
    return "NO";
    start=max(interval1[0],interval2[0]);
    end=min(interval1[1],interval2[1]);
    int length=end-start+1;
    if (length==1){
    return "NO";
    }
    for (i=2;i<=sqrt(length);i++)
    if (length%i==0){
    return "NO";
    }
    return "YES";
}


