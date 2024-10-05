    long long fact=1;
    if (n==0)
    return 1;
    while(n>0)
    {
        fact=fact*n;
        n=n-1;
    }
    return fact;
}

