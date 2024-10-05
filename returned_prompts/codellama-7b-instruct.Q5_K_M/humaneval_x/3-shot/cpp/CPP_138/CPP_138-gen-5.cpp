    int i,j;
    for (i=2;i<=n;i+=2)
    for (j=2;j<=n;j+=2)
    if (i+j+n-i-j==n)
    return true;
    return false;
}



