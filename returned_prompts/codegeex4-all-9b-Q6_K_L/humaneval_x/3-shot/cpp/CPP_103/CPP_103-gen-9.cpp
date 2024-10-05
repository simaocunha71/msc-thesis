    if (n>m)
    return "-1";
    int sum=0;
    int count=0;
    int i;
    for (i=n;i<=m;i++)
    {
        sum+=i;
        count+=1;
    }
    int avg=sum/count;
    return to_string(avg);
}

