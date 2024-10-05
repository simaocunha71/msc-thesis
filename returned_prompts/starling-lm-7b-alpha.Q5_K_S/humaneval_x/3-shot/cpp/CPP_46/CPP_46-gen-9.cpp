    int a=0,b=0,c=2,d=0;
    int i;
    if (n==0) return 0;
    if (n==1) return 0;
    if (n==2) return 2;
    if (n==3) return 0;
    for (i=4;i<=n;i++)
    {
        d=c;
        c=a+b+c;
        a=b;
        b=d;
    }
    return c;
}


