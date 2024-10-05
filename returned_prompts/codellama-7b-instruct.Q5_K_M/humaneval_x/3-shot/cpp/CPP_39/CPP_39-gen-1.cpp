    int a=0;
    int b=1;
    int c=a+b;
    int i=0;
    
    while (i<n){
        a=b;
        b=c;
        c=a+b;
        i++;
    }
    if (is_prime(c))
    return c;
    else
    return prime_fib(n+1);
}


