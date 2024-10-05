    int a[1000];
    a[0]=0;
    a[1]=0;
    a[2]=1;
    int i;
    for (i=3;i<=n;i++)
    {
        a[i]=a[i-1]+a[i-2]+a[i-3];
    }
    return a[n];
}

