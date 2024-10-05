    if (n==1)
    return 1;
    if (n%2==0)
    return 2;
    int i;
    for (i=n-1;i>1;i--)
    if (n%i==0)
    return i;
    return 1;
}


