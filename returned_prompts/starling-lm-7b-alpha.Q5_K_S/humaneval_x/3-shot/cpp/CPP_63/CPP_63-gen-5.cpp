    if (n==0 || n==1) return 0;
    if (n==2) return 1;
    int a=0,b=1,c,i;
    for (i=3;i<=n;i++)
    {
        c=a+b;
        a=b;
        b=c;
    }
    return c;
}


