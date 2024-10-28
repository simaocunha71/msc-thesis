    vector<int> primes;
    for (int i=2;i<n;i++)
    {
        bool is_prime=true;
        for (int j=2;j*j<=i;j++)
        {
            if (i%j==0)
            {
                is_prime=false;
                break;
            }
        }
        if (is_prime)
            primes.push_back(i);
    }
    return primes;
} // end of function count_up_to
// You can also use the Sieve of Eratosthenes algorithm for this problem. It is more efficient than the above solution for large values of n.