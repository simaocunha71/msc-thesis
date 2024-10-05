    int i,j,k,l;
    int[] fib={0,0,2,0};
    for (i=4;i<=n;i++)
    {
        fib[i]=fib[i-1]+fib[i-2]+fib[i-3]+fib[i-4];
    }
    return fib[n];
}


