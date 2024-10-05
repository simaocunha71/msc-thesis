    if (n==1) return 1;
    if (n==2) return 1;
    int a=1,b=1;
    int res=1;
    for (int i=3;i<=n;i++)
    {
        res=a+b;
        a=b;
        b=res;
    }
    return res;
}