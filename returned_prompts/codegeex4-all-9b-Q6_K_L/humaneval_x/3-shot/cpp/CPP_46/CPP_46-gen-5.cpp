    int a,b,c,d;
    int result;
    if (n==0)
    return 0;
    if (n==1)
    return 0;
    if (n==2)
    return 2;
    if (n==3)
    return 0;
    a=0;
    b=0;
    c=2;
    d=0;
    for (int i=4;i<=n;i++)
    {
        result=a+b+c+d;
        a=b;
        b=c;
        c=d;
        d=result;
    }
    return result;
}

