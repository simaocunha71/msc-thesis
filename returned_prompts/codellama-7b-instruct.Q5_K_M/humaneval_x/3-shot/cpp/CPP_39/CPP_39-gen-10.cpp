    int a,b;
    a=0;
    b=1;
    for (int i=0;i<n;i++)
    {
        int temp=a;
        a=b;
        b=temp+b;
    }
    if (is_prime(a))
    return a;
    else
    return prime_fib(n+1);
}
int is_prime(int n)
{
    int i;
    for (i=2;i<=n/2;i++)
    if (n%i==0)
    return 0;
    return 1;
}



