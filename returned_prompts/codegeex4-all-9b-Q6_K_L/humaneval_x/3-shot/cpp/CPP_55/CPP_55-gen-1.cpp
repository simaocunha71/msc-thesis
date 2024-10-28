    if (n==1)
    return 1;
    if (n==0)
    return 0;
    else
    {
        int i;
        int a[n+1];
        a[0]=0;
        a[1]=1;
        for (i=2;i<=n;i++)
        a[i]=a[i-1]+a[i-2];
        return a[n];
    }

}

