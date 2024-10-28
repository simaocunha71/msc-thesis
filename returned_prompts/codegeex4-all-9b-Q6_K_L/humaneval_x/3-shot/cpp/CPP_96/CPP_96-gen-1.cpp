    vector<int> primes;
    int i,j;
    for (i=2;i<n;i++)
    {
    for (j=2;j<i;j++)
    if (i%j==0) break;
    if (i==j)
    primes.push_back(i);
    }
    return primes;
}

