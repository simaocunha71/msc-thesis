    if (n==0) return 0;
    if (n==1) return 0;
    if (n==2) return 2;
    if (n==3) return 0;
    int a=0,b=2,c=0,i;
    for (i=4;i<=n;i++)
    {
        c=a+b;
        a=b;
        b=c;
    }
    return c;
}


