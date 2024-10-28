    int fib_prime[n+1];
    fib_prime[0]=2;
    fib_prime[1]=3;
    int i;
    int j;
    int fib;
    int is_prime;
    for (i=2;i<=n;i++)
    {
        fib=fib_prime[i-1]+fib_prime[i-2];
        is_prime=1;
        for (j=2;j<=fib;j++)
        if (fib%j==0)
        {
            is_prime=0;
            break;
        }
        if (is_prime==1)
        fib_prime[i]=fib;
    }
    return fib_prime[n];
}



