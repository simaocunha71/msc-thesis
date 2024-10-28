    int i;
    for (i=2;i<=n;i++)
    {
        while (n%i==0)
        {
            n=n/i;
        }
    }
    return n;
}

