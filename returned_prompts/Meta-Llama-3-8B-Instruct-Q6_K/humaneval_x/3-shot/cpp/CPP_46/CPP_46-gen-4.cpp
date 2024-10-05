    if (n<2) return 0;
    if (n==2) return 2;
    int a=0, b=0, c=2, d=0;
    for (int i=3;i<=n;i++)
    {
        int temp=a+b+c;
        a=b;
        b=c;
        c=temp;
        d=a;
    }
    return d;
}