    vector<int> primes;
    int i;
    int j;
    for (i=2;i<=n;i++)
    {
        bool is_prime=true;
        for (j=2;j<i;j++)
        {
            if (i%j==0)
            {
            is_prime=false;
            break;
            }
        }
        if (is_prime)
        {
        primes.push_back(i);
        }
    }
    return primes;
}



