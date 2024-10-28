    int a=0,b=0,c=1;
    int i;
    if (n<=2)
    return 1;
    for (i=3;i<=n;i++)
    {
        a=b;
        b=c;
        c=a+b+c;
    }
    return c;
}

