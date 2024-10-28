    if (n>m)
        return "-1";
    int sum=0;
    for (int i=n;i<=m;i++)
        sum+=i;
    int avg=sum/(m-n+1);
    return to_string(avg);
}


