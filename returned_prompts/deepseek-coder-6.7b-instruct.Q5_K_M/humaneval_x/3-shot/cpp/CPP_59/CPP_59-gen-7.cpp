    int i;
    for(i=2; i*i<=n; i++)
    {
        while(n%i==0)
        {
            n/=i;
        }
    }
    return n;
}


