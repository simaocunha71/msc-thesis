    int a=1,b=2,c=a+b,i=3;
    while (i<n)
    {
        c=a+b;
        a=b;
        b=c;
        i++;
    }
    if (is_prime(c))
    return c;
    else
    return prime_fib(i);
}


