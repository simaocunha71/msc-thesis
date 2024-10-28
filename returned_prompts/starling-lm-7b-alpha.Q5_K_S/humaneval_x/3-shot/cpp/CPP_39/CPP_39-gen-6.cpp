    vector<bool> primes(1000000,true);
    vector<int> fib_primes;
    int i,j,current_fib;
    primes[0]=false;
    primes[1]=false;
    for (i=2;i<primes.size();i++)
    {
        if (primes[i])
        {
            for (j=i*i;j<primes.size();j+=i)
            {
                primes[j]=false;
            }
        }
    }
    current_fib=1;
    j=1;
    while (fib_primes.size()<n)
    {
        current_fib=current_fib+j;
        if (primes[current_fib])
        {
        fib_primes.push_back(current_fib);
        }
        j=current_fib-j;
    }
    return fib_primes[n-1];
}



