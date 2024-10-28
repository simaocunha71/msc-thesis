    int i;
    if (n==1)
    return y;
    for (i=2;i<=n-1;i++)
    if (n%i==0)
    return y;
    return x;
}

