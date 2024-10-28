    int fib[4];
    fib[0]=0;
    fib[1]=0;
    fib[2]=2;
    fib[3]=0;
    int i;
    for (i=4;i<=n;i++)
    {
        fib[i%4]=fib[(i-1)%4]+fib[(i-2)%4]+fib[(i-3)%4]+fib[(i-4)%4];
    }
    return fib[n%4];
}

