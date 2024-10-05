    int start=0,end=0;
    if (interval1[0]>interval2[0])
        start=interval1[0];
    else
        start=interval2[0];
    if (interval1[1]<interval2[1])
        end=interval1[1];
    else
        end=interval2[1];
    if (end-start<0)
        return "NO";
    if (end-start==1)
        return "YES";
    if (end-start==2)
        return "YES";

    int i=2;
    while (i*i<=end-start){
        if ((end-start)%i==0)
        return "NO";
        i+=1;
    }
    return "YES";
}

