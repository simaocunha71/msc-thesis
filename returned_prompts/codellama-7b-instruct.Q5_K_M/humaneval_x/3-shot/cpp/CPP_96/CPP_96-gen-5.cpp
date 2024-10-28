    vector<int> primes;
    for (int i=1;i<n;i++)
    {
        if (is_prime(i))
        {
            primes.push_back(i);
        }
    }
    return primes;
}

bool is_prime(int n){
    if (n==2||n==3)
    return true;
    if (n<2||n%2==0||n%3==0)
    return false;
    for (int i=5;i*i<=n;i+=6)
    if (n%i==0||n%(i+2)==0)
    return false;
    return true;
}



