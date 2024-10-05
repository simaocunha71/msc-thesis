    int a=0,b=0,c=2,d;
    int i;
    if (n==0) return 0;
    if (n==1) return 0;
    if (n==2) return 2;
    if (n==3) return 0;
    for (i=4;i<=n;i++)
    {
        d=a+b+c;
        a=b;
        b=c;
        c=d;
    }
    return c;
}



