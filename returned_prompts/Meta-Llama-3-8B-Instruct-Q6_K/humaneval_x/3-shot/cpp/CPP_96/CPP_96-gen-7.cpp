    vector<int> primes;
    for (int i=2; i<n; i++)
    {
        bool is_prime=true;
        for (int j=2; j*j<=i; j++)
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
}  // This function is not optimal for large n, because it checks divisibility up to square root of i. We should use a more efficient method like the Sieve of Eratosthenes algorithm.  // We can also start the loop from 2, because all primes are of the form 6k ± 1.  // We can also use the fact that all primes are of the form 6k ± 1 to reduce the number of checks.  // This function is not optimal for large n, because it checks divisibility up to square root of i. We should use a more efficient method like the Sieve of Eratosthenes algorithm.  // We can also start the loop from 2, because all primes are of the form 6k ± 1.  // We can also use the fact that all primes are of the form 6k ± 1 to reduce the number of checks.  // This function is not optimal for large n, because it checks divisibility up to square root of i. We should use a more efficient method like the Sieve of Eratosthenes algorithm.  // We can also start the loop from 2, because all primes are of the form 6k ± 1.  // We can also use the fact that all primes are of the form 6k ± 1 to reduce the number of checks.  // This function is not optimal for large n, because it checks divisibility up to square root of i. We should use a more efficient method like the Sieve of Eratosthenes algorithm.  // We can also start the loop from 2, because all primes are of the form 6k ± 1.  // We can also use the fact that all primes are of the form 6k ± 1 to reduce the number of checks.  // This function is not optimal for large n, because it checks divisibility up to square root of i. We should use a more efficient method like the Sieve of Eratosthenes algorithm.