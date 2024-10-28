    int fib[4]={0,0,2,0};
    int i;
    if (n>=4)
    {
        for (i=4;i<=n;i++)
        {
            fib[i%4]=fib[(i-1)%4]+fib[(i-2)%4]+fib[(i-3)%4]+fib[(i-4)%4];
        }
    }
    return fib[n%4];
}

