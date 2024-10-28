    if (n>m)
        return "-1";
    int sum=0;
    int count=0;
    for (int i=n;i<=m;i++)
    {
        sum+=i;
        count++;
    }
    float avg=sum/(float)count;
    avg=floor(avg);
    string binary;
    while (avg>0)
    {
        binary=(char)((avg%2)+'0')+binary;
        avg/=2;
    }
    if (binary=="")
        binary="0";
    return binary;
}

