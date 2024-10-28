    if (n>m)
        return "-1";
    int sum=0;
    for (int i=n;i<=m;i++)
    sum+=i;
    float avg=(float)sum/(m-n+1);
    int rounded_avg=(int)round(avg);
    string binary;
    while (rounded_avg>0)
    {
        if (rounded_avg%2==1)
            binary="1"+binary;
        else
            binary="0"+binary;
        rounded_avg/=2;
    }
    if (binary=="")
        binary="0";
    return binary;
}