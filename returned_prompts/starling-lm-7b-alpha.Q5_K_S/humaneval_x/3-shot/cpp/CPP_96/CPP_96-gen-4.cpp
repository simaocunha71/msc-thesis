    vector<int> primes;
    if (n<2) return primes;
    primes.push_back(2);
    if (n<3) return primes;
    primes.push_back(3);
    if (n<6) return primes;
    int i;
    for (i=6;i<=n;i++)
    {
        bool isPrime = true;
        for (int j=2;j<i;j++)
        {
            if (i%j==0){
                isPrime = false;
                break;
            }
        }
        if (isPrime) primes.push_back(i);
    }
    return primes;
}


