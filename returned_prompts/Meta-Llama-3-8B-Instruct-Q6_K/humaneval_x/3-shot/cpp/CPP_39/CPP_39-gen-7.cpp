    int a=0,b=1,fib=1;
    while(fib<=n)
    {
        if (is_prime(fib))
        {
            return fib;
        }
        a=b;
        b=fib+a;
        fib=b;
    }
    return -1;
}

int is_prime(int num)
{
    if(num<2)
    {
        return 0;
    }
    for(int i=2;i*i<=num;i++)
    {
        if(num%i==0)
        {
            return 0;
        }
    }
    return 1;
}