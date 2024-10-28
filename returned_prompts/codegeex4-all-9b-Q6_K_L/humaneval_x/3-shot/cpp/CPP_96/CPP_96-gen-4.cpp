    vector<int> all_primes;
    if (n<=1)
    return all_primes;

    int i;
    for (i=2;i<n;i++)
    {
        int j;
        for (j=2;j<i;j++)
        if (i%j==0)
        break;

        if (j==i)
        all_primes.push_back(i);
    }

    return all_primes;
}

