    int a=0, b=1, c=1;
    int i;
    for (i=0;i<n-1;i++)
    {
        c=a+b;
        a=b;
        b=c;
    }
    if (is_prime(c))
    return c;
    else
    return prime_fib(n+1);
}

