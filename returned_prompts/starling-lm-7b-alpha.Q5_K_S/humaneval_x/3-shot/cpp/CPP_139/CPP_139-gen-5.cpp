    long long res=1;
    int i;
    if (n<2)
    return 1;
    for (i=2;i<=n;i++)
    res*=i;
    return res;
}



