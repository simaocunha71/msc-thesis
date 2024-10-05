    if (n==0)
    return 0;
    if (n==1)
    return 0;
    if (n==2)
    return 1;
    int f0=0, f1=0, f2=1;
    int i;
    for (i=3;i<=n;i++)
    {
        int temp = f1+f2+f0;
        f0=f1;
        f1=f2;
        f2=temp;
    }
    return f2;
}

