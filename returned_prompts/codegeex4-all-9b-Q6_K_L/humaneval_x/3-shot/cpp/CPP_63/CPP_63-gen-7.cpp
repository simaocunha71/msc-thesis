    int a=0;
    int b=0;
    int c=1;
    int d;
    int i;
    if (n==0||n==1)
    return 0;
    if (n==2)
    return 1;
    for (i=3;i<=n;i++)
    {
        d=a+b+c;
        a=b;
        b=c;
        c=d;
    }
    return d;
}

