    vector<int> primes;
    int i,j;
    int n_sqrt=(int)sqrt(n);
    for (i=2;i<=n_sqrt;i++)
    {
        if (n%i==0)
        return primes;
        for (j=i;j<=n_sqrt;j+=i)
        if (j*i<=n)
        primes.push_back(j*i);
    }
    primes.push_back(n);
    return primes;
}


