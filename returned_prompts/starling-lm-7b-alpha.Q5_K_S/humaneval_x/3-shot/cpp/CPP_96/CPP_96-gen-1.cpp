    int i,j;
    vector<int> primes;
    bool is_prime[n+1];
    if (n==0)
    return primes;
    if (n==1)
    return {1};
    for (i=2;i<=n;i++)
    is_prime[i]=true;
    for (i=2;i<=n;i++)
    {
        if (is_prime[i])
        {
            primes.push_back(i);
            for (j=i*i;j<=n;j+=i)
            is_prime[j]=false;
        }
    }
    return primes;
}



