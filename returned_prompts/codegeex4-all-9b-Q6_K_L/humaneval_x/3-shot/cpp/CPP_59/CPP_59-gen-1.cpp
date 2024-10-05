    int i,j;
    for (i=2;i<n;i++)
    for (j=i;j<=n;j+=i)
    if (j==n)
    return i;
}

