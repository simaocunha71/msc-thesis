    int i;
    int primes=0;
    string hex="0123456789ABCDEF";
    string prime_hex="2357D";
    for (i=0;i<num.length();i++)
    {
        char chr=num[i];
        if (count(prime_hex.begin(),prime_hex.end(),chr)==1)
        primes+=1;
    }
    return primes;
}

