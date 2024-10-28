    int a,b,c,d;
    int i;
    a=0;
    b=0;
    c=2;
    d=0;
    if (n==0)
    return a;
    if (n==1)
    return b;
    if (n==2)
    return c;
    if (n==3)
    return d;
    for (i=4;i<=n;i++)
    {
        int temp;
        temp=a+b+c+d;
        a=b;
        b=c;
        c=d;
        d=temp;
    }
    return d;
}

